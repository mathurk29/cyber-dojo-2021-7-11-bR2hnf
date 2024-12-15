import pytest
from hiker import global_answer, Hiker


@pytest.mark.skip
def test_global_function():
    assert global_answer() == 42


@pytest.mark.skip
def test_instance_method():
    assert Hiker().instance_answer() == 42
