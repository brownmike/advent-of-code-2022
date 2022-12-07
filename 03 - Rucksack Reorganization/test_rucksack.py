import pytest

from rucksack import Rucksack


def test_compartments_is_correctly_determined():
    rucksack = Rucksack(items='abcDEF')

    assert rucksack.compartments == ('abc', 'DEF')


def test_common_items_are_found():
    rucksack = Rucksack(items='aBcABC')

    assert rucksack.common_items == {'B'}


def test_common_items_value_is_correct():
    rucksack = Rucksack(items='aBcaBC')

    assert rucksack.common_items_value == 29


@pytest.mark.parametrize('encoded_items,common_items,total_value', [
    ('vJrwpWtwJgWrhcsFMMfFFhFp', {'p'}, 16),
    ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', {'L'}, 38),
    ('PmmdzqPrVvPwwTWBwg', {'P'}, 42),
    ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', {'v'}, 22),
    ('ttgJtRGJQctTZtZT', {'t'}, 20),
    ('CrZsJsPPZsGzwwsLwLmpwMDw', {'s'}, 19),
])
def test_examples_from_readme(encoded_items: str, common_items: set, total_value: int):
    rucksack = Rucksack(items=encoded_items)

    assert rucksack.common_items == common_items
    assert rucksack.common_items_value == total_value


def test_identify_security_badge():
    rucksacks = [
        Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'),
        Rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),
        Rucksack('PmmdzqPrVvPwwTWBwg'),
    ]

    assert Rucksack.identify_security_badge(rucksacks) == 'r'


def test_rucksack_equality():
    assert Rucksack('abc') == Rucksack('abc')


def test_get_elf_groups_returns_groups_of_3():
    item_lists = [
        Rucksack('FqdWDFppHWhmwwzdjvjTRTznjdMv'),
        Rucksack('ZBJrDVfQcfSRMLjZnjjM'),
        Rucksack('cBffPfbrbQcgQJggfVQJBPbCwlPtWFDWHFHhpmmGlGmlqmDG'),
        Rucksack('PNbMLgmPgRDgRtMPDdmdbmdmQrTBVCZnVnpCnNHHVZBNVZHc'),
        Rucksack('ljvvqhlvshhnrcpBZqpTcr'),
        Rucksack('zGhWzFTJvsFttddWbMRdmP'),
    ]

    expected = [
        [item_lists[0], item_lists[1], item_lists[2]],
        [item_lists[3], item_lists[4], item_lists[5]],
    ]

    assert Rucksack.get_elf_groups(item_lists) == expected
