/*
 * evm_impl.h
 *
 *  Created on: Nov 17, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_LIB_EVM_IMPL_H_
#define GR_CS436_LIB_EVM_IMPL_H_

#include <gnuradio/cs436/evm.h>

namespace gr
{
namespace cs436
{

class evm_impl : public evm
{
public:
	evm_impl(const size_t vlen,
	         const constellation_t constellation,
	         const float sampling_rate);

	int
	work(int noutput_items, gr_vector_const_void_star &input_items,
	     gr_vector_void_star &output_items);

private:
	const size_t 		d_vlen;
	const constellation_t	d_constellation;
	const float		d_sampling_rate;
};

} /* namespace cs436 */
} /* namespace gr */

#endif /* GR_CS436_LIB_EVM_IMPL_H_ */
