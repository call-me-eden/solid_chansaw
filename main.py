import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import main_screen


def main():

    app = main_screen.app
    widget = main_screen.widget

    widget.update()

    app.setStyle('Breeze')

    screen = main_screen.screen()

    screen.window()

    widget.setGeometry(50, 50, 250, 250)

    widget.show()

    app.exec()


if __name__ == '__main__':
    main()
