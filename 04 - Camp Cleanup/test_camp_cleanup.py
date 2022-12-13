import pytest

from camp_cleanup import Range


@pytest.mark.parametrize('container,containee', [
    (Range(1, 2), Range(1, 1)),
    (Range(1, 1), Range(1, 1)),
    (Range(100, 200), Range(101, 199)),
])
def test_range_contains_other_range(container: Range, containee: Range):
    assert container.contains(containee)


@pytest.mark.parametrize('r1,r2', [
    (Range(1, 1), Range(1, 2)),
    (Range(2, 3), Range(1, 4)),
    (Range(2, 3), Range(1, 4)),
])
def test_range_does_not_contain_other_range(r1: Range, r2: Range):
    assert not r1.contains(r2)


def test_constructing_from_string():
    assert Range.from_string('3-5') == Range(3, 5)


@pytest.mark.parametrize('r1,r2', [
    (Range(5, 7), Range(7, 9)),
    (Range(2, 8), Range(3, 7)),
    (Range(6, 6), Range(4, 6)),
    (Range(2, 6), Range(4, 8)),
])
def test_overlaps_with(r1: Range, r2: Range):
    assert r1.overlaps_with(r2)
    assert r2.overlaps_with(r1)
