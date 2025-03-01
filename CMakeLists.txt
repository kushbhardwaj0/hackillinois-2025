cmake_minimum_required(VERSION 3.14)
project(GlitchGuardTests LANGUAGES CXX)

include(FetchContent)

FetchContent_Declare(
  catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.5.0
)

FetchContent_MakeAvailable(catch2)

add_executable(tests test_run.cpp)
target_compile_features(tests PUBLIC cxx_std_17)
target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
