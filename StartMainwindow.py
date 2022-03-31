# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from WodloopMainwindow import Ui_WodLoopMainWindow
from config import *



class Ui_StartMainWindow(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super(Ui_StartMainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, StartMainWindow):
        StartMainWindow.setObjectName("StartMainWindow")
        StartMainWindow.resize(844, 567)
        self.centralwidgetWhole = QtWidgets.QWidget(StartMainWindow)
        self.centralwidgetWhole.setObjectName("centralwidgetWhole")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidgetWhole)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelConfigPicture = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelConfigPicture.sizePolicy().hasHeightForWidth())
        self.labelConfigPicture.setSizePolicy(sizePolicy)
        self.labelConfigPicture.setMinimumSize(QtCore.QSize(400, 250))
        self.labelConfigPicture.setMaximumSize(QtCore.QSize(1600, 1000))
        self.labelConfigPicture.setObjectName("labelConfigPicture")
        self.verticalLayout.addWidget(self.labelConfigPicture)
        spacerItem = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonConfig = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfig.sizePolicy().hasHeightForWidth())
        self.pushButtonConfig.setSizePolicy(sizePolicy)
        self.pushButtonConfig.setMinimumSize(QtCore.QSize(400, 80))
        self.pushButtonConfig.setMaximumSize(QtCore.QSize(1600, 160))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonConfig.setFont(font)
        self.pushButtonConfig.setObjectName("pushButtonConfig")
        self.verticalLayout.addWidget(self.pushButtonConfig)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.pushButtonConfig.clicked.connect(self.goConfig)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 3, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 2, 1)
        StartMainWindow.setCentralWidget(self.centralwidgetWhole)

        self.retranslateUi(StartMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StartMainWindow)

    def retranslateUi(self, StartMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StartMainWindow.setWindowTitle(_translate("StartMainWindow", "MainWindow"))
        self.pushButtonConfig.setText(_translate("StartMainWindow", "配置本次的动作"))

        jpg = QtGui.QPixmap(":/Resources/crossfit.png").scaled(self.labelConfigPicture.width(), self.labelConfigPicture.height())
        self.labelConfigPicture.setPixmap(jpg)
        self.labelConfigPicture.setScaledContents(True)


    def goConfig(self):
        self.switch_window.emit()


