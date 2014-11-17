/*
 * api.h
 *
 *  Created on: Nov 13, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_API_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_API_H_

#include <gnuradio/attributes.h>

#ifdef gnuradio_channels_EXPORTS
#  define CS436_API __GR_ATTR_EXPORT
#else
#  define CS436_API __GR_ATTR_IMPORT
#endif

#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_API_H_ */
