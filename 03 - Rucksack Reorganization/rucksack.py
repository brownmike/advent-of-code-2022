from pathlib import Path


def get_priority(char: str):
    ordinal_value = ord(char)
    if ordinal_value < ord('a'):
        return (ordinal_value % (ord('A') - 1)) + 26
    else:
        return ordinal_value % (ord('a') - 1)


class Rucksack:
    def __init__(self, items: str):
        middle = len(items) // 2
        self.items = items
        self.compartments = items[:middle], items[middle:]
        self.unique_items = set(items)
        self._common_items = None

    @property
    def common_items(self):
        if self._common_items is None:
            self._common_items = set(self.compartments[0]).intersection(set(self.compartments[1]))

        return self._common_items

    @property
    def common_items_value(self):
        return sum(get_priority(item) for item in self.common_items)

    def __repr__(self):
        return self.items

    def __eq__(self, other):
        return self.items == other.items

    @staticmethod
    def identify_security_badge(rucksacks: list['Rucksack']) -> str:
        result = rucksacks[0].unique_items
        for rucksack in rucksacks[1:]:
            result.intersection_update(rucksack.unique_items)

        return list(result)[0]

    @staticmethod
    def get_elf_groups(rucksacks: list['Rucksack']) -> list[list['Rucksack']]:
        result = []
        group = []
        for rucksack in rucksacks:
            group.append(rucksack)

            if len(group) == 3:
                result.append(group)
                group = []

        return result


def main():
    rucksacks = [Rucksack(items) for items in Path('day03-input').read_text().splitlines()]
    total = sum(rucksack.common_items_value for rucksack in rucksacks)

    print(f'The sum of all common item values in all rucksacks is {total}')

    elf_groups = Rucksack.get_elf_groups(rucksacks)
    security_badges = [Rucksack.identify_security_badge(elf_group) for elf_group in elf_groups]
    security_badge_total_value = sum(get_priority(security_badge) for security_badge in security_badges)

    print(f'The sum of all security badge values in all elf groups is {security_badge_total_value}')


if __name__ == '__main__':
    main()
