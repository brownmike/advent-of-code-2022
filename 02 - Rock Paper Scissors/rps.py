from enum import Enum
from pathlib import Path


class Throw(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def loses_against(self) -> 'Throw':
        return Throw(self.value % 3 + 1)

    def wins_against(self) -> 'Throw':
        return Throw((self.value + 1) % 3 + 1)

    def __lt__(self, other: 'Throw'):
        return self.loses_against() == other


def parse_with_strat_1(line: str) -> (Throw, Throw):
    theirs, mine = line.split(' ')
    key = {
        'A': Throw.Rock, 'X': Throw.Rock,
        'B': Throw.Paper, 'Y': Throw.Paper,
        'C': Throw.Scissors, 'Z': Throw.Scissors,
    }

    return key.get(theirs), key.get(mine)


def parse_with_strat_2(line: str) -> (Throw, Throw):
    theirs, mine = line.split(' ')
    their_key = {'A': Throw.Rock, 'B': Throw.Paper, 'C': Throw.Scissors}
    their_throw = their_key.get(theirs)

    if mine == 'X':
        return their_throw, their_throw.wins_against()
    if mine == 'Y':
        return their_throw, their_throw
    if mine == 'Z':
        return their_throw, their_throw.loses_against()


def score(theirs: Throw, mine: Throw) -> int:
    bonus_points = 0
    if theirs == mine:
        bonus_points = 3
    if theirs < mine:
        bonus_points = 6

    return mine.value + bonus_points


def main():
    data = Path('day02-input')
    total1, total2 = 0, 0
    with data.open(mode='r') as f:
        for line in f:
            l = line.strip()
            total1 += score(*parse_with_strat_1(l))
            total2 += score(*parse_with_strat_2(l))

    print(f'Total score using strat 1: {total1}')
    print(f'Total score using strat 2: {total2}')


if __name__ == '__main__':
    main()
