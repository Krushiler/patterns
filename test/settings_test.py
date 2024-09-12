import pytest

from working_with_settings.di.di import Di
from working_with_settings.domain.model.organization.settings import Settings


@pytest.fixture(autouse=True, scope="function")
def inject() -> Di:
    return Di()


def test_settings(inject):
    settings = Settings(
        bic='Test',
        inn='123456789012',
        ownership_form='Test director',
        account='Test director'
    )

    assert settings.bic == 'Test'
    assert settings.inn == '123456789012'
    assert settings.ownership_form == 'Test director'
    assert settings.account == 'Test director'


def test_settings_manager_singleton(inject):
    manager1 = inject.get_settings_manager()
    manager1.open("../assets/settings_success.json")

    manager2 = inject.get_settings_manager()

    assert manager1.state.settings.inn == manager2.state.settings.inn
    assert manager1.state.settings.ownership_form == manager2.state.settings.ownership_form
