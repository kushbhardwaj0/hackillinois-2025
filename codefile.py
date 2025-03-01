import math

def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def reverse_string(s):
    """Returns the reverse of a given string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def find_max(lst):
    """Returns the maximum value in a list."""
    if len(lst) == 0:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def sum_of_squares(n):
    """Returns the sum of squares of numbers from 1 to n."""
    return sum([i*i for i in range(1, n+1)])

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    return s == s[::-1]

def merge_sorted_lists(lst1, lst2):
    """Merges two sorted lists into one sorted list."""
    merged = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

def word_count(s):
    """Returns a dictionary with the count of each word in a string."""
    words = s.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

def get_even_numbers(lst):
    """Returns a list of even numbers from the given list."""
    return [num for num in lst if num % 2 == 0]

def sum_digits(n):
    """Returns the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def gcd(a, b):
    """Computes the Greatest Common Divisor (GCD) of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Computes the Least Common Multiple (LCM) of two numbers."""
    return abs(a * b) // gcd(a, b)

def rotate_list(lst, k):
    """Rotates a list to the right by k positions."""
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

