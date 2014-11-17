#define CS436_API

%include "gnuradio.i"

//load generated python docstrings
%include "cs436_swig_doc.i"

%{
#include "gnuradio/cs436/hello_world_sync_block.h"
%}

%include "gnuradio/cs436/hello_world_sync_block.h"

GR_SWIG_BLOCK_MAGIC2(cs436, hello_world_sync_block);