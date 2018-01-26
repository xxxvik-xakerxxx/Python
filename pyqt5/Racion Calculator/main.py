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
            self.ui.label_49.setText(_translate("Dialog", "0.74"))
            self.ui.label_50.setText(_translate("Dialog", "0.34"))

    

    def calc(self):
        _translate = QtCore.QCoreApplication.translate
        phen = int(self.ui.lineEdit.text())
        yach = int(self.ui.lineEdit_2.text())
        kuk = int(self.ui.lineEdit_3.text())
        mk = int(self.ui.lineEdit_4.text())
        fish = int(self.ui.lineEdit_5.text())
        prem = int(self.ui.lineEdit_6.text())
        gmih = int(self.ui.lineEdit_7.text())
        shr = int(self.ui.lineEdit_8.text())
        mk2 = int(self.ui.lineEdit_9.text())
        yam = int(self.ui.lineEdit_10.text())
        trm = int(self.ui.lineEdit_11.text())
        msrs = int(self.ui.lineEdit_12.text())
        rk = int(self.ui.lineEdit_13.text())
        end = phen + yach + kuk + mk + fish + prem + gmih + shr + mk2 + yam + trm + msrs +rk

        if end == 100:
            self.ui.label_12.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        else:
            self.ui.label_12.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        self.open_bd(phen, yach, kuk, mk, fish, prem, gmih, shr, mk2, yam, trm, msrs, rk)

    def open_bd(self, phen, yach, kuk, mk, fish, prem, gmih, shr, mk2, yam, trm, msrs, rk):
        f = open("./data/phen.ini", "r")
        kdg_phen = int(''.join(re.findall(r'\d+', f.readline())))
        sp_phen = int(''.join(re.findall(r'\d+', f.readline())))
        sk_phen = int(''.join(re.findall(r'\d+', f.readline())))
        cal_phen = int(''.join(re.findall(r'\d+', f.readline())))
        fos_phen = int(''.join(re.findall(r'\d+', f.readline())))
        na_phen = int(''.join(re.findall(r'\d+', f.readline())))
        liz_phen = int(''.join(re.findall(r'\d+', f.readline())))
        met_phen = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/yach.ini", "r")
        kdg_yach = int(''.join(re.findall(r'\d+', f.readline())))
        sp_yach = int(''.join(re.findall(r'\d+', f.readline())))
        sk_yach = int(''.join(re.findall(r'\d+', f.readline())))
        cal_yach = int(''.join(re.findall(r'\d+', f.readline())))
        fos_yach = int(''.join(re.findall(r'\d+', f.readline())))
        na_yach = int(''.join(re.findall(r'\d+', f.readline())))
        liz_yach = int(''.join(re.findall(r'\d+', f.readline())))
        met_yach = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/kuk.ini", "r")
        kdg_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        sp_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        sk_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        cal_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        fos_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        na_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        liz_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        met_kuk = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/mk.ini", "r")
        kdg_mk = int(''.join(re.findall(r'\d+', f.readline())))
        sp_mk = int(''.join(re.findall(r'\d+', f.readline())))
        sk_mk = int(''.join(re.findall(r'\d+', f.readline())))
        cal_mk = int(''.join(re.findall(r'\d+', f.readline())))
        fos_mk = int(''.join(re.findall(r'\d+', f.readline())))
        na_mk = int(''.join(re.findall(r'\d+', f.readline())))
        liz_mk = int(''.join(re.findall(r'\d+', f.readline())))
        met_mk = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/fish.ini", "r")
        kdg_fish = int(''.join(re.findall(r'\d+', f.readline())))
        sp_fish = int(''.join(re.findall(r'\d+', f.readline())))
        sk_fish = int(''.join(re.findall(r'\d+', f.readline())))
        cal_fish = int(''.join(re.findall(r'\d+', f.readline())))
        fos_fish = int(''.join(re.findall(r'\d+', f.readline())))
        na_fish = int(''.join(re.findall(r'\d+', f.readline())))
        liz_fish = int(''.join(re.findall(r'\d+', f.readline())))
        met_fish = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/prem.ini", "r")
        kdg_prem = int(''.join(re.findall(r'\d+', f.readline())))
        sp_prem = int(''.join(re.findall(r'\d+', f.readline())))
        sk_prem = int(''.join(re.findall(r'\d+', f.readline())))
        cal_prem = int(''.join(re.findall(r'\d+', f.readline())))
        fos_prem = int(''.join(re.findall(r'\d+', f.readline())))
        na_prem = int(''.join(re.findall(r'\d+', f.readline())))
        liz_prem = int(''.join(re.findall(r'\d+', f.readline())))
        met_prem = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/gmih.ini", "r")
        kdg_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        sp_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        sk_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        cal_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        fos_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        na_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        liz_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        met_gmih = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/shr.ini", "r")
        kdg_shr = int(''.join(re.findall(r'\d+', f.readline())))
        sp_shr = int(''.join(re.findall(r'\d+', f.readline())))
        sk_shr = int(''.join(re.findall(r'\d+', f.readline())))
        cal_shr = int(''.join(re.findall(r'\d+', f.readline())))
        fos_shr = int(''.join(re.findall(r'\d+', f.readline())))
        na_shr = int(''.join(re.findall(r'\d+', f.readline())))
        liz_shr = int(''.join(re.findall(r'\d+', f.readline())))
        met_shr = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/mk2.ini", "r")
        kdg_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        sp_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        sk_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        cal_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        fos_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        na_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        liz_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        met_mk2 = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/yam.ini", "r")
        kdg_yam = int(''.join(re.findall(r'\d+', f.readline())))
        sp_yam = int(''.join(re.findall(r'\d+', f.readline())))
        sk_yam = int(''.join(re.findall(r'\d+', f.readline())))
        cal_yam = int(''.join(re.findall(r'\d+', f.readline())))
        fos_yam = int(''.join(re.findall(r'\d+', f.readline())))
        na_yam = int(''.join(re.findall(r'\d+', f.readline())))
        liz_yam = int(''.join(re.findall(r'\d+', f.readline())))
        met_yam = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/trm.ini", "r")
        kdg_trm = int(''.join(re.findall(r'\d+', f.readline())))
        sp_trm = int(''.join(re.findall(r'\d+', f.readline())))
        sk_trm = int(''.join(re.findall(r'\d+', f.readline())))
        cal_trm = int(''.join(re.findall(r'\d+', f.readline())))
        fos_trm = int(''.join(re.findall(r'\d+', f.readline())))
        na_trm = int(''.join(re.findall(r'\d+', f.readline())))
        liz_trm = int(''.join(re.findall(r'\d+', f.readline())))
        met_trm = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/msrs.ini", "r")
        kdg_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        sp_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        sk_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        cal_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        fos_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        na_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        liz_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        met_msrs = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        f = open("./data/rk.ini", "r")
        kdg_rk = int(''.join(re.findall(r'\d+', f.readline())))
        sp_rk = int(''.join(re.findall(r'\d+', f.readline())))
        sk_rk = int(''.join(re.findall(r'\d+', f.readline())))
        cal_rk = int(''.join(re.findall(r'\d+', f.readline())))
        fos_rk = int(''.join(re.findall(r'\d+', f.readline())))
        na_rk = int(''.join(re.findall(r'\d+', f.readline())))
        liz_rk = int(''.join(re.findall(r'\d+', f.readline())))
        met_rk = int(''.join(re.findall(r'\d+', f.readline())))
        f.close()

        kdg = ( (kdg_phen * phen) + (kdg_yach * yach) + (kdg_kuk * kuk) + (kdg_mk * mk) + (kdg_fish * fish) + (kdg_prem * prem) + (kdg_gmih * gmih) + (kdg_shr * shr) + (kdg_mk2 * mk2) + (kdg_yach * yach) + (kdg_trm * trm) + (kdg_msrs * msrs) + (kdg_rk * rk))/100
        sp =( (sp_phen * phen) + (sp_yach * yach) + (sp_kuk * kuk) + (sp_mk * mk) + (sp_fish * fish) + (sp_prem * prem) + (sp_gmih * gmih) + (sp_shr * shr) + (sp_mk2 * mk2) + (sp_yach * yach) + (sp_trm * trm) + (sp_msrs * msrs) + (sp_rk * rk))/100
        sk =( (sk_phen * phen) + (sk_yach * yach) + (sk_kuk * kuk) + (sk_mk * mk) + (sk_fish * fish) + (sk_prem * prem) + (sk_gmih * gmih) + (sk_shr * shr) + (sk_mk2 * mk2) + (sk_yach * yach) + (sk_trm * trm) + (sk_msrs * msrs) + (sk_rk * rk))/100
        cal =( (cal_phen * phen) + (cal_yach * yach) + (cal_kuk * kuk) + (cal_mk * mk) + (cal_fish * fish) + (cal_prem * prem) + (cal_gmih * gmih) + (cal_shr * shr) + (cal_mk2 * mk2) + (cal_yach * yach) + (cal_trm * trm) + (cal_msrs * msrs) + (cal_rk * rk) )/100
        fos =( (fos_phen * phen) + (fos_yach * yach) + (fos_kuk * kuk) + (fos_mk * mk) + (fos_fish * fish) + (fos_prem * prem) + ( fos_gmih * gmih) + (fos_shr * shr) + (fos_mk2 * mk2) + (fos_yach * yach) + (fos_trm * trm) + (fos_msrs * msrs) + (fos_rk * rk))/100
        na =( (na_phen * phen) + (na_yach * yach) + (na_kuk * kuk) + (na_mk * mk) + (na_fish * fish) + (na_prem * prem) + (na_gmih * gmih) + (na_shr * shr) + (na_mk2 * mk2) + (na_yach * yach) + (na_trm * trm) + (na_msrs * msrs) + (na_rk * rk))/100
        liz =( (liz_phen * phen) + (liz_yach * yach) + (liz_kuk * kuk) + (liz_mk * mk) + (liz_fish * fish) + (liz_prem * prem) + (liz_gmih * gmih) + (liz_shr * shr) + (liz_mk2 * mk2) + (liz_yach * yach) + (liz_trm * trm) + (liz_msrs * msrs) + (liz_rk * rk))/100
        met =( (met_phen * phen) + (met_yach * yach) + (met_kuk * kuk) + (met_mk * mk) + (met_fish * fish) + (met_prem * prem) + (met_gmih * gmih) + (met_shr * shr) + (met_mk2 * mk2) + (met_yach * yach) + (met_trm * trm) + (met_msrs * msrs) + (met_rk * rk))/100

        self.calc_end(kdg, sp, sk, cal, fos, na, liz, met)
        
    def calc_end(self, kdg, sp, sk, cal, fos, na, liz, met):
        _translate = QtCore.QCoreApplication.translate
        
        self.ui.label_20.setText(_translate("Dialog", str(kdg)))
        self.ui.label_21.setText(_translate("Dialog", str(sp)))
        self.ui.label_22.setText(_translate("Dialog", str(sk)))
        self.ui.label_23.setText(_translate("Dialog", str(cal)))
        self.ui.label_24.setText(_translate("Dialog", str(fos)))
        self.ui.label_25.setText(_translate("Dialog", str(na)))
        self.ui.label_47.setText(_translate("Dialog", str(liz)))
        self.ui.label_48.setText(_translate("Dialog", str(met)))

        norm_kdg = float(self.ui.label_26.text())
        norm_sp = float(self.ui.label_27.text())
        norm_sk = float(self.ui.label_28.text())
        norm_cal = float(self.ui.label_29.text())
        norm_fos = float(self.ui.label_30.text())
        norm_na = float(self.ui.label_31.text())
        norm_liz = float(self.ui.label_49.text())
        norm_met = float(self.ui.label_50.text())

        otl_kdg = norm_kdg - kdg
        if kdg == norm_kdg:
            self.ui.label_32.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_32.setText(_translate("Dialog", str(otl_kdg)))
        else:
            self.ui.label_32.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_32.setText(_translate("Dialog", str(otl_kdg)))

        otl_sp = norm_sp - sp
        if sp == norm_sp:
            self.ui.label_33.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_33.setText(_translate("Dialog", str(otl_sp)))
        else:
            self.ui.label_33.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_33.setText(_translate("Dialog", str(otl_sp)))

        otl_sk = norm_sk - sk
        if sk == norm_sk:
            self.ui.label_34.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_34.setText(_translate("Dialog", str(otl_sk)))
        else:
            self.ui.label_34.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_34.setText(_translate("Dialog", str(otl_sk)))

        otl_cal = norm_cal - cal
        if cal == norm_cal:
            self.ui.label_35.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_35.setText(_translate("Dialog", str(otl_cal)))
        else:
            self.ui.label_35.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_35.setText(_translate("Dialog", str(otl_cal)))

        otl_fos = norm_fos - fos
        if fos == norm_fos:
            self.ui.label_36.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_36.setText(_translate("Dialog", str(otl_fos)))
        else:
            self.ui.label_36.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_36.setText(_translate("Dialog", str(otl_fos)))

        otl_na = norm_na - na
        if na == norm_na:
            self.ui.label_37.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_37.setText(_translate("Dialog", str(otl_na)))
        else:
            self.ui.label_37.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_37.setText(_translate("Dialog", str(otl_na)))

        otl_liz = norm_liz - liz
        if liz == norm_liz:
            self.ui.label_51.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_51.setText(_translate("Dialog", str(otl_liz)))
        else:
            self.ui.label_51.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_51.setText(_translate("Dialog", str(otl_liz)))

        otl_met = norm_met - met
        if met == norm_met:
            self.ui.label_52.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_52.setText(_translate("Dialog", str(otl_met)))
        else:
            self.ui.label_52.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_52.setText(_translate("Dialog", str(otl_met)))

        
        
        

    

        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())