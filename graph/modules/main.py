# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        N = 5
        value = (20, 35, 30, 35, 27)
        ind = np.arange(N)
        width = 0.35

        # plt.bar(ind, value, width)
        #
        # plt.ylabel('Scores')
        # plt.title('Scores by group')
        # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
        #
        # plt.show()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(ind, value, width)
        ax.set_xticks(ind + width / 20)
        ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])

        canvas = FigureCanvas(fig)
        canvas.draw()
        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(canvas)
        canvas.show()

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()