file(GLOB xml_files "*.xml")
install(FILES ${xml_files}
    DESTINATION ${GRC_BLOCKS_DIR} COMPONENT "cs436_python"
)