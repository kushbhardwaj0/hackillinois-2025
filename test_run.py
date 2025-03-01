from codefile import *
import pytest

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(100) == False

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(-1) == 0

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("madam") == "madam"
    assert reverse_string("12345") == "54321"

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
    assert count_vowels("12345") == 0
    assert count_vowels("The quick brown fox") == 5

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(5) == 120


def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([-1, -2, -3]) == -1
    assert find_max([]) == None
    assert find_max([1]) == 1


def test_sum_of_squares():
    assert sum_of_squares(0) == 0
    assert sum_of_squares(1) == 1
    assert sum_of_squares(2) == 5
    assert sum_of_squares(3) == 14
    assert sum_of_squares(5) == 55

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a") == True
    assert is_palindrome("") == True

def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([1], []) == [1]
    assert merge_sorted_lists([], [1]) == [1]
    assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]

def test_word_count():
    assert word_count("the quick brown fox the lazy dog") == {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'lazy': 1, 'dog': 1}
    assert word_count("") == {}
    assert word_count("hello hello hello") == {'hello': 3}

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([]) == []
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]

def test_sum_digits():
    assert sum_digits(123) == 6
    assert sum_digits(0) == 0
    assert sum_digits(999) == 27
    assert sum_digits(100) == 1

def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(1, 1) == 1

def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(0, 5) == 0
    assert lcm(2,3) == 6

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate_list([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
    assert rotate_list([], 2) == []


if __name__ == "__main__":
    pytest.main()