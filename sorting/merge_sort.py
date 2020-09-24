from sorting.sort import Sort


class MergeSort(Sort):
    def sort(self, list_to_sort: list):
        if len(list_to_sort) > 1:
            sorted_list = MergeSort._merge_sort(list_to_sort)
            list_to_sort.clear()
            list_to_sort.extend(sorted_list)

    @staticmethod
    def _merge_sort(list_to_sort: list):
        if len(list_to_sort) > 1:
            middle_index = len(list_to_sort) // 2
            left_list = list_to_sort[:middle_index]
            right_list = list_to_sort[middle_index:]
            left_list = MergeSort._merge_sort(left_list)
            right_list = MergeSort._merge_sort(right_list)
            return MergeSort._merge(left_list, right_list)
        return list_to_sort

    @staticmethod
    def _merge(left_list, right_list):
        merged_list = MergeSort._merge_lists(left_list, right_list)
        merged_list = MergeSort._add_items_left(left_list, merged_list)
        merged_list = MergeSort._add_items_left(right_list, merged_list)
        return merged_list

    @staticmethod
    def _merge_lists(left_list, right_list):
        merged_list = []
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0] < right_list[0]:
                merged_list.append(left_list[0])
                left_list.pop(0)
            else:
                merged_list.append(right_list[0])
                right_list.pop(0)
        return merged_list

    @staticmethod
    def _add_items_left(list_with_items_left, merged_list):
        for item in list_with_items_left:
            merged_list.append(item)
        return merged_list
