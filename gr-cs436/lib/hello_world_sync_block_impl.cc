/*
 * hello_world_sync_block_impl.cc
 *
 *  Created on: Nov 13, 2014
 *      Author: surligas
 */

#include "hello_world_sync_block_impl.h"

/* This is required in order to declare input and output ports */
#include <gnuradio/io_signature.h>
#include <complex>
namespace gr
{
namespace cs436
{

/**
 * This is the way that a shared pointer of the block instance can be retrieved
 * @param real_mult multiply with this number the real part
 * @param imag_mult multiply with this number the imaginary part
 */
hello_world_sync_block::sptr
hello_world_sync_block::make(const float real_mult,
                             const float imag_mult)
{
	return gnuradio::get_initial_sptr(new hello_world_sync_block_impl(real_mult,
	                                                                  imag_mult));
}

/**
 * The "local" constructor of the block
 * @param real_mult multiply with this number the real part
 * @param imag_mult multiply with this number the imaginary part
 */
hello_world_sync_block_impl::hello_world_sync_block_impl(const float real_mult,
                                                         const float imag_mult)
: sync_block("hello_world_sync_block",
             io_signature::make(1, 1, sizeof(gr_complex)),
             io_signature::make(2, 2, sizeof(float))),
             d_real_mult(real_mult),
             d_imag_mult(imag_mult)
{
}

int
hello_world_sync_block_impl::work(int noutput_items,
                                  gr_vector_const_void_star& input_items,
                                  gr_vector_void_star& output_items)
{
	int i;

	/*
	 * Get the input and output ports.
	 * Each port is a buffer with the data type and size that
	 * were declared in the block constructor.
	 *
	 * For example this block has 1 complex input port and
	 * two output float ports.
	 */
	const gr_complex *input = (const gr_complex *) input_items[0];
	float *out_real = (float *) output_items[0];
	float *out_imag = (float *) output_items[1];

	for(i = 0; i < noutput_items; i++) {
		out_real[i] = std::real(input[i]) * d_real_mult;
		out_imag[i] = std::imag(input[i]) * d_imag_mult;
	}

	/*
	 * Return how many output items we produced.
	 * As this block is a synchronous block, it also
	 * tells the scheduler how many items we consumed.
	 */
	return noutput_items;
}

/**
 * Set the real part multiplier
 * @param mult multiply with this number the real part
 */
void
hello_world_sync_block_impl::set_real_multiplier(const float mult)
{
	d_real_mult = mult;
}

/**
 * Set the imaginary part multiplier
 * @param mult multiply with this number the imaginary part
 */
void
hello_world_sync_block_impl::set_imag_multiplier(const float mult)
{
	d_imag_mult = mult;
}

} /* namespace cs436 */
} /* namespace gr */
