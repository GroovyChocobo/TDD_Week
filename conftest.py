import pytest

@pytest.fixture
def player():
    return {"health": 100, "max_health": 100, "alive": True}