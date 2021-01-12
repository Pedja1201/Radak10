import sys
from PySide2.QtWidgets import (QWidget,QFileDialog,QTextEdit,QPushButton,QLabel,QVBoxLayout)
from PySide2.QtCore import QDir



class DialogApp(QWidget):
    def __init__(self):
        super().__init__()
#TODO:Uradi funkciju za otvaranje tool-a

    
        self.resize(800,800)

        self.button1 = QPushButton('Upload')

        self.button2 = QPushButton('Import')

        self.labelimage=QLabel()
        self.textEditor = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.labelimage)
        layout.addWidget(self.button2)
        layout.addWidget(self.textEditor)
        self.setLayout(layout)

