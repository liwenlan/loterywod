# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupSplitMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupSplitMainWindow(object):
    def setupUi(self, GroupSplitMainWindow):
        GroupSplitMainWindow.setObjectName("GroupSplitMainWindow")
        GroupSplitMainWindow.resize(844, 567)
        self.centralwidgetWhole = QtWidgets.QWidget(GroupSplitMainWindow)
        self.centralwidgetWhole.setObjectName("centralwidgetWhole")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidgetWhole)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayoutWhole = QtWidgets.QGridLayout()
        self.gridLayoutWhole.setObjectName("gridLayoutWhole")
        self.labelTitle = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.labelTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayoutWhole.addWidget(self.labelTitle, 0, 0, 1, 2)
        self.formLayouTeam = QtWidgets.QFormLayout()
        self.formLayouTeam.setObjectName("formLayouTeam")
        self.labelTeamA = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTeamA.sizePolicy().hasHeightForWidth())
        self.labelTeamA.setSizePolicy(sizePolicy)
        self.labelTeamA.setMinimumSize(QtCore.QSize(50, 50))
        self.labelTeamA.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamA.setFont(font)
        self.labelTeamA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamA.setObjectName("labelTeamA")
        self.formLayouTeam.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTeamA)
        self.textBrowserTeamA = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamA.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowserTeamA.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowserTeamA.setFont(font)
        self.textBrowserTeamA.setObjectName("textBrowserTeamA")
        self.formLayouTeam.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textBrowserTeamA)
        self.labelTeamB = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTeamB.sizePolicy().hasHeightForWidth())
        self.labelTeamB.setSizePolicy(sizePolicy)
        self.labelTeamB.setMinimumSize(QtCore.QSize(50, 50))
        self.labelTeamB.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamB.setFont(font)
        self.labelTeamB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamB.setObjectName("labelTeamB")
        self.formLayouTeam.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTeamB)
        self.textBrowserTeamB = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamB.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowserTeamB.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowserTeamB.setFont(font)
        self.textBrowserTeamB.setObjectName("textBrowserTeamB")
        self.formLayouTeam.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textBrowserTeamB)
        self.labelTeamC = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTeamC.sizePolicy().hasHeightForWidth())
        self.labelTeamC.setSizePolicy(sizePolicy)
        self.labelTeamC.setMinimumSize(QtCore.QSize(50, 50))
        self.labelTeamC.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamC.setFont(font)
        self.labelTeamC.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamC.setObjectName("labelTeamC")
        self.formLayouTeam.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTeamC)
        self.textBrowserTeamC = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamC.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowserTeamC.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowserTeamC.setFont(font)
        self.textBrowserTeamC.setObjectName("textBrowserTeamC")
        self.formLayouTeam.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowserTeamC)
        self.labelTeamD = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTeamD.sizePolicy().hasHeightForWidth())
        self.labelTeamD.setSizePolicy(sizePolicy)
        self.labelTeamD.setMinimumSize(QtCore.QSize(50, 50))
        self.labelTeamD.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamD.setFont(font)
        self.labelTeamD.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamD.setObjectName("labelTeamD")
        self.formLayouTeam.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTeamD)
        self.textBrowserTeamD = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamD.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowserTeamD.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowserTeamD.setFont(font)
        self.textBrowserTeamD.setObjectName("textBrowserTeamD")
        self.formLayouTeam.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowserTeamD)
        self.labelTeamE = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTeamE.sizePolicy().hasHeightForWidth())
        self.labelTeamE.setSizePolicy(sizePolicy)
        self.labelTeamE.setMinimumSize(QtCore.QSize(50, 50))
        self.labelTeamE.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelTeamE.setFont(font)
        self.labelTeamE.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTeamE.setObjectName("labelTeamE")
        self.formLayouTeam.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelTeamE)
        self.textBrowserTeamE = QtWidgets.QTextBrowser(self.centralwidgetWhole)
        self.textBrowserTeamE.setMinimumSize(QtCore.QSize(400, 50))
        self.textBrowserTeamE.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowserTeamE.setFont(font)
        self.textBrowserTeamE.setObjectName("textBrowserTeamE")
        self.formLayouTeam.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textBrowserTeamE)
        self.gridLayoutWhole.addLayout(self.formLayouTeam, 1, 0, 1, 1)
        self.gridLayoutSplit = QtWidgets.QGridLayout()
        self.gridLayoutSplit.setObjectName("gridLayoutSplit")
        self.labelPickCard = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPickCard.sizePolicy().hasHeightForWidth())
        self.labelPickCard.setSizePolicy(sizePolicy)
        self.labelPickCard.setMinimumSize(QtCore.QSize(160, 210))
        self.labelPickCard.setMaximumSize(QtCore.QSize(320, 420))
        self.labelPickCard.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPickCard.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPickCard.setObjectName("labelPickCard")
        self.gridLayoutSplit.addWidget(self.labelPickCard, 0, 1, 2, 2)
        self.lineEditAthleteName = QtWidgets.QLineEdit(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAthleteName.sizePolicy().hasHeightForWidth())
        self.lineEditAthleteName.setSizePolicy(sizePolicy)
        self.lineEditAthleteName.setMinimumSize(QtCore.QSize(160, 70))
        self.lineEditAthleteName.setMaximumSize(QtCore.QSize(160, 70))
        self.lineEditAthleteName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditAthleteName.setObjectName("lineEditAthleteName")
        self.gridLayoutSplit.addWidget(self.lineEditAthleteName, 2, 0, 1, 2)
        self.pushButtonConfirm = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfirm.sizePolicy().hasHeightForWidth())
        self.pushButtonConfirm.setSizePolicy(sizePolicy)
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(160, 90))
        self.pushButtonConfirm.setMaximumSize(QtCore.QSize(200, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonConfirm.setFont(font)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayoutSplit.addWidget(self.pushButtonConfirm, 2, 2, 1, 2)
        self.pushButtonStartWod = QtWidgets.QPushButton(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStartWod.sizePolicy().hasHeightForWidth())
        self.pushButtonStartWod.setSizePolicy(sizePolicy)
        self.pushButtonStartWod.setMinimumSize(QtCore.QSize(320, 90))
        self.pushButtonStartWod.setMaximumSize(QtCore.QSize(400, 90))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStartWod.setFont(font)
        self.pushButtonStartWod.setObjectName("pushButtonStartWod")
        self.gridLayoutSplit.addWidget(self.pushButtonStartWod, 3, 0, 1, 4)
        self.labelLeft = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLeft.sizePolicy().hasHeightForWidth())
        self.labelLeft.setSizePolicy(sizePolicy)
        self.labelLeft.setText("")
        self.labelLeft.setObjectName("labelLeft")
        self.gridLayoutSplit.addWidget(self.labelLeft, 0, 0, 2, 1)
        self.labelRight = QtWidgets.QLabel(self.centralwidgetWhole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRight.sizePolicy().hasHeightForWidth())
        self.labelRight.setSizePolicy(sizePolicy)
        self.labelRight.setText("")
        self.labelRight.setObjectName("labelRight")
        self.gridLayoutSplit.addWidget(self.labelRight, 0, 3, 2, 1)
        self.gridLayoutWhole.addLayout(self.gridLayoutSplit, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayoutWhole, 0, 0, 1, 1)
        GroupSplitMainWindow.setCentralWidget(self.centralwidgetWhole)

        self.retranslateUi(GroupSplitMainWindow)
        QtCore.QMetaObject.connectSlotsByName(GroupSplitMainWindow)

    def retranslateUi(self, GroupSplitMainWindow):
        _translate = QtCore.QCoreApplication.translate
        GroupSplitMainWindow.setWindowTitle(_translate("GroupSplitMainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("GroupSplitMainWindow", "????????????"))
        self.labelTeamA.setText(_translate("GroupSplitMainWindow", "A"))
        self.labelTeamB.setText(_translate("GroupSplitMainWindow", "B"))
        self.labelTeamC.setText(_translate("GroupSplitMainWindow", "C"))
        self.labelTeamD.setText(_translate("GroupSplitMainWindow", "D"))
        self.labelTeamE.setText(_translate("GroupSplitMainWindow", "E"))
        self.labelPickCard.setText(_translate("GroupSplitMainWindow", "TextLabel"))
        self.pushButtonConfirm.setText(_translate("GroupSplitMainWindow", "??????"))
        self.pushButtonStartWod.setText(_translate("GroupSplitMainWindow", "??????wod"))
