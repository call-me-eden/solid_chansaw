import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyparsing import null_debug_action
from functools import partial

app = QApplication([])
widget = QWidget()

num1 = 0
num2 = 0

user_input = []

has_inputted = False


# put it in a class so You can __init__ surface

# class button_presses:

header = QLabel(widget)

headerText = ["1", "2"]




class screen:


    def tryouts(self):
        print('jebus')

    def button_click(self, num):

        print(num)

        header.setText(header.text() + " " + str(num))


    def window(self):

        row = 0
        rng = range(9)
        buttonWidth = 50
        buttonHeight = 30

        for i in rng:
            col = i % 3
            if i % 3 == 0:
                row += 1
            x = (col * buttonWidth)
            y = (row * buttonHeight)

            button = QPushButton(widget)
            button.setText(str(i + 1))
            button.setGeometry(x, y + 50, buttonWidth, buttonHeight)
            button.clicked.connect(partial(self.button_click, i))

        header.setGeometry(25, 25, 200, 30)
        # button1 = QPushButton(widget)
        # button1.setGeometry(25, 75, 50, 30)
        #
        # button2 = QPushButton(widget)
        # button2.setGeometry(100, 75, 50, 30)
        #
        # button3 = QPushButton(widget)
        # button3.setGeometry(175, 75, 50, 30)
        #
        # button4 = QPushButton(widget)
        # button4.setGeometry(25, 125, 50, 30)
        #
        # button5 = QPushButton(widget)
        # button5.setGeometry(100, 125, 50, 30)
        #
        # button6 = QPushButton(widget)
        # button6.setGeometry(175, 125, 50, 30)
        #
        # button7 = QPushButton(widget)
        # button7.setGeometry(25, 175, 50, 30)
        #
        # button8 = QPushButton(widget)
        # button8.setGeometry(100, 175, 50, 30)
        #
        # button9 = QPushButton(widget)
        # button9.setGeometry(175, 175, 50, 30)

        # button1.clicked.connect(button1_click)
        #header.setText(str(headerText))
