import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import my_lib


class TestFibonacci:

    def test_fibonacci_on_five(self):
        assert my_lib.fibonacci(5) == [0, 1, 1, 2, 3]

    def test_fibonacci_on_zero(self):
        assert my_lib.fibonacci(0) == []

    def test_fibonacci_on_one(self):
        assert my_lib.fibonacci(1) == [0]

    def test_fibonacci_on_negative(self):
        with pytest.raises(ValueError):
            my_lib.fibonacci(-1)

    def test_fibonacci_on_wrong_type(self):
        with pytest.raises(TypeError):
            my_lib.fibonacci("5")