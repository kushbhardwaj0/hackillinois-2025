# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.27.6/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.27.6/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kushb/Downloads/hackillinois-2025

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kushb/Downloads/hackillinois-2025/build

# Include any dependencies generated for this target.
include _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/compiler_depend.make

# Include the progress variables for this target.
include _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/progress.make

# Include the compile flags for this target's objects.
include _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/flags.make

_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o: _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/flags.make
_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o: _deps/catch2-src/src/catch2/internal/catch_main.cpp
_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o: _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kushb/Downloads/hackillinois-2025/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o"
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o -MF CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o.d -o CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o -c /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-src/src/catch2/internal/catch_main.cpp

_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.i"
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-src/src/catch2/internal/catch_main.cpp > CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.i

_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.s"
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-src/src/catch2/internal/catch_main.cpp -o CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.s

# Object files for target Catch2WithMain
Catch2WithMain_OBJECTS = \
"CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o"

# External object files for target Catch2WithMain
Catch2WithMain_EXTERNAL_OBJECTS =

_deps/catch2-build/src/libCatch2Main.a: _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/catch2/internal/catch_main.cpp.o
_deps/catch2-build/src/libCatch2Main.a: _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/build.make
_deps/catch2-build/src/libCatch2Main.a: _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/kushb/Downloads/hackillinois-2025/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libCatch2Main.a"
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && $(CMAKE_COMMAND) -P CMakeFiles/Catch2WithMain.dir/cmake_clean_target.cmake
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Catch2WithMain.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/build: _deps/catch2-build/src/libCatch2Main.a
.PHONY : _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/build

_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/clean:
	cd /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src && $(CMAKE_COMMAND) -P CMakeFiles/Catch2WithMain.dir/cmake_clean.cmake
.PHONY : _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/clean

_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/depend:
	cd /Users/kushb/Downloads/hackillinois-2025/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kushb/Downloads/hackillinois-2025 /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-src/src /Users/kushb/Downloads/hackillinois-2025/build /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src /Users/kushb/Downloads/hackillinois-2025/build/_deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : _deps/catch2-build/src/CMakeFiles/Catch2WithMain.dir/depend

