from PyQt5.QtWidgets import *
from sql import sql_fxn
import sys

class checkout(QWidget):
    self.db = sql_fxn("MailDb.db")
    def __init__(self):
        QWidget.__init__(self)
        self.name = ""
        self.room = ""
        self.move(300, 100)
        self.layout = QVBoxLayout()
        title_label = QLabel("Mail Room Package Manager")
        self.layout.addWidget(title_label)
        self.setLayout(self.layout)

        name_label = QLabel("")
        room_label = QLabel("")
        self.layout.addWidget(title_label)

    def populate_packages(self, packages):
        for package in packages:
            check_box = QCheckBox(package)
            self.layout.addWidget(check_box)

    def get_details_id(self, id):
        packages = self.db.find_unchecked_packages_by_id(id)
        return packages

    def get_details_room(self, room):
        packages = self.db.find_unchecked_packages_by_room(room)
        return packages
