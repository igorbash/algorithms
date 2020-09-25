from sorting.sort import Sort


class SelectionSort(Sort):
    def sort(self, list_to_sort: list):
        list_length = len(list_to_sort)
        for i in range(list_length):
            min_index = SelectionSort._find_min_index_in_list(list_to_sort[i:]) + i
            list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]

    @staticmethod
    def _find_min_index_in_list(list_to_sort: list):
        min_index = 0
        for i in range(len(list_to_sort)):
            if list_to_sort[i] < list_to_sort[min_index]:
                min_index = i
        return min_index
