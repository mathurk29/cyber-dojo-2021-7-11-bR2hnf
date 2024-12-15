import copy
from enum import Enum


class CellState(Enum):
    LIVING = "*"
    DEAD = "."


class LifeScience:

    def __init__(self):
        self._life_matrix: list = []

    def seed(self):
        rows, _ = [int(x) for x in input().split()]
        for _ in range(rows):
            row = input()
            self._life_matrix.append(list(row))

    def next_generation(self):
        new_matrix = copy.deepcopy(self._life_matrix)
        for row_idx in range(len(self._life_matrix)):
            for col_idx in range(len(self._life_matrix[row_idx])):
                live_neighbors = self.calculate_live_neighbors(row_idx, col_idx)
                is_live = self._isLiveCell(row_idx, col_idx)
                if is_live and (live_neighbors < 2 or live_neighbors > 3):
                    new_matrix[row_idx][col_idx] = CellState.DEAD.value
                elif not is_live and live_neighbors == 3:
                    new_matrix[row_idx][col_idx] = CellState.LIVING.value
        self._life_matrix = new_matrix

    def _isLiveCell(self, row_idx, col_idx):
        return self._life_matrix[row_idx][col_idx] == CellState.LIVING.value

    def print_life_matrix(self):
        for row in self._life_matrix:
            print("".join(row))  # Convert list back to string for display

    def calculate_live_neighbors(self, row_idx, col_idx):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        live_neighbors = 0
        for d in directions:
            r, c = row_idx + d[0], col_idx + d[1]
            if 0 <= r < len(self._life_matrix) and 0 <= c < len(
                self._life_matrix[0]
            ):
                if self._life_matrix[r][c] == CellState.LIVING.value:
                    live_neighbors += 1
        return live_neighbors


def main():
    life_science = LifeScience()
    life_science.seed()
    life_science.next_generation()
    life_science.print_life_matrix()


if __name__ == "__main__":
    main()
