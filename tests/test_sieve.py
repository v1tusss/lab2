import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
import my_lib


class TestSieveOfEratosthenes:

    def test_sieve_on_ten(self):
        assert my_lib.sieve_of_eratosthenes(10) == [2, 3, 5, 7]

    def test_sieve_on_zero(self):
        assert my_lib.sieve_of_eratosthenes(0) == []

    def test_sieve_on_one(self):
        assert my_lib.sieve_of_eratosthenes(1) == []

    def test_sieve_on_two(self):
        assert my_lib.sieve_of_eratosthenes(2) == [2]

    def test_sieve_on_negative(self):
        with pytest.raises(ValueError):
            my_lib.sieve_of_eratosthenes(-10)

    def test_sieve_on_wrong_type(self):
        with pytest.raises(TypeError):
            my_lib.sieve_of_eratosthenes(5.5)