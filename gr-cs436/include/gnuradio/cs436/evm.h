/*
 * evm.h
 *
 *  Created on: Nov 17, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_EVM_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_EVM_H_


#include <gnuradio/cs436/api.h>
#include <gnuradio/sync_block.h>
#include <gnuradio/cs436/constellation.h>

namespace gr {

namespace cs436 {

class CS436_API evm : virtual public sync_block
{
public:
	typedef boost::shared_ptr<evm> sptr;

	/* Just a wrapper for GRC*/
	static sptr
	make(const size_t vlen, const int constellation,
	     const float sampling_rate);
};

}  // namespace cs436

}  // namespace gr


#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_EVM_H_ */
