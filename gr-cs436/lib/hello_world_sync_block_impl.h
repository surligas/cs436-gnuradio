/*
 * hello_world_sync_block_impl.h
 *
 *  Created on: Nov 13, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_LIB_HELLO_WORLD_SYNC_BLOCK_IMPL_H_
#define GR_CS436_LIB_HELLO_WORLD_SYNC_BLOCK_IMPL_H_

#include <gnuradio/cs436/hello_world_sync_block.h>

namespace gr
{
namespace cs436
{

class hello_world_sync_block_impl : public hello_world_sync_block
{
public:
	hello_world_sync_block_impl(const float real_mult, const float imag_mult);

	/* The work() method that each synchronous block should implement */
	int
	work(int noutput_items, gr_vector_const_void_star &input_items,
	     gr_vector_void_star &output_items);

	void
	set_real_multiplier(const float mult);

	void
	set_imag_multiplier(const float mult);

/* Declare the appropriate private members of the class */
private:
	float		d_real_mult;
	float		d_imag_mult;
};

} /* namespace cs436 */
} /* namespace gr */

#endif /* GR_CS436_LIB_HELLO_WORLD_SYNC_BLOCK_IMPL_H_ */
