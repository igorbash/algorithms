class BinarySearch:
    @staticmethod
    def search(sorted_list, value):
        """
        :param sorted_list: list to search in
        :param value: value to search for
        :return: index of the value if exists, None if doesn't
        """
        return BinarySearch._binary_search(sorted_list, 0, len(sorted_list), value)

    @staticmethod
    def _binary_search(sorted_list, start, end, value):
        if start >= end:
            return None
        mid = start + ((end - start) // 2)
        if sorted_list[mid] == value:
            return mid
        if sorted_list[mid] > value:
            return BinarySearch._binary_search(sorted_list, start, mid, value)
        else:
            return BinarySearch._binary_search(sorted_list, mid + 1, end, value)
