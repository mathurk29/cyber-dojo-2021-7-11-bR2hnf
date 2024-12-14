from enum import Enum


class LifeState(Enum):
    LIVING = "*"
    DEAD = "."


class LifeScience:

    def __init__(self):
        self._life_matrix = []

    def life_input(self):
        rows, _ = [int(x) for x in input().split()]
        for _ in range(rows):
            row = input()
            self._life_matrix.append(list(row))

    def process(self): ...

    def life_output(self):
        for row in self._life_matrix:
            print("".join(row))  # Convert list back to string for display


def main():
    life_science = LifeScience()
    life_science.life_input()
    life_science.process()
    life_science.life_output()


if __name__ == "__main__":
    main()
