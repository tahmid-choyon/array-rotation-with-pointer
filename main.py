from typing import Any, List

from errors import IndexOutOfBoundError, SizeLimitExceededError


class CircularArray:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.__items: List[Any] = []
        self._pointers: List[int] = []

    def __getitem__(self, index:int) -> Any:
        return self.get(index)

    def get(self, index: int) -> Any:
        if index >= len(self.__items):
            raise IndexOutOfBoundError
        return self.__items[self._pointers[index]]

    def clone(self) -> List[Any]:
        items = []
        for i in range(len(self.__items)):
            items.append(self.get(i))
        return items

    def append(self, item: Any) -> None:
        if len(self.__items) == self.size:
            raise SizeLimitExceededError

        self.__items.append(item)
        self._pointers.append(len(self.__items) - 1)

    def rotate_left_once(self) -> None:
        for i in range(len(self.__items)):
            self._pointers[i] += 1
            if self._pointers[i] >= len(self.__items):
                self._pointers[i] = 0

    def rotate_right_once(self) -> None:
        for i in range(len(self.__items)):
            self._pointers[i] -= 1
            if self._pointers[i] < 0:
                self._pointers[i] = len(self.__items) - 1
