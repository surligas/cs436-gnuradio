/*
 * constellation_source_impl.h
 *
 *  Created on: Nov 21, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_LIB_CONSTELLATION_SOURCE_IMPL_H_
#define GR_CS436_LIB_CONSTELLATION_SOURCE_IMPL_H_

#include <gnuradio/cs436/constellation_source.h>

namespace gr
{
namespace cs436
{

class constellation_source_impl : public constellation_source
{
public:
	constellation_source_impl(const size_t vlen,
	                          constellation_t modulation);

	int
	work(int noutput_items, gr_vector_const_void_star &input_items,
	     gr_vector_void_star &output_items);

private:
	const size_t			d_vlen;
	const constellation_t		d_constellation;
	gr_complex	 		*d_constellation_points;
};

} /* namespace cs436 */
} /* namespace gr */

#endif /* GR_CS436_LIB_CONSTELLATION_SOURCE_IMPL_H_ */
