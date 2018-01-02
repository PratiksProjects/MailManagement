from PyQt5.QtWidgets import *
import sys
from welcome import welcome
from checkout import checkout

app = QApplication(sys.argv)

screen = checkout()
checkout.populate_packages(screen,dict())
screen.show()

sys.exit(app.exec_())
