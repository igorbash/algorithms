from sorting.bubble_sort import BubbleSort


class TestBubbleSort:
    sorter = BubbleSort()

    def test_sort_empty_list(self):
        list_to_sort = []

        self.sorter.sort(list_to_sort)

        assert list_to_sort == []

    def test_one_item_list_sort(self):
        list_to_sort = [1]

        self.sorter.sort(list_to_sort)

        assert list_to_sort == [1]

    def test_sort(self):
        list_to_sort = [1, 2, 32, -321, 32, 0, 231]

        self.sorter.sort(list_to_sort)

        assert list_to_sort == [-321, 0, 1, 2, 32, 32, 231]
