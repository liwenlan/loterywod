from config import *
from input import *
from start import *
from athleteConfirm import *
from rules import *
from wodloop import *
from GroupSplit import *
from WodloopMainwindow import *
from StartMainwindow import *
from ConfigMainwindow import *
from AthleteConfirmMainWindow import *
from GroupSplitMainWindow import *

import sys
from PyQt5 import QtCore, QtWidgets


class Controller:

    def __init__(self, input):
        self.start = None
        self.config = None
        self.athleteConfirm = None
        self.rules = None
        self.wodLoop = None
        self.groupSplit = None
        self.action = input.actionConfig
        self.team = input.team
        self.confirmAction = None
        self.confirmBcardList = None

    def show_start(self):
        self.start = Ui_StartMainWindow()
        self.start.switch_window.connect(self.show_config)
        self.start.show()

    def show_config(self):
        self.config = Ui_ConfigMainWindow(self.action)
        self.config.switch_window.connect(self.show_athleteConfirm)
        self.start.close()
        self.config.show()

    def show_athleteConfirm(self, actionConfig, BcardList):
        self.confirmBcardList = BcardList
        self.confirmAction = actionConfig
        self.athleteConfirm = Ui_AthleteConfirmMainWindow(self.team)
        self.athleteConfirm.switch_window_rules.connect(self.show_rules)
        self.athleteConfirm.switch_window_groupSplit.connect(self.show_groupSplit)
        self.config.close()
        self.athleteConfirm.show()

    def show_groupSplit(self, teamConfirmValue, group, teamEveryNum):
        self.groupSplit = Ui_GroupSplitMainWindow(teamConfirmValue, group, teamEveryNum, self.confirmAction,
                                          self.confirmBcardList)
        self.groupSplit.switch_window_WodLoop.connect(self.show_wodLoopNew)
        self.groupSplit.switch_window_AthleteConfirm.connect(self.show_athleteConfirm)
        self.athleteConfirm.close()
        self.groupSplit.show()

    def show_rules(self):
        self.rules = Rules_Ui_Dialog()
        # self.config.close()
        self.rules.show()

    def show_wodLoop(self, teamConfirmValue, teamName, group):
        self.wodLoop = WodLoop_Ui_Dialog(teamConfirmValue, teamName, group, self.confirmAction, self.confirmBcardList)
        self.groupSplit.close()
        self.wodLoop.show()

    def show_wodLoopNew(self, teamConfirmValue, teamName, group):
        self.wodLoopNew = Ui_WodLoopMainWindow(teamConfirmValue, teamName, group, self.confirmAction,
                                               self.confirmBcardList)
        self.groupSplit.close()
        self.wodLoopNew.show()


def main():
    input = Input()
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(input)
    controller.show_start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
