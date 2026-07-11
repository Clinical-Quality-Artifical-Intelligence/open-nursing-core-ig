import pytest

from core.settings import Settings


def make_settings(**overrides):
    values = {
        "APP_ENV": "development",
        "USE_DATABASE": False,
        "_env_file": None,
    }
    values.update(overrides)
    return Settings(**values)


def test_application_has_no_built_in_user_passwords():
    config = make_settings()
    assert config.ADMIN_PASSWORD is None
    assert config.NURSE_PASSWORD is None
    assert config.CLINICIAN_PASSWORD is None
    assert config.ALLOW_IN_MEMORY_AUTH is False


def test_production_rejects_in_memory_authentication():
    config = make_settings(APP_ENV="production", ALLOW_IN_MEMORY_AUTH=True)
    with pytest.raises(ValueError, match="ALLOW_IN_MEMORY_AUTH"):
        config.check_security()


def test_production_rejects_known_placeholder_credentials():
    config = make_settings(APP_ENV="production", ADMIN_PASSWORD="admin" + "2025")
    with pytest.raises(ValueError, match="Placeholder"):
        config.check_security()


def test_production_postgres_requires_database_password():
    config = make_settings(APP_ENV="production", DB_TYPE="postgres")
    with pytest.raises(ValueError, match="DB_PASSWORD"):
        config.check_security()
