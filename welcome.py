from PyQt5.QtWidgets import *
import sys

class welcome(QWidget):
    def __init__(self):
        self.current = None
        QWidget.__init__(self)
        self.move(300, 100)
        layout = QVBoxLayout()
        title_label = QLabel("Mail Room Package Manager")
        self.id_field = QLineEdit()
        self.room_field = QLineEdit()
        self.setLayout(layout)
        self.submitButton = QPushButton("&Search")
        layout.addWidget(title_label)

        radiobutton = QRadioButton("Buzzcard ID")
        radiobutton.setChecked(True)
        radiobutton.value = "id"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0)
        layout.addWidget(self.id_field)

        radiobutton = QRadioButton("Room Number")
        radiobutton.value = "room"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0)
        layout.addWidget(self.room_field)

        layout.addWidget(self.submitButton)
        self.submitButton.clicked.connect(self.start_search)


    def on_radio_button_toggled(self):
        radiobutton = self.sender()
        self.current = radiobutton.value
        if radiobutton.isChecked():
            print("Selected Value is %s" % (radiobutton.value))
            if radiobutton.value == "id":
                self.id_field.setReadOnly(False)
                self.room_field.setReadOnly(True)
            else:
                self.room_field.setReadOnly(False)
                self.id_field.setReadOnly(True)

    def start_search(self):
        value = ""
        if(self.current == "id"):
            print("id")
        else:        
            print("room")
