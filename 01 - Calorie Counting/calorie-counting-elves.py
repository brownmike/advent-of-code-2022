from pathlib import Path
from queue import PriorityQueue


class CalorieCounter:
    def __init__(self, calorie_records: Path):
        self._priority_queue = PriorityQueue(maxsize=3)
        self._parse(calorie_records)

    @property
    def top3(self):
        return list(self._priority_queue.queue)

    def _parse(self, calorie_records: Path):
        with calorie_records.open(mode='r') as f:
            current_elf_total = 0
            for line in f:
                if line == '\n':
                    self._record_value(current_elf_total)
                    current_elf_total = 0
                else:
                    current_elf_total += int(line.strip())

    def _record_value(self, value: int):
        if self._priority_queue.full():
            self._priority_queue.put(max(self._priority_queue.get(), value))
        else:
            self._priority_queue.put(value)


def main():
    cc = CalorieCounter(calorie_records=Path('day01-input'))

    print(f'Max calorie load: {max(*cc.top3)}')
    print(f'Sum of top 3 calorie loads: {sum(cc.top3)}')


if __name__ == '__main__':
    main()
