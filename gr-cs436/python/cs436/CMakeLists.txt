########################################################################
# Setup python install
########################################################################
include(GrPython)

GR_PYTHON_INSTALL(
    FILES
    __init__.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/cs436
    COMPONENT "cs436_python"
)