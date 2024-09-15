import pytest

from working_with_settings.di.di import Di


@pytest.fixture(autouse=True, scope="function")
def inject() -> Di:
    return Di()
