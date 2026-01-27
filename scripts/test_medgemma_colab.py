# MedGemma Adapter Compatibility Test
# Run this in Google Colab (with GPU runtime enabled)
# ============================================================

# 1. Install Dependencies
!pip install -q transformers accelerate bitsandbytes peft

# 2. Login to Hugging Face (MedGemma is gated)
from huggingface_hub import login
login()  # Enter your HF token when prompted

# 3. Load Base Model and Adapter
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE_MODEL = "google/medgemma-4b-it"
ADAPTER_ID = "NurseCitizenDeveloper/relational-intelligence-unsloth-medgemma"

print(f"🔄 Loading base model: {BASE_MODEL}")
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_ID)

# --- Test 1: Float16 (No Quantization) ---
print("\n--- TEST 1: Float16 (No Quantization) ---")
try:
    model_fp16 = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    model_fp16 = PeftModel.from_pretrained(model_fp16, ADAPTER_ID)
    print("✅ Float16 model loaded successfully!")
    
    # Test generation
    prompt = "<start_of_turn>user\nWhat is person-centred care?<end_of_turn>\n<start_of_turn>model\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model_fp16.device)
    outputs = model_fp16.generate(**inputs, max_new_tokens=100)
    print("Generated:", tokenizer.decode(outputs[0], skip_special_tokens=True))
    del model_fp16
    torch.cuda.empty_cache()
except Exception as e:
    print(f"❌ Float16 FAILED: {e}")

# --- Test 2: 8-bit Quantization ---
print("\n--- TEST 2: 8-bit Quantization ---")
try:
    model_8bit = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        device_map="auto",
        load_in_8bit=True,
        trust_remote_code=True,
    )
    model_8bit = PeftModel.from_pretrained(model_8bit, ADAPTER_ID)
    print("✅ 8-bit model loaded successfully!")
    
    prompt = "<start_of_turn>user\nWhat is person-centred care?<end_of_turn>\n<start_of_turn>model\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model_8bit.device)
    outputs = model_8bit.generate(**inputs, max_new_tokens=100)
    print("Generated:", tokenizer.decode(outputs[0], skip_special_tokens=True))
    del model_8bit
    torch.cuda.empty_cache()
except Exception as e:
    print(f"❌ 8-bit FAILED: {e}")

# --- Test 3: 4-bit Quantization ---
print("\n--- TEST 3: 4-bit Quantization ---")
try:
    model_4bit = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        device_map="auto",
        load_in_4bit=True,
        trust_remote_code=True,
    )
    model_4bit = PeftModel.from_pretrained(model_4bit, ADAPTER_ID)
    print("✅ 4-bit model loaded successfully!")
    
    prompt = "<start_of_turn>user\nWhat is person-centred care?<end_of_turn>\n<start_of_turn>model\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model_4bit.device)
    outputs = model_4bit.generate(**inputs, max_new_tokens=100)
    print("Generated:", tokenizer.decode(outputs[0], skip_special_tokens=True))
    del model_4bit
    torch.cuda.empty_cache()
except Exception as e:
    print(f"❌ 4-bit FAILED: {e}")

# --- Summary ---
print("\n" + "="*50)
print("SUMMARY: Check which test(s) passed above.")
print("If Float16 works but 8-bit fails, you need float16 on an A100 GPU")
print("If all fail, there may be a vocabulary mismatch in the adapter")
print("="*50)
