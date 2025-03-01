#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
#include "codefile.cpp"
#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>

TEST_CASE("Factorial of zero", "[factorial]") {
    REQUIRE(factorial(0) == 1);
}

TEST_CASE("Factorial of one", "[factorial]") {
    REQUIRE(factorial(1) == 1);
}

TEST_CASE("Factorial of positive number", "[factorial]") {
    REQUIRE(factorial(5) == 120);
}

TEST_CASE("Factorial of large positive number", "[factorial]") {
    REQUIRE(factorial(10) == 3628800);
}

TEST_CASE("Factorial of negative number", "[factorial]") {
    REQUIRE_THROWS_AS(factorial(-1), std::invalid_argument);
}

