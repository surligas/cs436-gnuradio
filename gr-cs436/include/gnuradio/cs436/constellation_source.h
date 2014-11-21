/*
 * constellation_source.h
 *
 *  Created on: Nov 21, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_SOURCE_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_SOURCE_H_

#include <gnuradio/cs436/api.h>
#include <gnuradio/sync_block.h>
#include <gnuradio/cs436/constellation.h>

namespace gr {

namespace cs436 {

class CS436_API constellation_source : virtual public sync_block
{
public:
	typedef boost::shared_ptr<constellation_source> sptr;

	static sptr
	make(const size_t vlen, int modulation);

};

}  // namespace cs436

}  // namespace gr

#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_SOURCE_H_ */
