# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/PythonModule

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/PythonModule/Build

# Include any dependencies generated for this target.
include CMakeFiles/fotosfera.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/fotosfera.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fotosfera.dir/flags.make

CMakeFiles/fotosfera.dir/fotosfera.cpp.o: CMakeFiles/fotosfera.dir/flags.make
CMakeFiles/fotosfera.dir/fotosfera.cpp.o: ../fotosfera.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/PythonModule/Build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fotosfera.dir/fotosfera.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fotosfera.dir/fotosfera.cpp.o -c /home/pi/PythonModule/fotosfera.cpp

CMakeFiles/fotosfera.dir/fotosfera.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fotosfera.dir/fotosfera.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/PythonModule/fotosfera.cpp > CMakeFiles/fotosfera.dir/fotosfera.cpp.i

CMakeFiles/fotosfera.dir/fotosfera.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fotosfera.dir/fotosfera.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/PythonModule/fotosfera.cpp -o CMakeFiles/fotosfera.dir/fotosfera.cpp.s

CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o: CMakeFiles/fotosfera.dir/flags.make
CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o: ../usb2lin06Controler.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/PythonModule/Build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o -c /home/pi/PythonModule/usb2lin06Controler.cpp

CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/PythonModule/usb2lin06Controler.cpp > CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.i

CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/PythonModule/usb2lin06Controler.cpp -o CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.s

CMakeFiles/fotosfera.dir/usb2linException.cpp.o: CMakeFiles/fotosfera.dir/flags.make
CMakeFiles/fotosfera.dir/usb2linException.cpp.o: ../usb2linException.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/PythonModule/Build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/fotosfera.dir/usb2linException.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fotosfera.dir/usb2linException.cpp.o -c /home/pi/PythonModule/usb2linException.cpp

CMakeFiles/fotosfera.dir/usb2linException.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fotosfera.dir/usb2linException.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/PythonModule/usb2linException.cpp > CMakeFiles/fotosfera.dir/usb2linException.cpp.i

CMakeFiles/fotosfera.dir/usb2linException.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fotosfera.dir/usb2linException.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/PythonModule/usb2linException.cpp -o CMakeFiles/fotosfera.dir/usb2linException.cpp.s

CMakeFiles/fotosfera.dir/statusReport.cpp.o: CMakeFiles/fotosfera.dir/flags.make
CMakeFiles/fotosfera.dir/statusReport.cpp.o: ../statusReport.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/PythonModule/Build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/fotosfera.dir/statusReport.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fotosfera.dir/statusReport.cpp.o -c /home/pi/PythonModule/statusReport.cpp

CMakeFiles/fotosfera.dir/statusReport.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fotosfera.dir/statusReport.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/PythonModule/statusReport.cpp > CMakeFiles/fotosfera.dir/statusReport.cpp.i

CMakeFiles/fotosfera.dir/statusReport.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fotosfera.dir/statusReport.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/PythonModule/statusReport.cpp -o CMakeFiles/fotosfera.dir/statusReport.cpp.s

# Object files for target fotosfera
fotosfera_OBJECTS = \
"CMakeFiles/fotosfera.dir/fotosfera.cpp.o" \
"CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o" \
"CMakeFiles/fotosfera.dir/usb2linException.cpp.o" \
"CMakeFiles/fotosfera.dir/statusReport.cpp.o"

# External object files for target fotosfera
fotosfera_EXTERNAL_OBJECTS =

fotosfera.so: CMakeFiles/fotosfera.dir/fotosfera.cpp.o
fotosfera.so: CMakeFiles/fotosfera.dir/usb2lin06Controler.cpp.o
fotosfera.so: CMakeFiles/fotosfera.dir/usb2linException.cpp.o
fotosfera.so: CMakeFiles/fotosfera.dir/statusReport.cpp.o
fotosfera.so: CMakeFiles/fotosfera.dir/build.make
fotosfera.so: /usr/lib/arm-linux-gnueabihf/libboost_python.so
fotosfera.so: /usr/lib/arm-linux-gnueabihf/libpython2.7.so
fotosfera.so: /usr/lib/arm-linux-gnueabihf/libusb-1.0.so
fotosfera.so: CMakeFiles/fotosfera.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/PythonModule/Build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX shared module fotosfera.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fotosfera.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fotosfera.dir/build: fotosfera.so

.PHONY : CMakeFiles/fotosfera.dir/build

CMakeFiles/fotosfera.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fotosfera.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fotosfera.dir/clean

CMakeFiles/fotosfera.dir/depend:
	cd /home/pi/PythonModule/Build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/PythonModule /home/pi/PythonModule /home/pi/PythonModule/Build /home/pi/PythonModule/Build /home/pi/PythonModule/Build/CMakeFiles/fotosfera.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fotosfera.dir/depend

