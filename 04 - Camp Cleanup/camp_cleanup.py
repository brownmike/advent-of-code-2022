from dataclasses import dataclass
from pathlib import Path


@dataclass
class Range:
    start: int
    end: int

    def contains(self, other: 'Range') -> bool:
        return other.start >= self.start and other.end <= self.end

    def overlaps_with(self, other: 'Range') -> bool:
        return (self.start <= other.start <= self.end) or (self.start <= other.end <= self.end) or \
            (other.start <= self.start <= other.end) or (other.start <= self.end <= other.end)

    @staticmethod
    def from_string(s: str) -> 'Range':
        start, end = s.split('-')

        return Range(int(start), int(end))

    def __repr__(self):
        return f'{self.start}-{self.end}'


if __name__ == '__main__':
    redundant_assignment_pairs = []
    duplicate_work_assignment_pairs = []
    with Path('day04-input').open(mode='r') as f:
        for line in f:
            str_pairs = line.split(',')
            p1, p2 = Range.from_string(str_pairs[0]), Range.from_string(str_pairs[1])
            if p1.contains(p2) or p2.contains(p1):
                redundant_assignment_pairs.append([p1, p2])
            if p1.overlaps_with(p2):
                duplicate_work_assignment_pairs.append([p1, p2])

    print(len(redundant_assignment_pairs))
    print(len(duplicate_work_assignment_pairs))
