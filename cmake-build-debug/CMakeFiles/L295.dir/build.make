# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/liheng/ClionProjects/clion_p1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/liheng/ClionProjects/clion_p1/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/L295.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/L295.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/L295.dir/flags.make

CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o: CMakeFiles/L295.dir/flags.make
CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o: ../c6_stack_queue/L295-m.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/liheng/ClionProjects/clion_p1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o -c /Users/liheng/ClionProjects/clion_p1/c6_stack_queue/L295-m.cpp

CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/liheng/ClionProjects/clion_p1/c6_stack_queue/L295-m.cpp > CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.i

CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/liheng/ClionProjects/clion_p1/c6_stack_queue/L295-m.cpp -o CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.s

# Object files for target L295
L295_OBJECTS = \
"CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o"

# External object files for target L295
L295_EXTERNAL_OBJECTS =

L295: CMakeFiles/L295.dir/c6_stack_queue/L295-m.cpp.o
L295: CMakeFiles/L295.dir/build.make
L295: CMakeFiles/L295.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/liheng/ClionProjects/clion_p1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable L295"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/L295.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/L295.dir/build: L295

.PHONY : CMakeFiles/L295.dir/build

CMakeFiles/L295.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/L295.dir/cmake_clean.cmake
.PHONY : CMakeFiles/L295.dir/clean

CMakeFiles/L295.dir/depend:
	cd /Users/liheng/ClionProjects/clion_p1/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/liheng/ClionProjects/clion_p1 /Users/liheng/ClionProjects/clion_p1 /Users/liheng/ClionProjects/clion_p1/cmake-build-debug /Users/liheng/ClionProjects/clion_p1/cmake-build-debug /Users/liheng/ClionProjects/clion_p1/cmake-build-debug/CMakeFiles/L295.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/L295.dir/depend

