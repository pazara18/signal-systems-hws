import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from scipy.io import wavfile
import numpy as np
import simpleaudio as sa


# import sympy
# s = sp.Symbol("s")
# z = sp.Symbol("z")
# w_cl = sp.Symbol("w_cl")
# w_ch = sp.Symbol("w_ch")
# T = sp.Symbol("T")
#
# G_s = ((w_cl ** (-3) * s ** 3) / ((1+s/w_cl)**3 * (1+s/w_ch)**3)).subs(s, 2/T * (1 - z ** (-1)) / (1 + z ** (-1)))
#
# print(sp.collect((sp.simplify(G_s).expand()), z))

# We obtain the coefficients for the Z transfer function by using sympy and commented lines above

# using the filter designed in previous parts
# returns filtered data and sample rate
# filtered data depends on filter mode
def bpf(filename, f_c, bandwidth, filter_mode):
    sample_rate, data = wavfile.read(filename)
    T = 1 / sample_rate
    f_cl = 2 * np.pi * int(f_c - bandwidth * f_c)
    f_ch = 2 * np.pi * int(f_c + bandwidth * f_c)
    b_0 = 8 * T ** 3 * f_ch ** 3
    b_2 = -24 * T ** 3 * f_ch ** 3
    b_4 = +24 * T ** 3 * f_ch ** 3
    b_6 = -8 * T ** 3 * f_ch ** 3

    a_0 = T ** 6 * f_ch ** 3 * f_cl ** 3 + 6 * T ** 5 * f_ch ** 3 * f_cl ** 2 + 6 * T ** 5 * f_ch ** 2 * f_cl ** 3 + 12 * T ** 4 * f_ch ** 3 * f_cl + 36 * T ** 4 * f_ch ** 2 * f_cl ** 2 + 12 * T ** 4 * f_ch * f_cl ** 3 + 8 * T ** 3 * f_ch ** 3 + 72 * T ** 3 * f_ch ** 2 * f_cl + 72 * T ** 3 * f_ch * f_cl ** 2 + 8 * T ** 3 * f_cl ** 3 + 48 * T ** 2 * f_ch ** 2 + 144 * T ** 2 * f_ch * f_cl + 48 * T ** 2 * f_cl ** 2 + 96 * T * f_ch + 96 * T * f_cl + 64
    a_1 = 6 * T ** 6 * f_ch ** 3 * f_cl ** 3 + 24 * T ** 5 * f_ch ** 3 * f_cl ** 2 + 24 * T ** 5 * f_ch ** 2 * f_cl ** 3 + 24 * T ** 4 * f_ch ** 3 * f_cl + 72 * T ** 4 * f_ch ** 2 * f_cl ** 2 + 24 * T ** 4 * f_ch * f_cl ** 3 - 96 * T ** 2 * f_ch ** 2 - 288 * T ** 2 * f_ch * f_cl - 96 * T ** 2 * f_cl ** 2 - 384 * T * f_ch - 384 * T * f_cl - 384
    a_2 = 15 * T ** 6 * f_ch ** 3 * f_cl ** 3 + 30 * T ** 5 * f_ch ** 3 * f_cl ** 2 + 30 * T ** 5 * f_ch ** 2 * f_cl ** 3 - 12 * T ** 4 * f_ch ** 3 * f_cl - 36 * T ** 4 * f_ch ** 2 * f_cl ** 2 - 12 * T ** 4 * f_ch * f_cl ** 3 - 24 * T ** 3 * f_ch ** 3 - 216 * T ** 3 * f_ch ** 2 * f_cl - 216 * T ** 3 * f_ch * f_cl ** 2 - 24 * T ** 3 * f_cl ** 3 - 48 * T ** 2 * f_ch ** 2 - 144 * T ** 2 * f_ch * f_cl - 48 * T ** 2 * f_cl ** 2 + 480 * T * f_ch + 480 * T * f_cl + 960
    a_3 = 20 * T ** 6 * f_ch ** 3 * f_cl ** 3 - 48 * T ** 4 * f_ch ** 3 * f_cl - 144 * T ** 4 * f_ch ** 2 * f_cl ** 2 - 48 * T ** 4 * f_ch * f_cl ** 3 + 192 * T ** 2 * f_ch ** 2 + 576 * T ** 2 * f_ch * f_cl + 192 * T ** 2 * f_cl ** 2 - 1280
    a_4 = 15 * T ** 6 * f_ch ** 3 * f_cl ** 3 - 30 * T ** 5 * f_ch ** 3 * f_cl ** 2 - 30 * T ** 5 * f_ch ** 2 * f_cl ** 3 - 12 * T ** 4 * f_ch ** 3 * f_cl - 36 * T ** 4 * f_ch ** 2 * f_cl ** 2 - 12 * T ** 4 * f_ch * f_cl ** 3 + 24 * T ** 3 * f_ch ** 3 + 216 * T ** 3 * f_ch ** 2 * f_cl + 216 * T ** 3 * f_ch * f_cl ** 2 + 24 * T ** 3 * f_cl ** 3 - 48 * T ** 2 * f_ch ** 2 - 144 * T ** 2 * f_ch * f_cl - 48 * T ** 2 * f_cl ** 2 - 480 * T * f_ch - 480 * T * f_cl + 960
    a_5 = 6 * T ** 6 * f_ch ** 3 * f_cl ** 3 - 24 * T ** 5 * f_ch ** 3 * f_cl ** 2 - 24 * T ** 5 * f_ch ** 2 * f_cl ** 3 + 24 * T ** 4 * f_ch ** 3 * f_cl + 72 * T ** 4 * f_ch ** 2 * f_cl ** 2 + 24 * T ** 4 * f_ch * f_cl ** 3 - 96 * T ** 2 * f_ch ** 2 - 288 * T ** 2 * f_ch * f_cl - 96 * T ** 2 * f_cl ** 2 + 384 * T * f_ch + 384 * T * f_cl - 384
    a_6 = T ** 6 * f_ch ** 3 * f_cl ** 3 - 6 * T ** 5 * f_ch ** 3 * f_cl ** 2 - 6 * T ** 5 * f_ch ** 2 * f_cl ** 3 + 12 * T ** 4 * f_ch ** 3 * f_cl + 36 * T ** 4 * f_ch ** 2 * f_cl ** 2 + 12 * T ** 4 * f_ch * f_cl ** 3 - 8 * T ** 3 * f_ch ** 3 - 72 * T ** 3 * f_ch ** 2 * f_cl - 72 * T ** 3 * f_ch * f_cl ** 2 - 8 * T ** 3 * f_cl ** 3 + 48 * T ** 2 * f_ch ** 2 + 144 * T ** 2 * f_ch * f_cl + 48 * T ** 2 * f_cl ** 2 - 96 * T * f_ch - 96 * T * f_cl + 64

    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    Y_arr = []
    for X in data:
        A = X + (-a_1 * B - a_2 * C - a_3 * D - a_4 * E - a_5 * F - a_6 * G) / a_0
        Y = int((b_0 * A + b_2 * C + b_4 * E + b_6 * G) / a_0)
        Y_arr.append(Y)
        G = F
        F = E
        E = D
        D = C
        C = B
        B = A

    BSP = data - np.array(Y_arr)
    if filter_mode == "BPF":
        return sample_rate, np.array(Y_arr)
    else:
        return sample_rate, BSP


ui_path = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(ui_path + "\\filter.ui", self)
        self.browse.clicked.connect(self.browsefiles)
        self.save_button.clicked.connect(self.save)
        self.play_button.clicked.connect(self.play)
        self.filter_button.clicked.connect(self.filter)
        self.freq_interval.valueChanged.connect(self.freq_changed)
        self.bw_interval.valueChanged.connect(self.bw_changed)
        self.radioButtonBPF.clicked.connect(self.get_type)
        self.radioButtonBSP.clicked.connect(self.get_type)
        self.data = []
        self.filter_type = "BPF"
        self.sample_rate = 44100
        self.filename = ""
        self.filtered = False
        self.playing = None

    # updates frequency label on slide
    def freq_changed(self):
        new_freq = self.freq_interval.value()
        self.freq_value_label.setText(str(new_freq) + "Hz")

    # updates bandwidth label on slide
    def bw_changed(self):
        new_bw = self.bw_interval.value()
        self.bw_value_label.setText(str(new_bw) + "%")

    # gets type from radiobutton
    def get_type(self):
        self.filter_type = "BPF"
        if self.radioButtonBSP.isChecked():
            self.filter_type = "BSP"
        elif self.radioButtonBPF.isChecked():
            self.filter_type = "BPF"

    # used for selecting files via browse
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', ui_path, 'WAV Files (*.wav)')
        self.gui_filename.setText(fname[0])
        if fname[0] != self.filename:
            MainWindow.filtered = False
            self.filename = fname[0]

    # used to display warnings when trying to play or save without filtering
    @staticmethod
    def not_filtered():
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Cannot play or save without Filtering!")
        msg.exec_()

    # method used when play button is pressed
    # plays last filtered data array as wav
    # gives warning prompt if no such data exists
    def play(self):
        if not self.filtered:
            self.not_filtered()
            return
        if self.playing is None:
            self.play_button.setText("Stop")
            self.playing = sa.play_buffer(np.array(self.data).astype(np.int16), 1, 2, self.sample_rate)
        else:
            if not self.playing.is_playing():
                self.play_button.setText("Stop")
                self.playing = sa.play_buffer(np.array(self.data).astype(np.int16), 1, 2, self.sample_rate)
            elif self.playing.is_playing():
                self.play_button.setText("Play")
                sa.stop_all()

    # method used when filter button is pressed
    # gets filtering mode central freq and bandwidth and file from gui and filters given wav file
    # gives warning prompt if no file is chosen
    def filter(self):
        print("filter")
        if self.filename == "":
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Choose a file to filter")
            msg.exec_()
            return
        f_c = self.freq_interval.value()
        bandwidth = self.bw_interval.value() / 100
        self.sample_rate, self.data = bpf(self.filename, f_c, bandwidth, self.filter_type)
        self.filtered = True

    # saves last filtered data to a filenameB.wav file
    # gives warning prompt if no such data exists
    def save(self):
        if not self.filtered:
            self.not_filtered()
            return
        fname = self.filename.split('/')[-1]
        new_filename = fname[0:fname.rfind('.')] + "B.wav"
        wavfile.write(os.path.join(os.getcwd(), new_filename), self.sample_rate, np.array(self.data).astype(np.int16))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(310)
    widget.setFixedWidth(430)
    widget.show()
    sys.exit(app.exec_())
