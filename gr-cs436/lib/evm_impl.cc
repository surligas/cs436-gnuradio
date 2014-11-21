/*
 * evm_impl.cc
 *
 *  Created on: Nov 17, 2014
 *      Author: surligas
 */

#include "evm_impl.h"
#include <gnuradio/io_signature.h>

namespace gr
{
namespace cs436
{

/**
 * Crates the EVM block.
 *
 * Input 0 (gr_complex): The reference signal
 * Input 1 (gr_complex): The received signal
 *
 * Output 0 (float): The EVM of each input item of the received signal
 * Output 1 (float): The BER
 *
 * @param vlen how many complex numbers each input item is
 * @param constellation the constellation of the input items
 * @param sampling_rate the sampling rate of the system. As we can
 * not measure time very accurate, in order to measure the BER with
 * the sampling rate we now exactly how many complex numbers are
 * transmitted within a second.
 * @return shared pointer of the EVM block
 */
evm::sptr
evm::make(const size_t vlen, const int constellation, const float sampling_rate)
{
	return gnuradio::get_initial_sptr(new evm_impl(vlen,
	                                               (const constellation_t) constellation,
	                                               sampling_rate));
}

/**
 * The constructor of the EVM block
 *
 * @param vlen how many complex numbers each input item is
 * @param constellation the constellation of the input items
 * @param sampling_rate the sampling rate of the system. As we can
 * not measure time very accurate, in order to measure the BER with
 * the sampling rate we now exactly how many complex numbers are
 * transmitted within a second.
 *
 */
evm_impl::evm_impl(const size_t vlen, const constellation_t constellation,
                   const float sampling_rate)
: sync_block("evm",
             /* FIXME: Make the proper changes at the input signatures */
             io_signature::make(0, 0, 0),
             /* FIXME: Make the proper changes at the output signatures */
             io_signature::make(0, 0, 0)),
             d_vlen(vlen),
             d_constellation(constellation),
             d_sampling_rate(sampling_rate)
{
}

int
evm_impl::work(int noutput_items, gr_vector_const_void_star& input_items,
               gr_vector_void_star& output_items)
{
	/* TODO: Write your code here! */
	return noutput_items;
}

} /* namespace cs436 */
} /* namespace gr */
