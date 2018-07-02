import sys
import gui
from PyQt5 import QtWidgets, QtGui, QtCore

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game1 = gui.TicTacToeGUI()
    sys.exit(app.exec_())
