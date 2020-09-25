from sorting.sort import Sort


class BubbleSort(Sort):
    def sort(self, list_to_sort: list):
        list_length = len(list_to_sort)
        for i in range(list_length - 1):
            for j in range(list_length - i - 1):
                if list_to_sort[j] > list_to_sort[j + 1]:
                    list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
