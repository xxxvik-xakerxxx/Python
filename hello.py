#!/usr/bin/python
from PyQt4 import Qt
import sys

if __name__ == "__main__" :
	app = Qt.QApplication(sys.argv)
	button = Qt.QPushButton("Exit")
	button.resize(200, 70)
	Qt.QObject.connect(button, Qt.SIGNAL("clicked()"), sys.exit)
	button.show()
	app.exec_()
