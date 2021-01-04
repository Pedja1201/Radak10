import sys

from PySide2 import QtWidgets, QtGui, QtCore
from strukture_dock import StructureDock
from workspace import WorkspaceWidget
from data_generator import GenerickiModel



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
#TODO:Uradi funkciju za otvaranje tool-a