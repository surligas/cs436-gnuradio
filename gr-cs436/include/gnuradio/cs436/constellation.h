/*
 * constellation.h
 *
 *  Created on: Nov 21, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_H_

#include <gnuradio/cs436/api.h>

/**
 * @file constellation.h
 *
 * This files contains the constellation and their mapping for the 3 different
 * modulation schemes.
 */

namespace gr {

namespace cs436 {

static gr_complex _bpsk_points[2] = {
	gr_complex(-1, 0),
	gr_complex(1, 0)
};

static uint8_t _bpsk_mapping[2] = {
	0b0,
	0b1
};

static gr_complex _qpsk_points[4] = {
	gr_complex(-0.70710678,-0.70710678),
	gr_complex(-0.70710678, 0.70710678),
	gr_complex(0.70710678, -0.70710678),
	gr_complex(0.70710678, 0.70710678)
};

static uint8_t _qpsk_mapping[4] = {
	0b00,
	0b01,
	0b10,
	0b11
};

static gr_complex _qam16_points[16] = {
	gr_complex(-0.94868328, -0.94868328),
	gr_complex(-0.94868328, -0.31622776),
	gr_complex(-0.94868328, 0.94868328),
	gr_complex(-0.94868328, 0.31622776),
	gr_complex(-0.31622776, -0.94868328),
	gr_complex(-0.31622776, -0.31622776),
	gr_complex(-0.31622776, 0.94868328),
	gr_complex(-0.31622776, 0.31622776),
	gr_complex(0.94868328, -0.94868328),
	gr_complex(0.94868328, -0.31622776),
	gr_complex(0.94868328, 0.94868328),
	gr_complex(0.94868328, 0.31622776),
	gr_complex(0.31622776, -0.94868328),
	gr_complex(0.31622776, -0.31622776),
	gr_complex(0.31622776, 0.94868328),
	gr_complex(0.31622776, 0.31622776)
};

static uint8_t _qam16_mapping[16] = {
	0b0000,
	0b0001,
	0b0010,
	0b0011,
	0b0100,
	0b0101,
	0b0110,
	0b0111,
	0b1000,
	0b1001,
	0b1010,
	0b1011,
	0b1100,
	0b1101,
	0b1110,
	0b1111
};

}  // namespace cs436

}  // namespace gr


#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_CONSTELLATION_H_ */
