from config import *
from input import *
from start import *
from athleteConfirm import *
from rules import *
from wodloop import *
from GroupSplit import *
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

    def show_start(self):
        self.start = Start_Ui_Dialog()
        self.start.switch_window.connect(self.show_config)
        self.start.show()

    def show_config(self):
        self.config = Config_Ui_Dialog(self.action)
        self.config.switch_window.connect(self.show_athleteConfirm)
        self.start.close()
        self.config.show()

    def show_athleteConfirm(self):
        self.athleteConfirm = Confirm_Ui_Dialog(self.team)
        self.athleteConfirm.switch_window_rules.connect(self.show_rules)
        self.athleteConfirm.switch_window_groupSplit.connect(self.show_groupSplit)
        self.config.close()
        self.athleteConfirm.show()

    def show_rules(self):
        self.rules = Rules_Ui_Dialog()
        #self.config.close()
        self.rules.show()

    def show_groupSplit(self, teamConfirmValue):
        self.groupSplit = Group_Ui_Dialog(teamConfirmValue)
        self.groupSplit.switch_window_WodLoop.connect(self.show_wodLoop)
        self.groupSplit.switch_window_AthleteConfirm.connect(self.show_athleteConfirm)
        self.athleteConfirm.close()
        self.groupSplit.show()

    def show_wodLoop(self, teamConfirmValue):
        self.wodLoop = WodLoop_Ui_Dialog(teamConfirmValue)
        self.groupSplit.close()
        self.wodLoop.show()

def main():
    input = Input()
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(input)
    controller.show_start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
