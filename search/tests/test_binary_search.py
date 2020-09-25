from search.binary_search import BinarySearch


def test_binary_search_empty_list():
    sorted_list = []

    result = BinarySearch.search(sorted_list, 1)

    assert result is None


def test_binary_search_one_item_list():
    sorted_list = [1]

    found_result = BinarySearch.search(sorted_list, 1)
    not_found_result = BinarySearch.search(sorted_list, 2)

    assert found_result == 0
    assert not_found_result is None


def test_binary_search():
    sorted_list = [1, 2, 6, 74, 2434, 43232, 3243243]

    found_result = BinarySearch.search(sorted_list, 6)
    found_result_right_side = BinarySearch.search(sorted_list, 3243243)
    not_fount_result = BinarySearch.search(sorted_list, 224)

    assert found_result == 2
    assert found_result_right_side == 6
    assert not_fount_result is None
