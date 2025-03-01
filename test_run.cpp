#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
#include "codefile.cpp"

TEST_CASE("is_prime: Basic prime numbers") {
    REQUIRE(is_prime(2));
    REQUIRE(is_prime(3));
    REQUIRE(is_prime(5));
    REQUIRE(is_prime(7));
    REQUIRE(is_prime(11));
    REQUIRE(is_prime(13));
    REQUIRE(is_prime(17));
    REQUIRE(is_prime(19));
    REQUIRE(is_prime(23));
    REQUIRE(is_prime(29));
}

TEST_CASE("is_prime: Basic composite numbers") {
    REQUIRE_FALSE(is_prime(1));
    REQUIRE_FALSE(is_prime(4));
    REQUIRE_FALSE(is_prime(6));
    REQUIRE_FALSE(is_prime(8));
    REQUIRE_FALSE(is_prime(9));
    REQUIRE_FALSE(is_prime(10));
    REQUIRE_FALSE(is_prime(12));
    REQUIRE_FALSE(is_prime(14));
    REQUIRE_FALSE(is_prime(15));
    REQUIRE_FALSE(is_prime(16));
}

TEST_CASE("is_prime: Edge cases") {
    REQUIRE_FALSE(is_prime(0));
    REQUIRE_FALSE(is_prime(-1));
    REQUIRE_FALSE(is_prime(-2));
}

TEST_CASE("is_square_root: Basic square roots") {
    REQUIRE(is_square_root(0, 0));
    REQUIRE(is_square_root(1, 1));
    REQUIRE(is_square_root(2, 4));
    REQUIRE(is_square_root(3, 9));
    REQUIRE(is_square_root(4, 16));
    REQUIRE(is_square_root(5, 25));
}


TEST_CASE("is_square_root: Non-square roots") {
    REQUIRE_FALSE(is_square_root(2, 5));
    REQUIRE_FALSE(is_square_root(3, 8));
    REQUIRE_FALSE(is_square_root(4, 15));
    REQUIRE_FALSE(is_square_root(5, 26));
}

TEST_CASE("is_square_root: Edge cases") {
    REQUIRE_FALSE(is_square_root(-1, 1));
    REQUIRE_FALSE(is_square_root(1, -1));
    REQUIRE_FALSE(is_square_root(-1, -1));
    REQUIRE_FALSE(is_square_root(0, -1));
    REQUIRE_FALSE(is_square_root(-1, 0));

}