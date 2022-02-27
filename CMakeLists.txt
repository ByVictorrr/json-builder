cmake_minimum_required (VERSION 2.6)
project (jsonbuilder)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set (CMAKE_C_FLAGS "-std=c89 -ansi -pedantic -Wall ${CMAKE_C_FLAGS}")
set (SOURCES ${SOURCES} json-builder.c)

add_library (${PROJECT_NAME} ${SOURCES})

set_target_properties (${PROJECT_NAME} PROPERTIES VERSION 0.1.0
                                              SOVERSION 0.1)

message("c = ${CONAN_LIBS}")
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

install (TARGETS ${PROJECT_NAME} DESTINATION lib)
install (FILES json-builder.h DESTINATION include/json-builder)


