import pytest
from reactivex import Observable

from working_with_settings.domain.model.organization.organization import Organization
from working_with_settings.data.mapping.settings_mapper import SettingsMapper
from working_with_settings.di.di import Di
from working_with_settings.domain.exceptions.field_exceptions import InvalidTypeException, InvalidLengthException, \
    InvalidFormatException
from working_with_settings.domain.model.organization.settings import Settings


def test_settings(inject: Di):
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


def test_mapper_validation():
    mapper = SettingsMapper()
    with pytest.raises(InvalidTypeException):
        mapper.from_json('')


def test_settings_manager_loading(inject: Di):
    manager = inject.get_settings_manager()
    res = manager.open("assets/settings_success.json")

    assert res is True


def test_settings_manager_singleton(inject: Di):
    manager1 = inject.get_settings_manager()
    manager1.open(5)

    manager2 = inject.get_settings_manager()

    assert isinstance(manager1.stream, Observable)

    assert manager1.state.settings.inn == manager2.state.settings.inn
    assert manager1.state.settings.ownership_form == manager2.state.settings.ownership_form
    assert manager1.state.file_name == manager2.state.file_name
    assert manager1.state.error == manager2.state.error
    assert manager1.state.with_error(None).error is None


def test_settings_validation():
    settings = Settings(
        bic='Test',
        inn='123456789012',
        ownership_form='Test director',
        account='Test director'
    )

    with pytest.raises(InvalidLengthException):
        settings.inn = '1234567890'

    with pytest.raises(InvalidTypeException):
        settings.inn = 123

    with pytest.raises(InvalidFormatException):
        settings.inn = '12345678901B'

    with pytest.raises(InvalidTypeException):
        settings.ownership_form = 123

    with pytest.raises(InvalidTypeException):
        settings.account = 123

    with pytest.raises(InvalidTypeException):
        settings.bic = 123


def test_organization_settings():
    settings = Settings(
        bic='Test',
        inn='123456789012',
        ownership_form='Test director',
        account='Test director'
    )

    org = Organization(settings=settings)

    assert org.inn == '123456789012'
    assert org.ownership_form == 'Test director'
    assert org.bic == 'Test'
    assert org.account == 'Test director'
