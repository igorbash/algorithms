from random import randint

from sorting.sort import Sort


class QuickSort(Sort):
    def sort(self, list_to_sort: list):
        QuickSort._quick_sort(list_to_sort, 0, len(list_to_sort) - 1)

    @staticmethod
    def _quick_sort(list_to_sort, low, high):
        if low < high:
            partition_index = QuickSort._partition(list_to_sort, low, high)
            QuickSort._quick_sort(list_to_sort, low, partition_index - 1)
            QuickSort._quick_sort(list_to_sort, partition_index + 1, high)

    @staticmethod
    def _partition(list_to_sort, low, high):
        pivot = QuickSort._get_pivot_in_the_beginning(list_to_sort, low, high)
        pivot = QuickSort._sort_array_with_pivot(list_to_sort, low, high, pivot)
        return pivot

    @staticmethod
    def _get_pivot_in_the_beginning(list_to_sort, low, high):
        pivot = randint(low, high)
        list_to_sort[low], list_to_sort[pivot] = list_to_sort[pivot], list_to_sort[low]
        return low

    @staticmethod
    def _sort_array_with_pivot(list_to_sort, low, high, pivot):
        while True:
            while low <= high and list_to_sort[low] <= list_to_sort[pivot]:
                low += 1
            while low <= high and list_to_sort[high] >= list_to_sort[pivot]:
                high -= 1
            if low <= high:
                list_to_sort[low], list_to_sort[high] = list_to_sort[high], list_to_sort[low]
            else:
                break
        list_to_sort[pivot], list_to_sort[high] = list_to_sort[high], list_to_sort[pivot]
        return high
