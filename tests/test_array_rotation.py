import pytest
from errors import IndexOutOfBoundError, SizeLimitExceededError
from pytest import raises

from main import CircularArray


def each(fn, items):
    for item in items:
        fn(item)


class TestArrayRotation:
    def test_getitem(self):
        array = CircularArray(size=2)

        array.append(1)
        array.append(2)

        assert array[0] == 1
        assert array[1] == 2


    @pytest.mark.parametrize('size, items, index', [
        (2, [1, None], 3),
        (3, [10], 1),
        (100, [i for i in range(50)], 92),
    ])
    def test_getitem_raises_error(self, size, items, index):
        array = CircularArray(size=size)
        each(array.append, items)

        with raises(IndexOutOfBoundError):
            array[index]


    @pytest.mark.parametrize('size, items', [
        (2, [1, 2]),
        (3, [None, False, 'test']),
        (50, [i for i in range(50)]),
        (500, [i for i in range(200)]),
    ])
    def test_clone(self, size, items):
        array = CircularArray(size=size)
        each(array.append, items)

        assert array.to_list() == items


    def test_append(self):
        array = CircularArray(size=6)

        array.append(1)
        assert array[0] == 1

        obj = object
        array.append(obj)
        assert array[1] == obj

        array.append('string')
        assert array[2] == 'string'

        array.append(3.1416)
        assert array[3] == 3.1416

        array.append(False)
        assert array[4] == False

        array.append(None)
        assert array[5] is None


    def test_append_raises_error(self):
        array = CircularArray(size=2)

        array.append(1)
        array.append(2)

        with raises(SizeLimitExceededError):
            array.append(3)


    def test_get(self):
        array = CircularArray(size=3)

        array.append(1)
        array.append(5)
        array.append(10)

        assert array.get(0) == 1
        assert array.get(1) == 5
        assert array.get(2) == 10


    @pytest.mark.parametrize('size, items, index', [
        (2, [1, None], 3),
        (3, [10], 1),
        (100, [i for i in range(50)], 92),
    ])
    def test_get_raises_error(self, size, items, index):
        array = CircularArray(size=size)
        each(array.append, items)

        with raises(IndexOutOfBoundError):
            array.get(index)


    def test_rotate_right_once(self):
        items = [1, 2, 3]
        array = CircularArray(size=3)
        each(array.append, items)

        array.rotate_right_once()
        assert array.to_list() == [3, 1, 2]

        array.rotate_right_once()
        assert array.to_list() == [2, 3, 1]

        array.rotate_right_once()
        assert array.to_list() == [1, 2, 3]


    def test_rotate_left_once(self):
        items = [1, 2, 3]
        array = CircularArray(size=3)
        each(array.append, items)

        array.rotate_left_once()
        assert array.to_list() == [2, 3, 1]

        array.rotate_left_once()
        assert array.to_list() == [3, 1, 2]

        array.rotate_left_once()
        assert array.to_list() == [1, 2, 3]


    @pytest.mark.parametrize('size, items, number_of_rotation, final_array', [
        (5, [1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        (1, ['test'], 2, ['test']),
        (0, [], 10, []),
        (5, [1, True, 'string', 3.1416, None], 3, ['string', 3.1416, None, 1, True]),
    ])
    def test_multiple_right_rotation(self, size, items, number_of_rotation, final_array):
        array = CircularArray(size=size)
        each(array.append, items)

        for _ in range(number_of_rotation):
            array.rotate_right_once()

        assert array.to_list() == final_array


    @pytest.mark.parametrize('size, items, number_of_rotation, final_array', [
        (5, [1, 2, 3, 4, 5], 3, [4, 5, 1, 2, 3]),
        (1, ['test'], 2, ['test']),
        (0, [], 10, []),
        (5, [1, True, 'string', 3.1416, None], 3, [3.1416, None, 1, True, 'string']),
    ])
    def test_multiple_right_rotation(self, size, items, number_of_rotation, final_array):
        array = CircularArray(size=size)
        each(array.append, items)

        for _ in range(number_of_rotation):
            array.rotate_left_once()

        assert array.to_list() == final_array
