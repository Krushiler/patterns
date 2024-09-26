import pytest

from working_with_settings.di.di import Di
from working_with_settings.domain.model.organization.settings import Settings


@pytest.fixture
def inject() -> Di:
    try:
        yield Di()
    finally:
        pass


@pytest.fixture
def settings() -> Settings:
    return Settings(inn='123456789012', bic='Test', account='Test', ownership_form='Test director')
