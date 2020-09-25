from abc import ABC, abstractmethod


class Sort(ABC):
    """
    Sort class that sorts lists with specific sorting algorithm
    """

    @abstractmethod
    def sort(self, list_to_sort: list):
        """
        sorting given list
        :param list_to_sort: the list to sort
        """
        pass
