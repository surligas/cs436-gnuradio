/*
 * hello_world_sync_block.h
 *
 *  Created on: Nov 13, 2014
 *      Author: surligas
 */

#ifndef GR_CS436_INCLUDE_GNURADIO_CS436_HELLO_WORLD_SYNC_BLOCK_H_
#define GR_CS436_INCLUDE_GNURADIO_CS436_HELLO_WORLD_SYNC_BLOCK_H_

/*
 * This is the public header file. Each block should declare in this
 * file, a public constructor and all the available public methods.
 *
 * In order to keep this header file clean, the public methods are declared
 * as pure virtual methods. Private members of the block and the methods
 * are implemented in separate files inside the 'lib' directory of the module.
 *
 */

/*
 * All blocks' header should include the API header file of the current module
 */
#include <gnuradio/cs436/api.h>

/*
 * Depending the block type that we want to use, the appropriate block header file
 * should be included.
 *
 * Sync blocks: #include <gnuradio/sync_block.h>
 * Decimation blocks: #include <gnuradio/sync_decimator.h>
 * Interpolation blocks: #include <gnuradio/sync_interpolator.h>
 * General blocks: #include <gnuradio/block.h>
 */
#include <gnuradio/sync_block.h>


namespace gr {

namespace cs436 {

/* Now declare the public abstract class that inherits from synchronous block
 * abstract class
 *
 * NOTE: The CS436_API should be declared before the class name to set up
 * the visibility attributes properly
 */

class CS436_API hello_world_sync_block : public virtual sync_block
{
public:
	/* Each block should be referenced by a boost shared pointer */
	typedef boost::shared_ptr<hello_world_sync_block> sptr;

	/*
	 * The public availabe block constructor, that returns
	 * a shared pointer of the block
	 */
	static sptr
	make(const float real_mult, const float imag_mult);

	/*
	 * Declare all the public availabe block methods.
	 * As they will be implemented in a seperate class (in the lib directory)
	 * they should be pure virtual
	 */
	virtual void set_real_multiplier(const float mult) = 0;
	virtual void set_imag_multiplier(const float mult) = 0;
};

}  // namespace cs436

}  // namespace gr

#endif /* GR_CS436_INCLUDE_GNURADIO_CS436_HELLO_WORLD_SYNC_BLOCK_H_ */
