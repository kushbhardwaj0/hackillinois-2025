#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int n) {
    if (n < 2) return false;        // 0 and 1 are not prime
    if (n == 2 || n == 3) return true; // 2 and 3 are prime numbers
    if (n % 2 == 0 || n % 3 == 0) return false; // Eliminate even numbers and multiples of 3

    for (int i = 5; i * i <= n; i += 6) { // Check only numbers of the form 6k ± 1
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}

bool is_square_root(int root, int num) {
    if (root < 0 || num < 0) return false; // Negative numbers don't have real square roots
    return root * root == num;
}