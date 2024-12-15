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
        [".", ".", ".", ".", ".", "*", ".", "."],
    ]
    monkeypatch.setattr("builtins.input", lambda: next(input_lines))
    life_science_instance.seed()
    assert life_science_instance._life_matrix == expected_input


def test_game_evolution(life_science_instance: LifeScience) -> None:
    # Initial game state as per the example input
    initial_state = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "*", ".", ".", "."],
        [".", ".", ".", "*", "*", ".", ".", "."],
        [".", ".", ".", ".", ".", "*", ".", "."],
    ]

    # Expected state after one evolution step as per the example output
    expected_state = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "*", "*", ".", ".", "."],
        [".", ".", ".", "*", "*", "*", ".", "."],
        [".", ".", ".", ".", "*", ".", ".", "."],
    ]

    # Manually setting the initial state to the LifeScience instance
    life_science_instance._life_matrix = initial_state

    # Run the process function which presumably applies the rules of the game
    life_science_instance.next_generation()

    assert (
        life_science_instance._life_matrix == expected_state
    ), "The game did not evolve as expected."
