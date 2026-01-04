"""
Relational AI 4 Nursing - Hugging Face Spaces Demo
Fine-tuned Llama-3-8B for person-centred nursing documentation.
"""
import gradio as gr
import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
from huggingface_hub import login
from mdt_orchestrator import MDTOrchestrator

# Login to Hugging Face (Requires HF_TOKEN secret in Space settings)
if os.getenv("HF_TOKEN"):
    login(token=os.getenv("HF_TOKEN"))

# ============================================
# MODEL CONFIGURATION
# ============================================
MODEL_ID = "NurseCitizenDeveloper/nursing-llama-3-8b-fons"

# Alpaca prompt format (used during training)
ALPACA_TEMPLATE = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{context}

### Response:
"""

# ============================================
# LOAD MODEL (PEFT / Adapter Compatible)
# ============================================
BASE_MODEL = "NousResearch/Meta-Llama-3-8B" # Non-gated alternative to original Meta repo
print(f"🔄 Loading base model: {BASE_MODEL}")

# tokenizer should be loaded from the adapter repo if it has custom tokens
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Load base model (Requires HF_TOKEN secret in Space settings)
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

# Load Adapters
from peft import PeftModel
print(f"🧩 Applying nursing adapters from: {MODEL_ID}")
model = PeftModel.from_pretrained(model, MODEL_ID)

print("✅ Super-Gold Model loaded and ready!")

# ============================================
# GENERATION FUNCTION
# ============================================
def generate_response(instruction: str, context: str, max_tokens: int = 256, temperature: float = 0.7):
    """Generate a response using the fine-tuned model."""
    prompt = ALPACA_TEMPLATE.format(instruction=instruction, context=context)
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # Streaming setup
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    generation_kwargs = dict(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=0.9,
        repetition_penalty=1.2,
        streamer=streamer,
    )
    
    # Run generation in a thread for streaming
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()
    
    # Yield tokens as they arrive
    partial_response = ""
    for new_text in streamer:
        partial_response += new_text
        yield partial_response


def rewrite_clinical_note(original_note: str):
    """Rewrite a clinical note using person-centred language."""
    instruction = "Rewrite this clinical note using person-centred, dignified language that respects the patient. Focus on their experience and preferences."
    for response in generate_response(instruction, original_note, max_tokens=300):
        yield response


def skin_tone_assessment(patient_info: str):
    """Generate skin tone-aware pressure ulcer assessment."""
    instruction = "Generate a comprehensive skin assessment for pressure ulcer risk. Include specific guidance for documenting skin tone changes, ensuring the assessment is appropriate for all skin tones including darker complexions."
    for response in generate_response(instruction, patient_info, max_tokens=400):
        yield response


def adpie_generator(clinical_scenario: str):
    """Generate structured ADPIE nursing documentation."""
    instruction = "Structure this clinical scenario using the ADPIE nursing process: Assessment, Diagnosis, Planning, Implementation, and Evaluation. Provide clear, actionable documentation for each step."
    for response in generate_response(instruction, clinical_scenario, max_tokens=500):
        yield response


def semantic_review(note: str):
    """Perform openEHR-inspired semantic analysis on a nursing note."""
    instruction = """Perform a SUPER-GOLD SEMANTIC AUDIT on this nursing note.
    Your goal is to exceed openEHR standards by validating:
    1. ONC Empathy Index (1-5): Score the therapeutic depth of the interaction.
    2. Relief Engagement (1-5): Score the authentic partnership level.
    3. Mandatory Equity Gate: Verify if skin tone or cultural background is documented to guide clinical assessment.
    4. NANDA-I Mapping: Suggest formal Nursing Diagnoses.
    5. ADPIE Integrity: Ensure Assessment leads logically to Implementation.
    
    If any 'Relational' or 'Equity' markers are missing, provide a 'Relational Intervention' to fix it."""
    for response in generate_response(instruction, note, max_tokens=500):
        yield response


# ============================================
# GRADIO UI
# ============================================
# Custom CSS for NHS-inspired theme
custom_css = """
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}
.gr-button-primary {
    background-color: #005eb8 !important;
    border-color: #005eb8 !important;
}
.gr-button-primary:hover {
    background-color: #003d7a !important;
}
footer {
    visibility: hidden;
}
"""

# Header HTML
header_html = """
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #005eb8 0%, #003d7a 100%); border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; margin: 0; font-size: 2.5em;">🤖 Relational AI 4 Nursing</h1>
    <p style="color: #e8edee; margin-top: 10px; font-size: 1.1em;">
        The first open-source LLM fine-tuned on FONS literature for person-centred, equitable clinical documentation.
    </p>
    <div style="margin-top: 15px;">
        <span style="background: #4c9aff; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">🎯 Equity Score: 8/10</span>
        <span style="background: #7c3aed; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">💬 Person-Centred: 7.6/10</span>
        <span style="background: #059669; color: white; padding: 5px 15px; border-radius: 20px; margin: 0 5px; font-size: 0.9em;">✅ FONS Aligned</span>
    </div>
</div>
"""

with gr.Blocks(css=custom_css, title="Relational AI 4 Nursing") as demo:
    gr.HTML(header_html)
    
    with gr.Tabs():
        # Tab 1: Chat Interface
        with gr.TabItem("💬 Chat Assistant"):
            gr.Markdown("### Ask questions about nursing practice, care planning, or clinical documentation.")
            chatbot = gr.ChatInterface(
                fn=chat_interface,
                examples=[
                    "What are the key principles of person-centred care?",
                    "How should I document a patient's refusal of medication?",
                    "Explain the importance of relational care in nursing.",
                    "What is the FONS approach to practice development?",
                ],
                retry_btn=None,
                undo_btn=None,
            )
        
        # Tab 2: Language Rewriter
        with gr.TabItem("✨ Language Rewriter"):
            gr.Markdown("""
            ### Transform Clinical Jargon into Person-Centred Language
            Paste a clinical note written in traditional medical language, and Relational AI will rewrite it 
            using dignified, person-centred language that respects the patient's experience.
            """)
            
            with gr.Row():
                with gr.Column():
                    original_input = gr.Textbox(
                        label="Original Clinical Note",
                        placeholder="e.g., 'Patient non-compliant with medication. Refused to ambulate. Agitated and uncooperative.'",
                        lines=5,
                    )
                    rewrite_btn = gr.Button("✨ Rewrite with Relational AI", variant="primary")
                
                with gr.Column():
                    rewritten_output = gr.Textbox(
                        label="Person-Centred Version",
                        lines=8,
                        interactive=False,
                    )
            
            rewrite_btn.click(
                fn=rewrite_clinical_note,
                inputs=original_input,
                outputs=rewritten_output,
            )
            
            gr.Examples(
                examples=[
                    ["Patient is non-compliant with medication regimen. Refused physiotherapy session. Combative when staff attempted to assist with personal care."],
                    ["Elderly female, confused and agitated. Fall risk. Requires 1:1 supervision. Not eating."],
                    ["Patient is a poor historian. Unable to provide reliable information about symptoms."],
                ],
                inputs=original_input,
            )
        
        # Tab 3: Skin Tone Assessment
        with gr.TabItem("🎨 Equity: Skin Assessment"):
            gr.Markdown("""
            ### Equitable Skin Tone Assessment
            Standard pressure ulcer tools (like the Braden Scale) often fail to capture risks for patients with darker skin tones.
            This tool generates assessments that account for **all skin tones**, ensuring equitable care.
            
            > **Why this matters:** Early signs of pressure damage (erythema) appear differently on darker skin. 
            > Relational AI was specifically trained to address this gap.
            """)
            
            patient_info_input = gr.Textbox(
                label="Patient Information",
                placeholder="e.g., 'Mrs. Johnson, 78 years old, limited mobility, dark brown skin tone (Fitzpatrick V), admitted for hip fracture.'",
                lines=3,
            )
            skin_btn = gr.Button("🔍 Generate Equitable Assessment", variant="primary")
            skin_output = gr.Textbox(label="Skin Assessment", lines=10, interactive=False)
            
            skin_btn.click(
                fn=skin_tone_assessment,
                inputs=patient_info_input,
                outputs=skin_output,
            )
            
            gr.Examples(
                examples=[
                    ["78-year-old woman with dark skin (Fitzpatrick Type V), admitted for stroke rehabilitation, limited mobility, incontinent."],
                    ["65-year-old man, South Asian heritage, diabetic, peripheral neuropathy, using wheelchair."],
                ],
                inputs=patient_info_input,
            )
        
        # Tab 4: ADPIE Generator
        with gr.TabItem("📋 ADPIE Generator"):
            gr.Markdown("""
            ### Structure Your Documentation Using ADPIE
            Enter a clinical scenario, and Relational AI will help you organize it using the nursing process:
            - **A**ssessment
            - **D**iagnosis
            - **P**lanning
            - **I**mplementation
            - **E**valuation
            """)
            
            scenario_input = gr.Textbox(
                label="Clinical Scenario",
                placeholder="e.g., 'Patient reports difficulty sleeping due to pain in left hip. Pain score 7/10. Currently on paracetamol PRN.'",
                lines=4,
            )
            adpie_btn = gr.Button("📋 Generate ADPIE Documentation", variant="primary")
            adpie_output = gr.Textbox(label="Structured ADPIE Notes", lines=15, interactive=False)
            
            adpie_btn.click(
                fn=adpie_generator,
                inputs=scenario_input,
                outputs=adpie_output,
            )

        # Tab 6: Semantic Review (Now Tab 6, previously Tab 5)
        with gr.TabItem("🧠 Semantic Review"):
            gr.Markdown("""
            ### 🧠 Clinical Semantic Analysis (openEHR Inspired)
            This tool performs a deep audit of your nursing documentation. It checks the note against 
            the **ONC Relational Care Logical Model** and suggests formal **NANDA-I** mappings.
            
            > **Goal:** To ensure documentation is not just "data" but high-quality **Clinical Knowledge**.
            """)
            
            with gr.Row():
                with gr.Column():
                    review_input = gr.Textbox(
                        label="Patient Progress Note",
                        placeholder="Paste a note for a semantic audit...",
                        lines=5,
                    )
                    review_btn = gr.Button("🧠 Perform Semantic Review", variant="primary")
                
                with gr.Column():
                    review_output = gr.Textbox(
                        label="Semantic Audit & Mapping Suggestions",
                        lines=12,
                        interactive=False,
                    )
            
            review_btn.click(
                fn=semantic_review,
                inputs=review_input,
                outputs=review_output,
            )
            
            gr.Examples(
                examples=[
                    ["Patient seems isolated today. Minimal eye contact. Did not participate in group activity."],
                    ["Mrs. Singh (dark skin tone) has area of hyperpigmentation on sacrum. Patient prefers to be called 'Dadi'."],
                ],
                inputs=review_input,
            )

        # Tab 6: Super-Gold Safety Gates
        with gr.TabItem("🛡️ Safety & Quality Gates"):
            gr.Markdown("""
            ### Clinical Safety & Dignity Gates
            This tool validates your documentation against the new **"Super-Gold"** invariants.
            It checks for:
            *   **Mobility**: Bedbound patients MUST have a Pressure Ulcer risk assessment (Waterlow/Braden).
            *   **Nutrition**: Dysphagia signs MUST trigger a "Protected Mealtimes" flag.
            *   **Elimination**: Catheter care MUST reference a specific device (Dignity check).
            *   **Hygiene**: NBM patients MUST have frequent Oral Care planned.
            """)
            
            with gr.Row():
                with gr.Column():
                    gates_input = gr.Textbox(
                        label="Clinical Note / Care Plan",
                        placeholder="e.g., 'Patient is bedbound. Sacrum red. NBM for surgery tomorrow.'",
                        lines=5,
                    )
                    gates_btn = gr.Button("🛡️ Run Safety Gate Check", variant="primary")
                
                with gr.Column():
                    gates_output = gr.Textbox(
                        label="Safety Gate Results",
                        lines=10,
                        interactive=False,
                    )
            
            def check_safety_gates(note: str):
                """Run specific safety gate checks on the note."""
                instruction = """Perform a SAFETY GATE CHECK on this nursing note against these 4 rules. 
                Output PASS or FAIL for each gate with a reason.
                
                1. [Mobility Gate]: If 'bedbound' or 'immobile', is a Pressure Ulcer Risk Assessment (Braden/Waterlow/Purpose T) documented?
                2. [Nutrition Gate]: If 'dysphagia' or 'choking risk', is 'Protected Mealtimes' or 'Swallow Plan' mentioned?
                3. [Hygiene Gate]: If 'NBM' (Nil By Mouth), is 'Oral Care' frequency specified?
                4. [Elimination Gate]: If 'catheter' is present, is the specific device/size mentioned?
                
                Format:
                🛡️ Mobility Gate: [PASS/FAIL] - Reason
                🛡️ Nutrition Gate: [PASS/FAIL] - Reason
                🛡️ Hygiene Gate: [PASS/FAIL] - Reason
                🛡️ Elimination Gate: [PASS/FAIL] - Reason
                """
                for response in generate_response(instruction, note, max_tokens=400):
                    yield response

            gates_btn.click(
                fn=check_safety_gates,
                inputs=gates_input,
                outputs=gates_output,
            )
            
            gr.Examples(
                examples=[
                    ["Patient is bedbound following stroke. NBM pending speech therapy review. Catheter draining clear urine."],
                    ["Mobilising with frame. Eating and drinking well. No concerns."],
                ],
                inputs=gates_input,
            )

        # Tab 7: Virtual MDT (Multi-Agent Team)
        with gr.TabItem("🏥 Virtual MDT"):
            gr.Markdown("""
            ### Virtual Multi-Disciplinary Team Discussion
            This tool simulates an MDT meeting with specialized AI agents:
            *   **🩹 Tissue Viability Specialist**: Skin equity and pressure risk.
            *   **💚 Relational Facilitator**: Empathy and person-centred language.
            *   **🛡️ Safety Auditor**: Safety Gates validation.
            *   **📋 Clinical Coordinator**: Synthesizes the final "Super-Gold" Care Plan.
            
            > Enter a complex patient case below to see how the team collaborates.
            """)
            
            with gr.Row():
                with gr.Column(scale=1):
                    mdt_input = gr.Textbox(
                        label="Patient Case / Handover Note",
                        placeholder="e.g., '78-year-old patient, dark skin tone, bedbound following stroke, NBM pending swallow review, catheter in situ.'",
                        lines=6,
                    )
                    mdt_btn = gr.Button("🏥 Start MDT Discussion", variant="primary")
                
                with gr.Column(scale=2):
                    mdt_output = gr.Markdown(
                        label="MDT Discussion Log",
                        value="*Results will appear here...*",
                    )
            
            # Initialize the orchestrator with the generate_response function
            orchestrator = MDTOrchestrator(generate_response)
            
            def run_mdt_discussion(patient_case: str):
                """Run the MDT and yield the formatted discussion."""
                full_output = ""
                for chunk in orchestrator.run_discussion(patient_case):
                    full_output += chunk
                    yield full_output

            mdt_btn.click(
                fn=run_mdt_discussion,
                inputs=mdt_input,
                outputs=mdt_output,
            )
            
            gr.Examples(
                examples=[
                    ["78-year-old lady, dark skin (Fitzpatrick V), bedbound after hip fracture. NBM pending swallow assessment. IDC draining haematuria. Family anxious about care home placement."],
                    ["65-year-old man with dementia, frequent falls. Skin intact but reluctant to mobilise. Wife 'Dadi' is his main carer and prefers to be involved in all decisions."],
                ],
                inputs=mdt_input,
            )

    # Footer
    gr.Markdown("""
    ---
    **Model:** [NurseCitizenDeveloper/nursing-llama-3-8b-fons](https://huggingface.co/NurseCitizenDeveloper/nursing-llama-3-8b-fons) | 
    **License:** CC BY-NC 3.0 | 
    **IG:** [opennursingcoreig.com](https://opennursingcoreig.com)
    
    > ⚠️ **Disclaimer:** This tool is for research and educational purposes only. All clinical documentation must be verified by a registered nurse.
    """)

# Launch
if __name__ == "__main__":
    demo.queue().launch()



