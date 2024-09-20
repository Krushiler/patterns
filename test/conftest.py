import pytest

from working_with_settings.di.di import Di


@pytest.fixture
def inject() -> Di:
    try:
        yield Di()
    finally:
        pass

