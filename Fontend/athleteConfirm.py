# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'athleteConfirm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from LoteryWod import *
from input import *
from Card import *


class Confirm_Ui_Dialog(QtWidgets.QMainWindow):
    switch_window_rules = QtCore.pyqtSignal()
    switch_window_groupSplit = QtCore.pyqtSignal(object, object)

    def __init__(self, team):
        super(Confirm_Ui_Dialog, self).__init__()
        self.teamConfirm = team
        self.group = 0
        self.setupUi(self)
        self.retranslateUi(self)
        self.athleteNum = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Confirm")
        Dialog.resize(482, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 231, 121))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 213, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 210, 113, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goGroupSplit)
        #self.pushButton.clicked.connect(self.goGroupSplit)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 10, 113, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goRules)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入人数"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "规则说明"))

    def goRules(self):
        self.switch_window_rules.emit()

    def goGroupSplit(self):
        self.confirmGroup()
        self.switch_window_groupSplit.emit(self.teamConfirm, self.group)

    def confirmGroup(self):
        self.athleteNum = int(self.lineEdit.text())
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

        print(teamDeckTemp.athletes)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Confirm_Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
