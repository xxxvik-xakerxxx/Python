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
        self.ui.radioButton_2.toggled.connect(self.kur)
        self.ui.radioButton_3.toggled.connect(self.per)

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

    def kur(self):
        _translate = QtCore.QCoreApplication.translate
        radioButton_2 = self.sender()

        if radioButton_2.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1"))
            self.ui.label_27.setText(_translate("Dialog", "1"))
            self.ui.label_28.setText(_translate("Dialog", "1"))
            self.ui.label_29.setText(_translate("Dialog", "1"))
            self.ui.label_30.setText(_translate("Dialog", "1"))
            self.ui.label_31.setText(_translate("Dialog", "1"))
            self.ui.label_49.setText(_translate("Dialog", "1"))
            self.ui.label_50.setText(_translate("Dialog", "1"))

    def per(self):
        _translate = QtCore.QCoreApplication.translate
        radioButton_3 = self.sender()

        if radioButton_3.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1290"))
            self.ui.label_27.setText(_translate("Dialog", "20.5"))
            self.ui.label_28.setText(_translate("Dialog", "5"))
            self.ui.label_29.setText(_translate("Dialog", "1"))
            self.ui.label_30.setText(_translate("Dialog", "0.8"))
            self.ui.label_31.setText(_translate("Dialog", "0.3"))
            self.ui.label_49.setText(_translate("Dialog", "1"))
            self.ui.label_50.setText(_translate("Dialog", "0.43"))

    def calc(self):
        _translate = QtCore.QCoreApplication.translate
        phen = float(self.ui.lineEdit.text())
        yach = float(self.ui.lineEdit_2.text())
        kuk = float(self.ui.lineEdit_3.text())
        m_k = float(self.ui.lineEdit_4.text())
        fish = float(self.ui.lineEdit_5.text())
        prem_8184 = float(self.ui.lineEdit_6.text())
        gmih = float(self.ui.lineEdit_7.text())
        shr = float(self.ui.lineEdit_8.text())
        mk2 = float(self.ui.lineEdit_9.text())
        yam = float(self.ui.lineEdit_10.text())
        trm = float(self.ui.lineEdit_11.text())
        msrs = float(self.ui.lineEdit_12.text())
        r_k = float(self.ui.lineEdit_13.text())
        prem_8203 = float(self.ui.lineEdit_14.text())
        end = phen + yach + kuk + m_k + fish + prem_8184 + gmih + shr + mk2 + yam + trm + msrs +r_k + prem_8203

        if end == 100:
            self.ui.label_12.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        else:
            self.ui.label_12.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        self.open_bd(phen, yach, kuk, m_k, fish, prem_8184, gmih, shr, mk2, yam, trm, msrs, r_k, prem_8203)

    def open_bd(self, phen, yach, kuk, m_k, fish, prem_8184, gmih, shr, mk2, yam, trm, msrs, r_k, prem_8203):
        fille = open("./data/phen.ini", "r")
        kdg_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        na_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        met_phen = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/yach.ini", "r")
        kdg_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        na_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        met_yach = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/kuk.ini", "r")
        kdg_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        na_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        met_kuk = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/mk.ini", "r")
        kdg_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        na_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        met_m_k = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille  = open("./data/fish.ini", "r")
        kdg_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        na_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        met_fish = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/prem_8184.ini", "r")
        kdg_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        na_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        met_prem_8184 = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/gmih.ini", "r")
        kdg_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        na_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        met_gmih = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/shr.ini", "r")
        kdg_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        na_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        met_shr = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/mk2.ini", "r")
        kdg_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        na_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        met_mk2 = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/yam.ini", "r")
        kdg_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        na_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        met_yam = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/trm.ini", "r")
        kdg_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        na_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        met_trm = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/msrs.ini", "r")
        kdg_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        na_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        met_msrs = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/rk.ini", "r")
        kdg_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        na_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        met_r_k = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        fille = open("./data/prem_8203.ini", "r")
        kdg_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        sp_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        sk_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        cal_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        fos_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        na_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        liz_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        met_prem_8203 = float(''.join(re.findall(r'\d+', fille.readline())))
        fille.close()

        kdg = ((kdg_phen/100) * phen) + ((kdg_yach/100) * yach) + ((kdg_kuk/100) * kuk) + ((kdg_m_k/100) * m_k) + ((kdg_fish/100) * fish) + ((kdg_prem_8184/100) * prem_8184) + ((kdg_prem_8203/100) * prem_8203)  + ((kdg_gmih/100) * gmih) + ((kdg_shr/100) * shr) + ((kdg_mk2/100) * mk2) + ((kdg_yam/100) * yam) + ((kdg_trm/100) * trm) + ((kdg_msrs/100) * msrs) + ((kdg_r_k/100) * r_k)
        sp = ((sp_phen/1000) * phen) + ((sp_yach/1000) * yach) + ((sp_kuk/100) * kuk) + ((sp_m_k/1000) * m_k) + ((sp_fish/1000) * fish) + ((sp_prem_8184/10000) * prem_8184) + ((sp_prem_8203/100) * prem_8203)  + ((sp_gmih/1000) * gmih) + ((sp_shr/100) * shr) + ((sp_mk2/100) * mk2) + ((sp_yam/100) * yam) + ((sp_trm/1000) * trm) + ((sp_msrs/1000) * msrs) + ((sp_r_k/100) * r_k)
        sk = ((sk_phen/1000) * phen) + ((sk_yach/1000) * yach) + ((sk_kuk/1000) * kuk) + ((sk_m_k/100) * m_k) + ((sk_fish/100) * fish) + ((sk_prem_8184/100) * prem_8184) + ((sk_prem_8203/100) * prem_8203) + ((sk_gmih/100) * gmih) + ((sk_shr/100) * shr) + ((sk_mk2/100) * mk2) + ((sk_yam/100) * yam) + ((sk_trm/100) * trm) + ((sk_msrs/100) * msrs) + ((sk_r_k/100) * r_k)
        cal =((cal_phen/10000) * phen) + ((cal_yach/10000) * yach) + ((cal_kuk/10000) * kuk) + ((cal_m_k/1000) * m_k) + ((cal_fish/1000) * fish) + ((cal_prem_8184/100) * prem_8184) + ((cal_prem_8203/10000) * prem_8203)  + ((cal_gmih/10000) * gmih) + ((cal_shr/10000) * shr) + ((cal_mk2/10000) * mk2) + ((cal_yam/10000) * yam) + ((cal_trm/10000) * trm) + ((cal_msrs/100) * msrs) + ((cal_r_k/100) * r_k) 
        fos = ((fos_phen/1000) * phen) + ((fos_yach/10000) * yach) + ((fos_kuk/1000) * kuk) + ((fos_m_k/10000) * m_k) + ((fos_fish/1000) * fish) + ((fos_prem_8184/10000) * prem_8184) + ((fos_prem_8203/10000) * prem_8203) + ((fos_gmih/10000) * gmih) + ((fos_shr/10000) * shr) + ((fos_mk2/10000) * mk2) + ((fos_yam/10000) * yam) + ((fos_trm/10000) * trm) + ((fos_msrs/100) * msrs) + ((fos_r_k/100) * r_k)
        na = ((na_phen/10000) * phen) + ((na_yach/10000) * yach) + ((na_kuk/10000) * kuk) + ((na_m_k/10000) * m_k) + ((na_fish/10000) * fish) + ((na_prem_8184/100) * prem_8184) + ((na_prem_8203/1000) * prem_8203)  + ((na_gmih/10000) * gmih) + ((na_shr/10000) * shr) + ((na_mk2/10000) * mk2) + ((na_yam/100) * yam) + ((na_trm/10000) * trm) + ((na_msrs/100) * msrs) + ((na_r_k/100) * r_k)
        liz = ((liz_phen/10000) * phen) + ((liz_yach/1000) * yach) + ((liz_kuk/10000) * kuk) + ((liz_m_k/10000) * m_k) + ((liz_fish/10000) * fish) + ((liz_prem_8184/10000) * prem_8184) + ((liz_prem_8203/10000) * prem_8203)  + ((liz_gmih/10000) * gmih) + ((liz_shr/10000) * shr) + ((liz_mk2/10000) * mk2) + ((liz_yam/10000) * yam) + ((liz_trm/10000) * trm) + ((liz_msrs/100) * msrs) + ((liz_r_k/100) * r_k)
        met = ((met_phen/10000) * phen) + ((met_yach/10000) * yach) + ((met_kuk/10000) * kuk) + ((met_m_k/1000) * m_k) + ((met_fish/10000) * fish) + ((met_prem_8184/10000) * prem_8184) + ((met_prem_8203/10000) * prem_8203) + ((met_gmih/10000) * gmih) + ((met_shr/1000) * shr) + ((met_mk2/10000) * mk2) + ((met_yam/10000) * yam) + ((met_trm/10000) * trm) + ((met_msrs/100) * msrs) + ((met_r_k/100) * r_k)

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