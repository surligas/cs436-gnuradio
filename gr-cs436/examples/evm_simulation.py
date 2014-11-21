#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Evm Simulation
# Generated: Fri Nov 21 03:33:48 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import cs436
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys

from distutils.version import StrictVersion
class evm_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Evm Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Evm Simulation")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "evm_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.vlen = vlen = 64
        self.samp_rate = samp_rate = 1e6
        self.noise_amp = noise_amp = 0

        ##################################################
        # Blocks
        ##################################################
        self._noise_amp_layout = Qt.QVBoxLayout()
        self._noise_amp_tool_bar = Qt.QToolBar(self)
        self._noise_amp_layout.addWidget(self._noise_amp_tool_bar)
        self._noise_amp_tool_bar.addWidget(Qt.QLabel("Noise Amplitude"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._noise_amp_counter = qwt_counter_pyslot()
        self._noise_amp_counter.setRange(0, 1, 0.01)
        self._noise_amp_counter.setNumButtons(2)
        self._noise_amp_counter.setValue(self.noise_amp)
        self._noise_amp_tool_bar.addWidget(self._noise_amp_counter)
        self._noise_amp_counter.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._noise_amp_slider.setRange(0, 1, 0.01)
        self._noise_amp_slider.setValue(self.noise_amp)
        self._noise_amp_slider.setMinimumWidth(200)
        self._noise_amp_slider.valueChanged.connect(self.set_noise_amp)
        self._noise_amp_layout.addWidget(self._noise_amp_slider)
        self.top_layout.addLayout(self._noise_amp_layout)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        
        labels = ["Reference Points", "Received Points", "", "", "",
                  "", "", "", "", ""]
        widths = [2, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [2.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.cs436_constellation_source_0 = cs436.constellation_source(64, 2)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, vlen)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, vlen)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*vlen, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vlen)
        self.blocks_add_xx_0 = blocks.add_vcc(vlen)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, noise_amp, 0, 8192)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.cs436_constellation_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_const_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "evm_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vlen(self):
        return self.vlen

    def set_vlen(self, vlen):
        self.vlen = vlen

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise_amp)
        Qt.QMetaObject.invokeMethod(self._noise_amp_counter, "setValue", Qt.Q_ARG("double", self.noise_amp))
        Qt.QMetaObject.invokeMethod(self._noise_amp_slider, "setValue", Qt.Q_ARG("double", self.noise_amp))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = evm_simulation()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
