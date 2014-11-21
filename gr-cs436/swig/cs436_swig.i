#define CS436_API

%include "gnuradio.i"

//load generated python docstrings
%include "cs436_swig_doc.i"

%{
#include "gnuradio/cs436/hello_world_sync_block.h"
#include "gnuradio/cs436/evm.h"
#include "gnuradio/cs436/constellation_source.h"
%}

%include "gnuradio/cs436/hello_world_sync_block.h"
%include "gnuradio/cs436/evm.h"
%include "gnuradio/cs436/constellation_source.h"

enum modulation_t
{
	BPSK = 2, QPSK = 4, QAM16 = 16
};

GR_SWIG_BLOCK_MAGIC2(cs436, hello_world_sync_block);
GR_SWIG_BLOCK_MAGIC2(cs436, evm);
GR_SWIG_BLOCK_MAGIC2(cs436, constellation_source)