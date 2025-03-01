def factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

