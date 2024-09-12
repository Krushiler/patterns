import pytest

from working_with_settings.di.di import Di
from working_with_settings.domain.model.settings import Settings


@pytest.fixture(autouse=True, scope="function")
def inject() -> Di:
    return Di()


def test_settings(inject):
    settings = Settings()
    settings.organization_name = 'Test'
    settings.inn = '123456789012'
    settings.director_name = 'Test director'

    assert settings.organization_name == 'Test'
    assert settings.inn == '123456789012'
    assert settings.director_name == 'Test director'


def test_settings_manager_open(inject):
    manager1 = inject.get_settings_manager()
    result = manager1.open("../settings.json")
    assert result is True


def test_settings_manager_singleton(inject):
    manager1 = inject.get_settings_manager()
    manager1.open("../assets/settings_success.json.json")

    manager2 = inject.get_settings_manager()

    assert manager1.state.settings.inn == manager2.state.settings.inn
    assert manager1.state.settings.organization_name == manager2.state.settings.organization_name
