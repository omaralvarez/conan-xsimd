# conan-xsimd
    
## Reuse the packages

### Basic setup

    $ conan install xsimd/7.2.3@omaralvarez/public-conan

### Package basic test
    $ conan create . username/bintray-repo
    
## Example usage in a CMake-based project

### Conan and CMake files

* A sample from `conanfile.txt` in the root directory:
```
[requires]
xsimd/7.2.3@omaralvarez/public-conan
...

[generators]
cmake
...
```

* The `CMakeLists.txt` at the root directory:
```cmake
cmake_minimum_required(VERSION 3.8)
project(project_name CXX)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

include(CheckCXXCompilerFlag)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 14)

CHECK_CXX_COMPILER_FLAG("-march=native" COMPILER_SUPPORTS_MARCH_NATIVE)
if(COMPILER_SUPPORTS_MARCH_NATIVE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
endif()

CHECK_CXX_COMPILER_FLAG("-mtune=native" COMPILER_SUPPORTS_MARCH_NATIVE)
if(COMPILER_SUPPORTS_MARCH_NATIVE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mtune=native")
endif()

set(CMAKE_CXX_FLAGS_RELEASE "-O3")

find_package(OpenMP REQUIRED) # Find the package
...
```
* The `CMakeLists.txt` of a dependent target:
```cmake
...
add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS} ${OpenMP_CXX_LIBRARIES})
...
```

### Running Conan and CMake 

* First, add new remote pointing to the repository: 
```
conan remote add omaralvarez https://api.bintray.com/conan/omaralvarez/public-conan
```
* Change directory to the build location and run Conan installation:
```shell
conan install .. -s build_type=Release --build=missing
```
where the `..` points to the project root at the parent directory.
* Run CMake:
```shell
cmake ..
```
