########################################################################
# Setup swig generation
########################################################################
include(GrPython)
include(GrSwig)

set(GR_SWIG_INCLUDE_DIRS
    ${GR_CS436_INCLUDE_DIRS}
    ${GR_FILTER_INCLUDE_DIRS}
    ${GNURADIO_RUNTIME_SWIG_INCLUDE_DIRS}
    ${Boost_INCLUDE_DIRS}
)

if(ENABLE_GR_CTRLPORT)
  list(APPEND GR_SWIG_FLAGS "-DGR_CTRLPORT")
endif(ENABLE_GR_CTRLPORT)

set(GR_SWIG_DOC_FILE ${CMAKE_CURRENT_BINARY_DIR}/cs436_swig_doc.i)
set(GR_SWIG_DOC_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../include/gnuradio/cs436)
set(GR_SWIG_DOCS_TARGET_DEPS runtime_swig_swig_doc)
set(GR_SWIG_LIBRARIES gnuradio-cs436)

GR_SWIG_MAKE(cs436_swig cs436_swig.i)

GR_SWIG_INSTALL(
    TARGETS cs436_swig
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/cs436
    COMPONENT "cs436_python"
)

install(
    FILES
    cs436_swig.i
    ${CMAKE_CURRENT_BINARY_DIR}/cs436_swig_doc.i
    DESTINATION ${GR_INCLUDE_DIR}/gnuradio/swig
    COMPONENT "cs436_swig"
)