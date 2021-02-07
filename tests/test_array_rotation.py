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

        assert array.clone() == items


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
        assert array[5] == None


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
        assert array.clone() == [3, 1, 2]

        array.rotate_right_once()
        assert array.clone() == [2, 3, 1]

        array.rotate_right_once()
        assert array.clone() == [1, 2, 3]


    def test_rotate_left_once(self):
        items = [1, 2, 3]
        array = CircularArray(size=3)

        each(array.append, items)

        array.rotate_left_once()
        assert array.clone() == [2, 3, 1]

        array.rotate_left_once()
        assert array.clone() == [3, 1, 2]

        array.rotate_left_once()
        assert array.clone() == [1, 2, 3]
