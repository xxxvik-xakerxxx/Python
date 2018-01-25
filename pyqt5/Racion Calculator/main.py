#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from res.ui import Ui_Dialog
import re

class MyApp(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calc)
        self.ui.pushButton_3.clicked.connect(self.fil_read)
        self.ui.pushButton_4.clicked.connect(qApp.quit)
        self.ui.radioButton.toggled.connect(self.dack)
    

    def dack(self):
        _translate = QtCore.QCoreApplication.translate
        radioButton = self.sender()
    

        if radioButton.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1173"))
            self.ui.label_27.setText(_translate("Dialog", "17.1"))
            self.ui.label_28.setText(_translate("Dialog", "5.5"))
            self.ui.label_29.setText(_translate("Dialog", "2.5"))
            self.ui.label_30.setText(_translate("Dialog", "0.84"))
            self.ui.label_31.setText(_translate("Dialog", "0.45"))
    def calc(self):
        _translate = QtCore.QCoreApplication.translate
        phen = int(self.ui.lineEdit.text())
        yach = int(self.ui.lineEdit_2.text())
        kuk = int(self.ui.lineEdit_3.text())
        mk = int(self.ui.lineEdit_4.text())
        fish = int(self.ui.lineEdit_5.text())
        prem = int(self.ui.lineEdit_6.text())
        end = phen + yach + kuk + mk + fish + prem

        if end > 100:
            self.ui.label_12.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        else:
            self.ui.label_12.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))

    def fil_read(self):
        fphen = open("./data/phen.ini", "r")
        kdg_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        sp_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        sk_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        cal_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        fos_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        na_phen = int(''.join(re.findall(r'\d+', fphen.readline())))
        fphen.close()
        







if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())