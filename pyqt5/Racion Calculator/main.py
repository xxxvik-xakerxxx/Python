#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from res.ui import Ui_Dialog
import re
import sqlite3
conn = sqlite3.connect('./data/data.db')
c = conn.cursor()

class MyApp(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calc)
        self.ui.pushButton_4.clicked.connect(qApp.quit)

    def calc(self):
        _translate = QtCore.QCoreApplication.translate
        if self.ui.radioButton.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1173"))
            self.ui.label_27.setText(_translate("Dialog", "17.1"))
            self.ui.label_28.setText(_translate("Dialog", "5.5"))
            self.ui.label_29.setText(_translate("Dialog", "2.5"))
            self.ui.label_30.setText(_translate("Dialog", "0.84"))
            self.ui.label_31.setText(_translate("Dialog", "0.45"))
            self.ui.label_49.setText(_translate("Dialog", "0.74"))
            self.ui.label_50.setText(_translate("Dialog", "0.34"))

        if self.ui.radioButton_2.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1130"))
            self.ui.label_27.setText(_translate("Dialog", "17"))
            self.ui.label_28.setText(_translate("Dialog", "5.5"))
            self.ui.label_29.setText(_translate("Dialog", "3.1"))
            self.ui.label_30.setText(_translate("Dialog", "0.7"))
            self.ui.label_31.setText(_translate("Dialog", "0.3"))
            self.ui.label_49.setText(_translate("Dialog", "0.75"))
            self.ui.label_50.setText(_translate("Dialog", "0.32"))

        if self.ui.radioButton_3.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1290"))
            self.ui.label_27.setText(_translate("Dialog", "20.5"))
            self.ui.label_28.setText(_translate("Dialog", "5"))
            self.ui.label_29.setText(_translate("Dialog", "1"))
            self.ui.label_30.setText(_translate("Dialog", "0.8"))
            self.ui.label_31.setText(_translate("Dialog", "0.3"))
            self.ui.label_49.setText(_translate("Dialog", "1"))
            self.ui.label_50.setText(_translate("Dialog", "0.43"))
        self.sum_components()

    def sum_components(self):
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
        c.execute("SELECT  kdg FROM komponents")
        row = c.fetchmany(14)
        kdg_phen = row[0][0]
        kdg_yach = row[1][0]
        kdg_kuk = row [2][0]
        kdg_fish = row[3][0]
        kdg_mk2 = row[4][0]
        kdg_m_k = row[5][0]
        kdg_yam = row[6][0]
        kdg_gmih = row[7][0]
        kdg_shr = row[8][0]
        kdg_msrs = row[9][0]
        kdg_trm = row[10][0]
        kdg_r_k = row[11][0]
        kdg_prem_8203 = row[12][0]
        kdg_prem_8184 = row[13][0]
        
        c.execute("SELECT  sp FROM komponents")
        row = c.fetchmany(14)
        sp_phen =  row[0][0]
        sp_yach = row[1][0]
        sp_kuk = row [2][0]
        sp_fish = row[3][0]
        sp_mk2 = row[4][0]
        sp_m_k = row[5][0]
        sp_yam = row[6][0]
        sp_gmih = row[7][0]
        sp_shr = row[8][0]
        sp_msrs = row[9][0]
        sp_trm = row[10][0]
        sp_r_k = row[11][0]
        sp_prem_8203 = row[12][0]
        sp_prem_8184 = row[13][0]

        c.execute("SELECT  sk FROM komponents")
        row = c.fetchmany(14)
        sk_phen =  row[0][0]
        sk_yach = row[1][0]
        sk_kuk = row [2][0]
        sk_fish = row[3][0]
        sk_mk2 = row[4][0]
        sk_m_k = row[5][0]
        sk_yam = row[6][0]
        sk_gmih = row[7][0]
        sk_shr = row[8][0]
        sk_msrs = row[9][0]
        sk_trm = row[10][0]
        sk_r_k = row[11][0]
        sk_prem_8203 = row[12][0]
        sk_prem_8184 = row[13][0]
        
        c.execute("SELECT  cal FROM komponents")
        row = c.fetchmany(14)
        cal_phen =  row[0][0]
        cal_yach = row[1][0]
        cal_kuk = row [2][0]
        cal_fish = row[3][0]
        cal_mk2 = row[4][0]
        cal_m_k = row[5][0]
        cal_yam = row[6][0]
        cal_gmih = row[7][0]
        cal_shr = row[8][0]
        cal_msrs = row[9][0]
        cal_trm = row[10][0]
        cal_r_k = row[11][0]
        cal_prem_8203 = row[12][0]
        cal_prem_8184 = row[13][0]
        
        c.execute("SELECT  fos FROM komponents")
        row = c.fetchmany(14)
        fos_phen =  row[0][0]
        fos_yach = row[1][0]
        fos_kuk = row [2][0]
        fos_fish = row[3][0]
        fos_mk2 = row[4][0]
        fos_m_k = row[5][0]
        fos_yam = row[6][0]
        fos_gmih = row[7][0]
        fos_shr = row[8][0]
        fos_msrs = row[9][0]
        fos_trm = row[10][0]
        fos_r_k = row[11][0]
        fos_prem_8203 = row[12][0]
        fos_prem_8184 = row[13][0]
        
        c.execute("SELECT  na FROM komponents")
        row = c.fetchmany(14)
        na_phen =  row[0][0]
        na_yach = row[1][0]
        na_kuk = row [2][0]
        na_fish = row[3][0]
        na_mk2 = row[4][0]
        na_m_k = row[5][0]
        na_yam = row[6][0]
        na_gmih = row[7][0]
        na_shr = row[8][0]
        na_msrs = row[9][0]
        na_trm = row[10][0]
        na_r_k = row[11][0]
        na_prem_8203 = row[12][0]
        na_prem_8184 = row[13][0]

        c.execute("SELECT liz FROM komponents")
        row = c.fetchmany(14)
        liz_phen =  row[0][0]
        liz_yach = row[1][0]
        liz_kuk = row [2][0]
        liz_fish = row[3][0]
        liz_mk2 = row[4][0]
        liz_m_k = row[5][0]
        liz_yam = row[6][0]
        liz_gmih = row[7][0]
        liz_shr = row[8][0]
        liz_msrs = row[9][0]
        liz_trm = row[10][0]
        liz_r_k = row[11][0]
        liz_prem_8203 = row[12][0]
        liz_prem_8184 = row[13][0]
         
        c.execute("SELECT met FROM komponents")
        row = c.fetchmany(14)
        met_phen =  row[0][0]
        met_yach = row[1][0]
        met_kuk = row [2][0]
        met_fish = row[3][0]
        met_mk2 = row[4][0]
        met_m_k = row[5][0]
        met_yam = row[6][0]
        met_gmih = row[7][0]
        met_shr = row[8][0]
        met_msrs = row[9][0]
        met_trm = row[10][0]
        met_r_k = row[11][0]
        met_prem_8203 = row[12][0]
        met_prem_8184 = row[13][0]

        c.close()
        conn.close()        

        kdg = ((kdg_phen*phen)+(kdg_yach* yach) + (kdg_kuk* kuk) + (kdg_m_k* m_k) + (kdg_fish* fish) + (kdg_prem_8184* prem_8184) + (kdg_prem_8203* prem_8203)  + (kdg_gmih* gmih) + (kdg_shr* shr) + (kdg_mk2* mk2) + (kdg_yam* yam) + (kdg_trm* trm) + (kdg_msrs* msrs) + (kdg_r_k* r_k))/100
        sp = ((sp_phen* phen) + (sp_yach* yach) + (sp_kuk* kuk) + (sp_m_k* m_k) + (sp_fish* fish) + (sp_prem_8184* prem_8184) + (sp_prem_8203* prem_8203)  + (sp_gmih* gmih) + (sp_shr* shr) + (sp_mk2* mk2) + (sp_yam* yam) + (sp_trm* trm) + (sp_msrs* msrs) + (sp_r_k* r_k))/100
        sk = ((sk_phen* phen) + (sk_yach* yach) + (sk_kuk* kuk) + (sk_m_k* m_k) + (sk_fish* fish) + (sk_prem_8184* prem_8184) + (sk_prem_8203* prem_8203) + (sk_gmih* gmih) + (sk_shr* shr) + (sk_mk2* mk2) + (sk_yam* yam) + (sk_trm* trm) + (sk_msrs * msrs) + (sk_r_k* r_k))/100
        cal =((cal_phen* phen) + (cal_yach* yach) + (cal_kuk* kuk) + (cal_m_k* m_k) + (cal_fish* fish) + (cal_prem_8184* prem_8184) + (cal_prem_8203* prem_8203)  + (cal_gmih* gmih) + (cal_shr* shr) + (cal_mk2* mk2) + (cal_yam* yam) + (cal_trm* trm) + (cal_msrs* msrs) + (cal_r_k* r_k))/100 
        fos = ((fos_phen* phen) + (fos_yach* yach) + (fos_kuk* kuk) + (fos_m_k* m_k) + (fos_fish* fish) + (fos_prem_8184* prem_8184) + (fos_prem_8203* prem_8203) + (fos_gmih* gmih) + (fos_shr* shr) + (fos_mk2* mk2) + (fos_yam* yam) + (fos_trm* trm) + (fos_msrs* msrs) + (fos_r_k* r_k))/100
        na = ((na_phen* phen) + (na_yach* yach) + (na_kuk* kuk) + (na_m_k* m_k) + (na_fish* fish) + (na_prem_8184* prem_8184) + (na_prem_8203* prem_8203)  + (na_gmih* gmih) + (na_shr* shr) + (na_mk2* mk2) + (na_yam* yam) + (na_trm* trm) + (na_msrs* msrs) + (na_r_k* r_k))/100
        liz = ((liz_phen* phen) + (liz_yach* yach) + (liz_kuk* kuk) + (liz_m_k* m_k) + (liz_fish* fish) + (liz_prem_8184* prem_8184) + (liz_prem_8203* prem_8203)  + (liz_gmih* gmih) + (liz_shr* shr) + (liz_mk2* mk2) + (liz_yam* yam) + (liz_trm* trm) + (liz_msrs* msrs) + (liz_r_k* r_k))/100
        met = ((met_phen* phen) + (met_yach* yach) + (met_kuk* kuk) + (met_m_k* m_k) + (met_fish* fish) + (met_prem_8184* prem_8184) + (met_prem_8203* prem_8203) + (met_gmih* gmih) + (met_shr* shr) + (met_mk2* mk2) + (met_yam* yam) + (met_trm* trm) + (met_msrs* msrs) + (met_r_k* r_k))/100

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