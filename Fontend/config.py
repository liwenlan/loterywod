# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from LoteryWod import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Config_Ui_Dialog(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(object, object)

    def __init__(self, action):
        super(Config_Ui_Dialog, self).__init__()
        self.bonus = None
        self.diamond = None
        self.club = None
        self.spade = None
        self.heart = None
        self.actionConfig = action
        self.setupUi(self)
        self.retranslateUi(self)
        self.suit = []  # 记录不同花色对应的动作以及炸弹动作
        self.BcardList = []  # 记录被勾选的Bcard

    def setupUi(self, Dialog):
        Dialog.setObjectName("Config")
        Dialog.resize(478, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 51, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 51, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 51, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 50, 51, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(260, 110, 51, 41))
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(310, 110, 31, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 130, 31, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(310, 150, 41, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 170, 41, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(350, 110, 41, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(350, 130, 31, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(350, 150, 31, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(350, 170, 41, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(390, 110, 31, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_10.setGeometry(QtCore.QRect(390, 130, 41, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_11.setGeometry(QtCore.QRect(390, 150, 41, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_12.setGeometry(QtCore.QRect(390, 170, 41, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_13.setGeometry(QtCore.QRect(430, 110, 41, 20))
        self.checkBox_13.setObjectName("checkBox_13")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 210, 121, 51))
        self.pushButton.setObjectName("enterConfig")
        self.pushButton.clicked.connect(self.configConfirm)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit_heart")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 110, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_spade")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 170, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_club")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 230, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_diamond")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 60, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_bonus")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:18pt;\">动作库配置</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "heart"))
        self.label_3.setText(_translate("Dialog", "spade"))
        self.label_4.setText(_translate("Dialog", "club"))
        self.label_5.setText(_translate("Dialog", "diamond"))
        self.label_6.setText(_translate("Dialog", "bonus"))
        self.label_7.setText(_translate("Dialog", "Bcard"))
        self.checkBox.setText(_translate("Dialog", "A"))
        self.checkBox_2.setText(_translate("Dialog", "2"))
        self.checkBox_3.setText(_translate("Dialog", "3"))
        self.checkBox_4.setText(_translate("Dialog", "4"))
        self.checkBox_5.setText(_translate("Dialog", "5"))
        self.checkBox_6.setText(_translate("Dialog", "6"))
        self.checkBox_7.setText(_translate("Dialog", "7"))
        self.checkBox_8.setText(_translate("Dialog", "8"))
        self.checkBox_9.setText(_translate("Dialog", "9"))
        self.checkBox_10.setText(_translate("Dialog", "10"))
        self.checkBox_11.setText(_translate("Dialog", "J"))
        self.checkBox_12.setText(_translate("Dialog", "Q"))
        self.checkBox_13.setText(_translate("Dialog", "K"))
        self.pushButton.setText(_translate("Dialog", "确认"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "请输入红桃的动作"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "请输入黑桃的动作"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "请输入梅花的动作"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "请输入方片的动作"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "请输入彩蛋的动作"))

    def configConfirm(self):
        self.collectConfigration()
        if self.heart == '' or self.spade == '' or self.club == '' or self.diamond == '' or self.bonus == '':
            print("jinlaile")
            QtWidgets.QMessageBox.information(self, '提示', '好像还没有填完呢')
        else:
            self.getBcardState()
            self.goAthleteConfirm()

    def collectConfigration(self):
        self.heart = self.lineEdit.text()
        self.spade = self.lineEdit_2.text()
        self.club = self.lineEdit_3.text()
        self.diamond = self.lineEdit_4.text()
        self.bonus = self.lineEdit_5.text()
        self.suit = [self.heart, self.spade, self.club, self.diamond, self.bonus]
        self.actionConfig.update(
            {'heart': self.heart, 'spade': self.spade, 'club': self.club, 'diamond': self.diamond,
             'bonus': self.bonus})

    def setWodConfig(self):
        pass

    def setAction(self, heart, spade, club, diamond, bonus):
        pass

    def goAthleteConfirm(self):
        self.switch_window.emit(self.actionConfig, self.BcardList)

    def getBcardState(self):
        """
        获取Bcard中勾选的选项
        :return: Bcard中勾选的选项
        """
        stateA = self.checkBox.checkState()
        state2 = self.checkBox_2.checkState()
        state3 = self.checkBox_3.checkState()
        state4 = self.checkBox_4.checkState()
        state5 = self.checkBox_5.checkState()
        state6 = self.checkBox_6.checkState()
        state7 = self.checkBox_7.checkState()
        state8 = self.checkBox_8.checkState()
        state9 = self.checkBox_9.checkState()
        state10 = self.checkBox_10.checkState()
        stateJ = self.checkBox_11.checkState()
        stateQ = self.checkBox_12.checkState()
        stateK = self.checkBox_13.checkState()
        Bcard = [stateA, state2, state3, state4, state5, state6, state7, state8, state9, state10, stateJ, stateQ,
                 stateK]
        for index in range(len(Bcard)):
            if Bcard[index] == 2:
                if index == 0:
                    self.BcardList.append('A')
                elif index == 10:
                    self.BcardList.append('J')
                elif index == 11:
                    self.BcardList.append('Q')
                elif index == 12:
                    self.BcardList.append('K')
                else:
                    self.BcardList.append(str(index + 1))

        print("BcardList is ", self.BcardList)
