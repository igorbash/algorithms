import pytest

from sorting.bubble_sort import BubbleSort
from sorting.counting_sort import CountingSort
from sorting.merge_sort import MergeSort
from sorting.quick_sort import QuickSort
from sorting.selection_sort import SelectionSort

sorters = [BubbleSort(),
           SelectionSort(),
           MergeSort(),
           QuickSort()]


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


@pytest.mark.parametrize('sorter', sorters)
def test_sort_2(sorter):
    list_to_sort = [8, 2, 32, -321, 32, 0, 231, 3]

    sorter.sort(list_to_sort)

    assert list_to_sort == [-321, 0, 2, 3, 8, 32, 32, 231]


@pytest.mark.parametrize('list_to_sort,sorted_list', [([], []),
                                                      ([1], [1]),
                                                      ([2, 2, 1, 3, 1, 0, 5, 9, 7, 6], [0, 1, 1, 2, 2, 3, 5, 6, 7, 9])])
def test_counting_sort(list_to_sort, sorted_list):
    CountingSort().sort(list_to_sort)

    assert list_to_sort == sorted_list
