import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import my_lib

class TestBubbleSort:

    def test_bubble_sort_on_unsorted_list(self):
        assert my_lib.bubble_sort([3, 1, 2]) == [1, 2, 3]

    def test_bubble_sort_on_sorted_list(self):
        assert my_lib.bubble_sort([1, 2, 3]) == [1, 2, 3]

    def test_bubble_sort_on_equal_elements(self):
        assert my_lib.bubble_sort([5, 5, 5]) == [5, 5, 5]

    def test_bubble_sort_on_empty_list(self):
        assert my_lib.bubble_sort([]) == []

    def test_bubble_sort_on_wrong_type(self):
        with pytest.raises(TypeError):
            my_lib.bubble_sort("123")

    def test_bubble_sort_on_invalid_element(self):
        with pytest.raises(TypeError):
            my_lib.bubble_sort([1, "a", 3])