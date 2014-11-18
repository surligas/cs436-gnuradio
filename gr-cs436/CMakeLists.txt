########################################################################
# Setup dependencies
########################################################################
include(GrBoost)

########################################################################
# Register component
########################################################################
include(GrComponent)

GR_REGISTER_COMPONENT("gr-cs436" ENABLE_GR_CS436
    ENABLE_VOLK
    Boost_FOUND
    ENABLE_GNURADIO_RUNTIME
    ENABLE_GR_BLOCKS
    ENABLE_GR_FFT
    ENABLE_GR_FILTER
    ENABLE_GR_ANALOG
)

GR_SET_GLOBAL(GR_CS436_INCLUDE_DIRS
    ${CMAKE_CURRENT_SOURCE_DIR}/lib
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

########################################################################
# Begin conditional configuration
########################################################################
if(ENABLE_GR_CS436)

########################################################################
# Setup CPack components
########################################################################
include(GrPackage)
CPACK_SET(CPACK_COMPONENT_GROUP_CHANNELS_DESCRIPTION "GNU Radio Blocks for the CS-436 lesson of www.csd.uoc.gr")

CPACK_COMPONENT("cs436_runtime"
    GROUP        "CS-436 Blocks"
    DISPLAY_NAME "Runtime"
    DESCRIPTION  "Runtime"
    DEPENDS      "runtime_runtime"
)

CPACK_COMPONENT("cs436_devel"
    GROUP        "CS-436 Blocks"
    DISPLAY_NAME "Development"
    DESCRIPTION  "C++ headers, package config, import libraries"
    DEPENDS      "runtime_devel"
)

CPACK_COMPONENT("cs436_python"
    GROUP        "CS-436 Blocks"
    DISPLAY_NAME "Python"
    DESCRIPTION  "Python modules for runtime; GRC xml files"
    DEPENDS      "runtime_python;cs436_runtime"
)

CPACK_COMPONENT("cs436_swig"
    GROUP        "CS-436 Blocks"
    DISPLAY_NAME "SWIG"
    DESCRIPTION  "SWIG development .i files"
    DEPENDS      "runtime_swig;cs436_python;cs436_devel"
)

add_subdirectory(include/gnuradio/cs436)
add_subdirectory(lib)
if(ENABLE_PYTHON)
add_subdirectory(python/cs436)
add_subdirectory(grc)
add_subdirectory(swig)
endif(ENABLE_PYTHON)

########################################################################
# Create Pkg Config File
########################################################################
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/gnuradio-cs436.pc.in
    ${CMAKE_CURRENT_BINARY_DIR}/gnuradio-cs436.pc
@ONLY)

install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/gnuradio-cs436.pc
    DESTINATION ${GR_LIBRARY_DIR}/pkgconfig
    COMPONENT "cs436_devel"
)

endif(ENABLE_GR_CS436)