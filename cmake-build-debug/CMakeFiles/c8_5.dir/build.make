# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.12

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\Program Files\JetBrains\CLion 2018.2.5\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\Program Files\JetBrains\CLion 2018.2.5\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/c8_5.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/c8_5.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/c8_5.dir/flags.make

CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj: CMakeFiles/c8_5.dir/flags.make
CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj: CMakeFiles/c8_5.dir/includes_CXX.rsp
CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj: ../c8_recurrent_backtrack/L79.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj"
	C:\mingw64\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\c8_5.dir\c8_recurrent_backtrack\L79.cpp.obj -c "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\c8_recurrent_backtrack\L79.cpp"

CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.i"
	C:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\c8_recurrent_backtrack\L79.cpp" > CMakeFiles\c8_5.dir\c8_recurrent_backtrack\L79.cpp.i

CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.s"
	C:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\c8_recurrent_backtrack\L79.cpp" -o CMakeFiles\c8_5.dir\c8_recurrent_backtrack\L79.cpp.s

# Object files for target c8_5
c8_5_OBJECTS = \
"CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj"

# External object files for target c8_5
c8_5_EXTERNAL_OBJECTS =

c8_5.exe: CMakeFiles/c8_5.dir/c8_recurrent_backtrack/L79.cpp.obj
c8_5.exe: CMakeFiles/c8_5.dir/build.make
c8_5.exe: CMakeFiles/c8_5.dir/linklibs.rsp
c8_5.exe: CMakeFiles/c8_5.dir/objects1.rsp
c8_5.exe: CMakeFiles/c8_5.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable c8_5.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\c8_5.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/c8_5.dir/build: c8_5.exe

.PHONY : CMakeFiles/c8_5.dir/build

CMakeFiles/c8_5.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\c8_5.dir\cmake_clean.cmake
.PHONY : CMakeFiles/c8_5.dir/clean

CMakeFiles/c8_5.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1" "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1" "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug" "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug" "D:\Program Files\JetBrains\CLion 2018.2.5\Item_Set\clion_p1\cmake-build-debug\CMakeFiles\c8_5.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/c8_5.dir/depend

