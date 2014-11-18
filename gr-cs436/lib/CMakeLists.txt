########################################################################
# Setup the include and linker paths
########################################################################
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_BINARY_DIR}
    ${GR_CS436_INCLUDE_DIRS}
    ${GR_BLOCKS_INCLUDE_DIRS}
    ${GR_FILTER_INCLUDE_DIRS}
    ${GR_ANALOG_INCLUDE_DIRS}
    ${GNURADIO_RUNTIME_INCLUDE_DIRS}
    ${Boost_INCLUDE_DIRS}
)

link_directories(${Boost_LIBRARY_DIRS})

if(ENABLE_GR_CTRLPORT)
  ADD_DEFINITIONS(-DGR_CTRLPORT)
endif(ENABLE_GR_CTRLPORT)

########################################################################
# Setup library
########################################################################
list(APPEND cs436_sources
  evm_impl.cc
  hello_world_sync_block_impl.cc
)

list(APPEND cs436_libs
    volk
    gnuradio-runtime
    gnuradio-filter
    gnuradio-analog
    gnuradio-blocks
    ${Boost_LIBRARIES}
)

add_library(gnuradio-cs436 SHARED ${cs436_sources})
target_link_libraries(gnuradio-cs436 ${cs436_libs})
GR_LIBRARY_FOO(gnuradio-cs436 RUNTIME_COMPONENT "cs436_runtime" DEVEL_COMPONENT "cs436_devel")
add_dependencies(gnuradio-cs436
  cs436_generated_includes cs436_generated_swigs
  gnuradio-runtime gnuradio-filter gnuradio-analog gnuradio-blocks)