from PyQt5.QtWidgets import *
import sys
from welcome import welcome

app = QApplication(sys.argv)

screen = welcome()
screen.show()

sys.exit(app.exec_())
