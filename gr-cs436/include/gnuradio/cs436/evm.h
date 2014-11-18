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

namespace gr {

namespace cs436 {

/**
 * The modulation that is used for the current run
 */
typedef enum {
	BPSK = 0,//!< BPSK modulation (2 complex points, currying 1 bit each)
	QPSK = 1,//!< QPSK modulation (4 complex points, currying 2 bits each)
	QAM16 = 2//!< QAM16 modulation (16 complex points, currying 4 bits each)
} constellation_t;

class CS436_API evm : virtual public sync_block
{
public:
	typedef boost::shared_ptr<evm> sptr;

	static sptr
	make(const size_t vlen, const constellation_t constellation,
	     const float sampling_rate);

	/* Just a wrapper for GRC*/
	static sptr
	make(const size_t vlen, const int constellation,
	     const float sampling_rate);
};

}  // namespace cs436

}  // namespace gr


#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_EVM_H_ */
