import sys
 
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
 
 
class Tabs(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__()
        self.all_tabs = []
 
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)
 
        self.build_widgets()
 
    def build_widgets(self):
        for i in range(3):
            self.all_tabs.append(QtWidgets.QWidget())
            self.addTab(self.all_tabs[i], 'Tab {}'.format(i))
 
        self.all_tabs[0].setLayout(QtWidgets.QVBoxLayout())
        self.all_tabs[0].layout().addWidget(QtWidgets.QPushButton('Новая вкладка'))
        # Достаем первый виджет из layout и задаем ему сигнал
        self.all_tabs[0].layout().itemAt(0).widget().clicked.connect(self.create_tab)
 
    def create_tab(self):
        self.all_tabs.append(QtWidgets.QWidget())
        self.addTab(self.all_tabs[len(self.all_tabs) - 1],
                    'Tab {}'.format(len(self.all_tabs)))
 
    def close_tab(self, index):
        widget = self.widget(index)
        widget.deleteLater()
        self.removeTab(index)

class Toolbar(QtWidgets.QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()

        self.initUI()

    def initUI(self):

        newAction = QAction(QIcon('plus.png'), 'Plus', self)


        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(exitAction)

    

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar') 
 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.toolbar_area = Toolbar()
        self.tabs_area = Tabs()

        self.toolBarArea(self.toolbar_area)
 
        self.setCentralWidget(self.tabs_area)
 
 
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
 
sys.exit(app.exec_())
