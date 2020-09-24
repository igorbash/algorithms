from sorting.sort import Sort


class CountingSort(Sort):
    """
    Counting sort when the range is R (0 - R-1)
    """
    R = 10

    def sort(self, list_to_sort: list):
        count_array = CountingSort._create_count_array(list_to_sort)
        sorted_array = CountingSort._create_sorted_array(count_array)
        list_to_sort.clear()
        list_to_sort.extend(sorted_array)

    @staticmethod
    def _create_count_array(list_to_sort):
        count_array = [0] * CountingSort.R
        for value in list_to_sort:
            count_array[value] += 1
        return count_array

    @staticmethod
    def _create_sorted_array(count_array):
        sorted_array = []
        for value, count in enumerate(count_array):
            while count > 0:
                sorted_array.append(value)
                count -= 1
        return sorted_array
