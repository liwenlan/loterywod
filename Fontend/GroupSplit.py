# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupSplit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import time
from LoteryWod import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Group_Ui_Dialog(QtWidgets.QMainWindow):
    switch_window_WodLoop = QtCore.pyqtSignal(object)
    switch_window_AthleteConfirm = QtCore.pyqtSignal()

    def __init__(self, team):
        super(Group_Ui_Dialog, self).__init__()
        self.teamConfigValue = team
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 40, 101, 141))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 40, 171, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2.setVisible(bool(self.teamConfigValue[0]))
        self.textBrowser_2.setVisible(bool(self.teamConfigValue[0]))

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 31, 31))
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 90, 171, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3.setVisible(bool(self.teamConfigValue[1]))
        self.textBrowser_3.setVisible(bool(self.teamConfigValue[1]))

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 31, 31))
        self.label_4.setObjectName("label_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(50, 140, 171, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_4.setVisible(bool(self.teamConfigValue[2]))
        self.textBrowser_4.setVisible(bool(self.teamConfigValue[2]))

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.label_5.setObjectName("label_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(50, 190, 171, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_5.setVisible(bool(self.teamConfigValue[3]))
        self.textBrowser_5.setVisible(bool(self.teamConfigValue[3]))

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 31, 31))
        self.label_6.setObjectName("label_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(50, 240, 171, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_6.setVisible(bool(self.teamConfigValue[4]))
        self.textBrowser_6.setVisible(bool(self.teamConfigValue[4]))

        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(190, 6, 81, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 196, 113, 41))
        self.pushButton.setObjectName("pushButton_enter")
        self.pushButton.clicked.connect(self.pickCard)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(412, 10, 61, 41))
        self.pushButton_2.setObjectName("pushButton_back")
        self.pushButton_2.clicked.connect(self.goAthleteConfirm)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(245, 240, 101, 41))
        self.pushButton_3.setObjectName("pushButton_wodStart")
        self.pushButton_3.clicked.connect(self.goWodLoop)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(351, 241, 111, 41))
        self.pushButton_4.setObjectName("pushButton_restart")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 200, 91, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        #self.label.setText(_translate("Dialog", "cardRegion"))
        picPath = '../Resources/PokerPictures/pokerBack.jpg'
        print(picPath)
        pic = QtGui.QPixmap(picPath).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pic)

        self.label_2.setText(_translate("Dialog", "红桃"))
        self.label_3.setText(_translate("Dialog", "黑桃"))
        self.label_4.setText(_translate("Dialog", "方片"))
        self.label_5.setText(_translate("Dialog", "草花"))
        self.label_6.setText(_translate("Dialog", "E"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">抽 签 分 组</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.pushButton_3.setText(_translate("Dialog", "开始wod"))
        self.pushButton_4.setText(_translate("Dialog", "重开一局"))

    def goWodLoop(self):
        self.switch_window_WodLoop.emit(self.teamConfigValue)

    def goAthleteConfirm(self):
        self.switch_window_AthleteConfirm.emit()

    # def

    def pickCard(self):
        print(self.lineEdit.text())
        person = 9
        team = setTeamNum(person)
        luckyDog = selectAthlete()
        picPath = '../Resources/PokerPictures/' + luckyDog + '.jpg'
        pic = QtGui.QPixmap(picPath).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pic)
        self.label.setScaledContents(True)
        #self.label.setText(picPath)



