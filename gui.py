from pysynth import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *


class GUISignals(QObject):
    safe_exit = pyqtSignal()


class GUI(QWidget):

    def __init__(self):
        super(GUI, self).__init__()
        self.title = 'PySynth - Feel the wave'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.threadpool = QThreadPool().globalInstance()
        self.gui_signals = GUISignals()
        self.synth_signals = TerminateSignal()
        self.init_gui()
        self.init_synth()

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QGridLayout()

        # Create the splash image widget
        label = QLabel(self)
        pixmap = QPixmap('synthwave.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        # Instrument selector
        inst_select = QComboBox()
        inst_select.addItem('Synth 1')
        inst_select.addItem('Synth 2')

        # Volume control slider
        vol_slider = QSlider(Qt.Vertical)

        # Set up the widget grid layout
        layout.addWidget(label, 0, 0)
        layout.addWidget(inst_select, 1, 0)
        layout.addWidget(vol_slider, 2, 0)
        self.setLayout(layout)

        self.show()

    def init_synth(self):
        synth = PySynth()
        self.threadpool.start(synth)

    def closeEvent(self, event):
        self.synth_signals.safe_exit.emit()
        event.accept()
