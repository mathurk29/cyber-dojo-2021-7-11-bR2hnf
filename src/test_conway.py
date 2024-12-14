import pytest
from pytest import MonkeyPatch
from conway import LifeScience


@pytest.fixture
def life_science_instance() -> LifeScience:
    return LifeScience()


def test_life_input(
    monkeypatch: MonkeyPatch, life_science_instance: LifeScience
) -> None:
    mock_input = "4 8\n........\n....*...\n...**...\n.....*.."
    input_lines = iter(mock_input.split("\n"))  # Convert input to an iterator
    expected_input = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "*", ".", ".", "."],
        [".", ".", ".", "*", "*", ".", ".", "."],
        [".", ".", ".", ".", "*", ".", ".", "."],
    ]
    monkeypatch.setattr("builtins.input", lambda: next(input_lines))
    life_science_instance.life_input()
    assert life_science_instance._life_matrix == expected_input
