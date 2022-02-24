# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'athleteConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from LoteryWod import *
from input import *
from Card import *


class Confirm_Ui_Dialog(QtWidgets.QMainWindow):
    switch_window_rules = QtCore.pyqtSignal()
    switch_window_groupSplit = QtCore.pyqtSignal(object, object, object)

    def __init__(self, team):
        super(Confirm_Ui_Dialog, self).__init__()
        self.teamConfirm = team
        self.teamAthleteList = []
        self.group = 0
        self.setupUi(self)
        self.retranslateUi(self)
        self.athleteNum = 0
        self.tempAthleteNumstring = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Confirm")
        Dialog.resize(482, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 60, 261, 141))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 213, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 210, 113, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goGroupSplit)
        # self.pushButton.clicked.connect(self.goGroupSplit)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 10, 113, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goRules)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "彩票机"))
        self.label.setScaledContents(True)
        gif = QMovie(":/Resources/lottery.gif")
        self.label.setMovie(gif)
        gif.start()
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入人数"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "规则说明"))

    def goRules(self):
        self.switch_window_rules.emit()

    def goGroupSplit(self):
        self.tempAthleteNumstring = self.lineEdit.text()
        if self.tempAthleteNumstring == '':
            QtWidgets.QMessageBox.information(self, '提示', '一个人都没有呢')
        elif int(self.tempAthleteNumstring) <= 0:
            QtWidgets.QMessageBox.information(self, '提示', '可不能没人啊')
        elif int(self.tempAthleteNumstring) > 24:
            QtWidgets.QMessageBox.information(self, '提示', '人太多了，请包包扩容场地')
        else:
            self.confirmGroup()
            print(self.teamAthleteList)
            self.switch_window_groupSplit.emit(self.teamConfirm, self.group, self.teamAthleteList)

    def confirmGroup(self):
        self.athleteNum = int(self.lineEdit.text())
        self.teamAthleteList = setTeamNum(self.athleteNum)
        self.group = setGroupNum(self.athleteNum, self.teamConfirm)
        teamDeckTemp = AthleteDeck()
        if self.group == 3:
            teamDeckTemp.remove('diamond_A')
        elif self.group == 2:
            teamDeckTemp.remove('diamond_A')
            teamDeckTemp.remove('club_A')
        elif self.group == 1:
            teamDeckTemp.remove('diamond_A')
            teamDeckTemp.remove('club_A')
            teamDeckTemp.remove('heart_A')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Confirm_Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
