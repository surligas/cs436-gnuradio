/*
 * constellation_source_impl.cc
 *
 *  Created on: Nov 21, 2014
 *      Author: surligas
 */

#include "constellation_source_impl.h"
#include <gnuradio/io_signature.h>
#include <stdlib.h>

namespace gr
{
namespace cs436
{

constellation_source::sptr
constellation_source::make(const size_t vlen,
	                   int modulation)
{
	return gnuradio::get_initial_sptr(new constellation_source_impl(vlen,
	                                                                (constellation_t)modulation));
}

constellation_source_impl::constellation_source_impl(const size_t vlen,
                   	                             constellation_t modulation)
: sync_block("constellation_source",
             io_signature::make(0,0,0),
             io_signature::make(1, 1, vlen * sizeof(gr_complex))),
             d_vlen(vlen),
             d_constellation(modulation)
{
	switch (d_constellation)
		{
	case BPSK:
		d_constellation_points = _bpsk_points;
		break;
	case QPSK:
		d_constellation_points = _qpsk_points;
		break;
	case QAM16:
		d_constellation_points = _qam16_points;
		break;
	default:
		throw std::invalid_argument("Wrong modulation scheme");
		}
}

int
constellation_source_impl::work(int noutput_items,
                                gr_vector_const_void_star& input_items,
                                gr_vector_void_star& output_items)
{
	int 		i;
	size_t		j;
	gr_complex *out = (gr_complex *)output_items[0];

	for(i = 0; i < noutput_items; i++){
		for(j = 0; j < d_vlen; j++){
			out[i * d_vlen + j] =
				d_constellation_points[random() % d_constellation];
		}
	}
	return noutput_items;
}

} /* namespace cs436 */
} /* namespace gr */
