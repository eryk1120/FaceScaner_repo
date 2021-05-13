cmake_minimum_required(VERSION 3.5)

# Find python and Boost - both are required dependencies
find_package(PythonLibs 2.7 REQUIRED)
find_package(Boost COMPONENTS python REQUIRED)

find_path(LIBUSB_INCLUDE_DIR NAMES libusb.h )
find_library(LIBUSB_LIBRARY NAMES libusb-1.0.so)


# Without this, any build libraries automatically have names "lib{x}.so"
set(CMAKE_SHARED_MODULE_PREFIX "")

# Add a shared module - modules are intended to be imported at runtime.
# - This is where you add the source files

add_library(fotosfera MODULE fotosfera.cpp usb2lin06Controler.cpp usb2linException.cpp statusReport.cpp)


# Set up the libraries and header search paths for this target
target_link_libraries(fotosfera ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ${LIBUSB_LIBRARY} )
target_include_directories(fotosfera PRIVATE ${PYTHON_INCLUDE_DIRS} ${LIBUSB_INCLUDE_DIR})