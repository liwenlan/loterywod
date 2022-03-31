# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WodloopMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_WodLoopMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_WodLoopMainWindow, self).__init__()
        self.wodTime = QTime()
        self.wodTimer = QTimer()
        # self.teamConfigValue = team
        # self.teamNameConfig = teamName
        # self.confirmAction = confirmAction
        # self.confirmBcardList = confirmBcardList
        # self.groupName = []
        # self.group = group
        self.contDownTime = 10 * 1000  # 11sec
        # print(team, teamName, group, confirmAction, confirmBcardList)

    def setupUi(self, WodLoopMainWindow):
        WodLoopMainWindow.setObjectName("WodLoopMainWindow")
        WodLoopMainWindow.resize(844, 520)
        self.centralwidgetWhole = QtWidgets.QWidget(WodLoopMainWindow)
        self.centralwidgetWhole.setObjectName("centralwidgetWhole")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidgetWhole)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())

        self.wodTimer.timeout.connect(self.wodTimer_timeout)

        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QtCore.QSize(820, 30))
        self.labelTitle.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 2)
        self.gridLayoutTeam = QtWidgets.QGridLayout()
        self.gridLayoutTeam.setObjectName("gridLayoutTeam")
        self.pushButtonTeamA = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTeamA.sizePolicy().hasHeightForWidth())
        self.pushButtonTeamA.setSizePolicy(sizePolicy)
        self.pushButtonTeamA.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonTeamA.setFont(font)
        self.pushButtonTeamA.setObjectName("pushButtonTeamA")
        self.gridLayoutTeam.addWidget(self.pushButtonTeamA, 0, 0, 1, 1)
        self.textBrowserTeamA = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserTeamA.sizePolicy().hasHeightForWidth())
        self.textBrowserTeamA.setSizePolicy(sizePolicy)
        self.textBrowserTeamA.setMinimumSize(QtCore.QSize(240, 40))
        self.textBrowserTeamA.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserTeamA.setObjectName("textBrowserTeamA")
        self.gridLayoutTeam.addWidget(self.textBrowserTeamA, 0, 1, 1, 1)
        self.labelScoreA = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelScoreA.setFont(font)
        self.labelScoreA.setObjectName("labelScoreA")
        self.gridLayoutTeam.addWidget(self.labelScoreA, 0, 2, 1, 1)
        self.textBrowserScoreA = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserScoreA.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserScoreA.setObjectName("textBrowserScoreA")
        self.gridLayoutTeam.addWidget(self.textBrowserScoreA, 0, 3, 1, 1)
        self.pushButtonTeamB = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTeamB.sizePolicy().hasHeightForWidth())
        self.pushButtonTeamB.setSizePolicy(sizePolicy)
        self.pushButtonTeamB.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonTeamB.setFont(font)
        self.pushButtonTeamB.setObjectName("pushButtonTeamB")
        self.gridLayoutTeam.addWidget(self.pushButtonTeamB, 1, 0, 1, 1)
        self.textBrowserTeamB = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamB.setMinimumSize(QtCore.QSize(240, 40))
        self.textBrowserTeamB.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserTeamB.setObjectName("textBrowserTeamB")
        self.gridLayoutTeam.addWidget(self.textBrowserTeamB, 1, 1, 1, 1)
        self.labelScoreB = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelScoreB.setFont(font)
        self.labelScoreB.setObjectName("labelScoreB")
        self.gridLayoutTeam.addWidget(self.labelScoreB, 1, 2, 1, 1)
        self.textBrowserScoreB = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserScoreB.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserScoreB.setObjectName("textBrowserScoreB")
        self.gridLayoutTeam.addWidget(self.textBrowserScoreB, 1, 3, 1, 1)
        self.pushButtonTeamC = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTeamC.sizePolicy().hasHeightForWidth())
        self.pushButtonTeamC.setSizePolicy(sizePolicy)
        self.pushButtonTeamC.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonTeamC.setFont(font)
        self.pushButtonTeamC.setObjectName("pushButtonTeamC")
        self.gridLayoutTeam.addWidget(self.pushButtonTeamC, 2, 0, 1, 1)
        self.textBrowserTeamC = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamC.setMinimumSize(QtCore.QSize(240, 40))
        self.textBrowserTeamC.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserTeamC.setObjectName("textBrowserTeamC")
        self.gridLayoutTeam.addWidget(self.textBrowserTeamC, 2, 1, 1, 1)
        self.labelScoreC = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelScoreC.setFont(font)
        self.labelScoreC.setObjectName("labelScoreC")
        self.gridLayoutTeam.addWidget(self.labelScoreC, 2, 2, 1, 1)
        self.textBrowserScoreC = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserScoreC.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserScoreC.setObjectName("textBrowserScoreC")
        self.gridLayoutTeam.addWidget(self.textBrowserScoreC, 2, 3, 1, 1)
        self.textBrowserTeamD = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamD.setMinimumSize(QtCore.QSize(240, 40))
        self.textBrowserTeamD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserTeamD.setObjectName("textBrowserTeamD")
        self.gridLayoutTeam.addWidget(self.textBrowserTeamD, 3, 1, 1, 1)
        self.labelScoreD = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelScoreD.setFont(font)
        self.labelScoreD.setObjectName("labelScoreD")
        self.gridLayoutTeam.addWidget(self.labelScoreD, 3, 2, 1, 1)
        self.textBrowserScoreD = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserScoreD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserScoreD.setObjectName("textBrowserScoreD")
        self.gridLayoutTeam.addWidget(self.textBrowserScoreD, 3, 3, 1, 1)
        self.pushButtonTeamE = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTeamE.sizePolicy().hasHeightForWidth())
        self.pushButtonTeamE.setSizePolicy(sizePolicy)
        self.pushButtonTeamE.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonTeamE.setFont(font)
        self.pushButtonTeamE.setObjectName("pushButtonTeamE")
        self.gridLayoutTeam.addWidget(self.pushButtonTeamE, 4, 0, 1, 1)
        self.textBrowserTeamE = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamE.setMinimumSize(QtCore.QSize(240, 40))
        self.textBrowserTeamE.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserTeamE.setObjectName("textBrowserTeamE")
        self.gridLayoutTeam.addWidget(self.textBrowserTeamE, 4, 1, 1, 1)
        self.labelScoreE = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelScoreE.setFont(font)
        self.labelScoreE.setObjectName("labelScoreE")
        self.gridLayoutTeam.addWidget(self.labelScoreE, 4, 2, 1, 1)
        self.textBrowserScoreE = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserScoreE.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserScoreE.setObjectName("textBrowserScoreE")
        self.gridLayoutTeam.addWidget(self.textBrowserScoreE, 4, 3, 1, 1)
        self.pushButtonTeamD = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTeamD.sizePolicy().hasHeightForWidth())
        self.pushButtonTeamD.setSizePolicy(sizePolicy)
        self.pushButtonTeamD.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonTeamD.setFont(font)
        self.pushButtonTeamD.setObjectName("pushButtonTeamD")
        self.gridLayoutTeam.addWidget(self.pushButtonTeamD, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutTeam, 1, 0, 1, 1)
        self.gridLayoutCard = QtWidgets.QGridLayout()
        self.gridLayoutCard.setObjectName("gridLayoutCard")
        self.pushButtonPickCard = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPickCard.sizePolicy().hasHeightForWidth())
        self.pushButtonPickCard.setSizePolicy(sizePolicy)
        self.pushButtonPickCard.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonPickCard.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonPickCard.setFont(font)
        self.pushButtonPickCard.setObjectName("pushButtonPickCard")
        self.gridLayoutCard.addWidget(self.pushButtonPickCard, 2, 0, 1, 2)
        self.labelCardA = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCardA.sizePolicy().hasHeightForWidth())
        self.labelCardA.setSizePolicy(sizePolicy)
        self.labelCardA.setMinimumSize(QtCore.QSize(180, 240))
        self.labelCardA.setMaximumSize(QtCore.QSize(16777215, 240))
        self.labelCardA.setObjectName("labelCardA")
        self.gridLayoutCard.addWidget(self.labelCardA, 0, 1, 1, 1)
        self.textBrowserWodB = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserWodB.setMinimumSize(QtCore.QSize(180, 40))
        self.textBrowserWodB.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserWodB.setObjectName("textBrowserWodB")
        self.gridLayoutCard.addWidget(self.textBrowserWodB, 1, 1, 1, 1)
        self.textBrowserWodA = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserWodA.setMinimumSize(QtCore.QSize(180, 40))
        self.textBrowserWodA.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowserWodA.setObjectName("textBrowserWodA")
        self.gridLayoutCard.addWidget(self.textBrowserWodA, 1, 0, 1, 1)
        self.labelCardB = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCardB.sizePolicy().hasHeightForWidth())
        self.labelCardB.setSizePolicy(sizePolicy)
        self.labelCardB.setMinimumSize(QtCore.QSize(180, 240))
        self.labelCardB.setMaximumSize(QtCore.QSize(16777215, 240))
        self.labelCardB.setObjectName("labelCardB")
        self.gridLayoutCard.addWidget(self.labelCardB, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutCard, 1, 1, 1, 1)
        self.horizontalLayoutTimer = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTimer.setObjectName("horizontalLayoutTimer")
        self.lcdNumberMin = QtWidgets.QLCDNumber(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lcdNumberMin.setFont(font)
        self.lcdNumberMin.setObjectName("lcdNumberMin")
        self.horizontalLayoutTimer.addWidget(self.lcdNumberMin)
        self.labelMin = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.labelMin.setFont(font)
        self.labelMin.setObjectName("labelMin")
        self.horizontalLayoutTimer.addWidget(self.labelMin)
        self.lcdNumberSec = QtWidgets.QLCDNumber(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lcdNumberSec.setFont(font)
        self.lcdNumberSec.setObjectName("lcdNumberSec")
        self.horizontalLayoutTimer.addWidget(self.lcdNumberSec)
        self.labelSec = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.labelSec.setFont(font)
        self.labelSec.setObjectName("labelSec")
        self.horizontalLayoutTimer.addWidget(self.labelSec)
        self.lcdNumberMSec = QtWidgets.QLCDNumber(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lcdNumberMSec.setFont(font)
        self.lcdNumberMSec.setObjectName("lcdNumberMSec")
        self.horizontalLayoutTimer.addWidget(self.lcdNumberMSec)
        self.labelMSec = QtWidgets.QLabel(self.centralwidgetWhole)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.labelMSec.setFont(font)
        self.labelMSec.setObjectName("labelMSec")
        self.horizontalLayoutTimer.addWidget(self.labelMSec)
        self.pushButtonStartTimer = QtWidgets.QPushButton(self.centralwidgetWhole)
        self.pushButtonStartTimer.setMinimumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStartTimer.setFont(font)
        self.pushButtonStartTimer.setObjectName("pushButtonStartTimer")
        self.pushButtonStartTimer.clicked.connect(self.startWodTimer)
        self.horizontalLayoutTimer.addWidget(self.pushButtonStartTimer)
        self.gridLayout.addLayout(self.horizontalLayoutTimer, 2, 0, 1, 2)

        WodLoopMainWindow.setCentralWidget(self.centralwidgetWhole)

        self.retranslateUi(WodLoopMainWindow)
        QtCore.QMetaObject.connectSlotsByName(WodLoopMainWindow)

    def retranslateUi(self, WodLoopMainWindow):
        _translate = QtCore.QCoreApplication.translate
        WodLoopMainWindow.setWindowTitle(_translate("WodLoopMainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("WodLoopMainWindow", "开始wod吧"))
        self.pushButtonTeamA.setText(_translate("WodLoopMainWindow", "A"))
        self.labelScoreA.setText(_translate("WodLoopMainWindow", "分数"))
        self.pushButtonTeamB.setText(_translate("WodLoopMainWindow", "B"))
        self.labelScoreB.setText(_translate("WodLoopMainWindow", "分数"))
        self.pushButtonTeamC.setText(_translate("WodLoopMainWindow", "C"))
        self.labelScoreC.setText(_translate("WodLoopMainWindow", "分数"))
        self.labelScoreD.setText(_translate("WodLoopMainWindow", "分数"))
        self.pushButtonTeamE.setText(_translate("WodLoopMainWindow", "E"))
        self.labelScoreE.setText(_translate("WodLoopMainWindow", "分数"))
        self.pushButtonTeamD.setText(_translate("WodLoopMainWindow", "D"))
        self.pushButtonPickCard.setText(_translate("WodLoopMainWindow", "抽取本轮Wod"))
        self.labelCardA.setText(_translate("WodLoopMainWindow", "TextLabel"))
        self.labelCardB.setText(_translate("WodLoopMainWindow", "TextLabel"))
        self.labelMin.setText(_translate("WodLoopMainWindow", "分"))
        self.labelSec.setText(_translate("WodLoopMainWindow", "秒"))
        self.labelMSec.setText(_translate("WodLoopMainWindow", "毫秒"))
        self.pushButtonStartTimer.setText(_translate("WodLoopMainWindow", "开始计时"))

    def startWodTimer(self):
        print("in")
        self.wodTime.start()
        self.wodTimer.start(1)

    def wodTimer_timeout(self):
        remainTime = self.contDownTime - self.wodTime.elapsed()
        if self.contDownTime == 10 * 1000 and remainTime == 0:
            self.contDownTime = 30 * 60 * 1000  # 30sec
            self.wodTime.restart()
            self.lcdNumberMSec.display(remainTime % 1000)
            self.lcdNumberSec.display((remainTime // 1000) % 60)
            self.lcdNumberMin.display((remainTime // 1000) // 60)
        elif self.contDownTime == 30 * 60 * 1000 and remainTime == 0:
            self.wodTimer.stop()
            self.lcdNumberMSec.display(0)
            self.lcdNumberSec.display(0)
            self.lcdNumberMin.display(0)
        else:
            self.lcdNumberMSec.display(remainTime % 1000)
            self.lcdNumberSec.display((remainTime // 1000) % 60)
            self.lcdNumberMin.display((remainTime // 1000) // 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()  # 防止进程卡死
    MainWindow = QMainWindow()
    ui = Ui_WodLoopMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())