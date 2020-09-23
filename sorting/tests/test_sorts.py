import pytest

from sorting.bubble_sort import BubbleSort
from sorting.selection_sort import SelectionSort

sorters = [BubbleSort(),
           SelectionSort(),
           ]


@pytest.mark.parametrize('sorter', sorters)
def test_sort_empty_list(sorter):
    list_to_sort = []

    sorter.sort(list_to_sort)

    assert list_to_sort == []


@pytest.mark.parametrize('sorter', sorters)
def test_one_item_list_sort(sorter):
    list_to_sort = [1]

    sorter.sort(list_to_sort)

    assert list_to_sort == [1]


@pytest.mark.parametrize('sorter', sorters)
def test_sort(sorter):
    list_to_sort = [1, 2, 32, -321, 32, 0, 231]

    sorter.sort(list_to_sort)

    assert list_to_sort == [-321, 0, 1, 2, 32, 32, 231]
