cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test test.cpp)
target_link_libraries(test ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME test
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND test)
