/*
 * api.h
 *
 *  Created on: Nov 13, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_API_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_API_H_

#include <gnuradio/attributes.h>

/**
 * The modulation that is used for the current run
 */
enum constellation_t{
	BPSK = 2,//!< BPSK modulation (2 complex points, currying 1 bit each)
	QPSK = 4,//!< QPSK modulation (4 complex points, currying 2 bits each)
	QAM16 = 16//!< QAM16 modulation (16 complex points, currying 4 bits each)
};

#ifdef gnuradio_channels_EXPORTS
#  define CS436_API __GR_ATTR_EXPORT
#else
#  define CS436_API __GR_ATTR_IMPORT
#endif

#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_API_H_ */
