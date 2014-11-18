#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Nov 19 00:19:58 2014
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
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.real_mult = real_mult = 1
        self.imag_mult = imag_mult = 1
        self.freq = freq = 1e3

        ##################################################
        # Blocks
        ##################################################
        self._real_mult_layout = Qt.QVBoxLayout()
        self._real_mult_tool_bar = Qt.QToolBar(self)
        self._real_mult_layout.addWidget(self._real_mult_tool_bar)
        self._real_mult_tool_bar.addWidget(Qt.QLabel("Real multiplier"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._real_mult_counter = qwt_counter_pyslot()
        self._real_mult_counter.setRange(0, 20, 1)
        self._real_mult_counter.setNumButtons(2)
        self._real_mult_counter.setValue(self.real_mult)
        self._real_mult_tool_bar.addWidget(self._real_mult_counter)
        self._real_mult_counter.valueChanged.connect(self.set_real_mult)
        self._real_mult_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._real_mult_slider.setRange(0, 20, 1)
        self._real_mult_slider.setValue(self.real_mult)
        self._real_mult_slider.setMinimumWidth(200)
        self._real_mult_slider.valueChanged.connect(self.set_real_mult)
        self._real_mult_layout.addWidget(self._real_mult_slider)
        self.top_layout.addLayout(self._real_mult_layout)
        self._imag_mult_layout = Qt.QVBoxLayout()
        self._imag_mult_tool_bar = Qt.QToolBar(self)
        self._imag_mult_layout.addWidget(self._imag_mult_tool_bar)
        self._imag_mult_tool_bar.addWidget(Qt.QLabel("Imaginary multiplier"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._imag_mult_counter = qwt_counter_pyslot()
        self._imag_mult_counter.setRange(0, 20, 1)
        self._imag_mult_counter.setNumButtons(2)
        self._imag_mult_counter.setValue(self.imag_mult)
        self._imag_mult_tool_bar.addWidget(self._imag_mult_counter)
        self._imag_mult_counter.valueChanged.connect(self.set_imag_mult)
        self._imag_mult_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._imag_mult_slider.setRange(0, 20, 1)
        self._imag_mult_slider.setValue(self.imag_mult)
        self._imag_mult_slider.setMinimumWidth(200)
        self._imag_mult_slider.valueChanged.connect(self.set_imag_mult)
        self._imag_mult_layout.addWidget(self._imag_mult_slider)
        self.top_layout.addLayout(self._imag_mult_layout)
        self._freq_layout = Qt.QVBoxLayout()
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_layout.addWidget(self._freq_tool_bar)
        self._freq_tool_bar.addWidget(Qt.QLabel("Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_counter = qwt_counter_pyslot()
        self._freq_counter.setRange(500, 100e3, 1)
        self._freq_counter.setNumButtons(2)
        self._freq_counter.setValue(self.freq)
        self._freq_tool_bar.addWidget(self._freq_counter)
        self._freq_counter.valueChanged.connect(self.set_freq)
        self._freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_slider.setRange(500, 100e3, 1)
        self._freq_slider.setValue(self.freq)
        self._freq_slider.setMinimumWidth(200)
        self._freq_slider.valueChanged.connect(self.set_freq)
        self._freq_layout.addWidget(self._freq_slider)
        self.top_layout.addLayout(self._freq_layout)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        
        labels = ["Real part", "Imaginary part", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.cs436_hello_world_sync_block_0 = cs436.hello_world_sync_block(real_mult, imag_mult)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.cs436_hello_world_sync_block_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.cs436_hello_world_sync_block_0, 0))
        self.connect((self.cs436_hello_world_sync_block_0, 1), (self.qtgui_time_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_real_mult(self):
        return self.real_mult

    def set_real_mult(self, real_mult):
        self.real_mult = real_mult
        self.cs436_hello_world_sync_block_0.set_real_multiplier(self.real_mult)
        Qt.QMetaObject.invokeMethod(self._real_mult_counter, "setValue", Qt.Q_ARG("double", self.real_mult))
        Qt.QMetaObject.invokeMethod(self._real_mult_slider, "setValue", Qt.Q_ARG("double", self.real_mult))

    def get_imag_mult(self):
        return self.imag_mult

    def set_imag_mult(self, imag_mult):
        self.imag_mult = imag_mult
        self.cs436_hello_world_sync_block_0.set_imag_multiplier(self.imag_mult)
        Qt.QMetaObject.invokeMethod(self._imag_mult_counter, "setValue", Qt.Q_ARG("double", self.imag_mult))
        Qt.QMetaObject.invokeMethod(self._imag_mult_slider, "setValue", Qt.Q_ARG("double", self.imag_mult))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        Qt.QMetaObject.invokeMethod(self._freq_counter, "setValue", Qt.Q_ARG("double", self.freq))
        Qt.QMetaObject.invokeMethod(self._freq_slider, "setValue", Qt.Q_ARG("double", self.freq))
        self.analog_sig_source_x_0.set_frequency(self.freq)

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
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
