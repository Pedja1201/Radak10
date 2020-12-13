from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip
import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtGui import QIcon, QPixmap, QFont
from strukture_dock import StructureDock
from workspace import WorkspaceWidget
from workspace import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window=QtWidgets.QMainWindow()
        self.main_window.setWindowTitle("DATABASE")
        self.main_window.resize(880, 580)
        self.main_window.setWindowIcon(QIcon("picture/diplay.png"))
        
        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.setToolTip('Our Main Window')
        
        
        

        self.create_menu()


        
        self.main_window.show()

    def setIcon(self):
        appIcon = QIcon("picture/wifi.png")
        self.setWindowIcon(appIcon)
 
 
    def setIconModes(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100,100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label1.setToolTip("Active Icon")
 
        icon2 = QIcon("icon.png")
        label2 = QLabel('Sample', self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100,0)
        label2.setToolTip("Disable Icon")
 
        icon3 = QIcon("icon.png")
        label3 = QLabel('Sample', self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)
        label3.setToolTip("Selected Icon")
 
        

    def create_menu(self):
        self.menu_bar=QtWidgets.QMenuBar(self.main_window)

        #FILE MENU
        file_menu=QtWidgets.QMenu("File", self.menu_bar)
        self.menu_bar.addMenu(file_menu)

        new_action=QtWidgets.QAction(QIcon("./picture/new_file.png"), "New File", self)
        new_action.setShortcut('Ctrl+N')


        open_action=QtWidgets.QAction(QIcon("./picture/openfile.png"), "Open File", self)
        open_action.setShortcut('Ctrl+O')

        open_folder=QtWidgets.QAction(QIcon("./picture/open.png"), "Open Folder", self)
        open_folder.setShortcut('Ctrl+K+O')

        save_action=QtWidgets.QAction(QIcon('./picture/save.png'), "Save", self)
        save_action.setShortcut('Ctrl+S')

        print_action=QtWidgets.QAction(QIcon('./picture/pp.png'),"Print",self)
        print_action.setShortcut('Ctrl+P')

        exit_action=QtWidgets.QAction(QIcon('./picture/xx.png'), "Exit", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(open_folder)
        file_menu.addAction(save_action)
        file_menu.addAction(print_action)
        file_menu.addAction(exit_action)
        
        

        #EDIT MENU
        edit_menu=QtWidgets.QMenu('Edit',self.menu_bar)
        self.menu_bar.addMenu(edit_menu)

        undo_action=QtWidgets.QAction(QIcon('RJP.png'), "Undo", self)
        undo_action.setShortcut('Ctrl+Z')

        cut_action=QtWidgets.QAction(QIcon('RJP.png'),"Cut", self)
        cut_action.setShortcut('Ctrl+X')

        find_action=QtWidgets.QAction(QIcon('RJP.png'), "Find",self)
        find_action.setShortcut('Ctrl+F')

        copy_action=QtWidgets.QAction(QIcon('RJP.png'), "Copy",self)
        copy_action.setShortcut('Ctrl+C')

        paste_action=QtWidgets.QAction(QIcon('RJP.png'),"Paste", self)
        paste_action.setShortcut('Ctrl+V')
        
        edit_menu.addAction(undo_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(find_action)


        view_menu=QtWidgets.QMenu('View',self.menu_bar)
        self.menu_bar.addMenu(view_menu)

        window_menu=QtWidgets.QMenu('Window',self.menu_bar)
        self.menu_bar.addMenu(window_menu)

        help_menu=QtWidgets.QMenu('Help', self.menu_bar)
        self.menu_bar.addMenu(help_menu)

        self.main_window.setMenuBar(self.menu_bar)
        
        #STRUCTURE DOCK
        strukture_dock=StructureDock("Strukture dokumenta", self.main_window)
        

        


        #CENTRALNI VIDZET
        
        central_widget=QtWidgets.QTabWidget(self.main_window)
        central_widget.setStyleSheet('backg')
        central_widget.setTabsClosable(True)

        def delete_tab(index):
            central_widget.removeTab(index)
        central_widget.tabCloseRequested.connect(delete_tab)
        
        


        


        #WORKSPACE
        workspace=WorkspaceWidget(central_widget)
        central_widget.addTab(workspace,QtGui.QIcon("picture/tabela.png"), "Prikaz tabele")
        central_widget.setStyleSheet("color:black")

        def read_file(index):
            path=strukture_dock.model.filePath(index)
            with open(path) as f:
                text=(f.read())
                new_workspace=WorkspaceWidget(central_widget)
                central_widget.addTab(new_workspace, path.split("/")[-1])
                new_workspace.show_text(text)

        strukture_dock.tree.clicked.connect(read_file)
        self.main_window.setCentralWidget(central_widget)
        self.main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, strukture_dock)

        

    