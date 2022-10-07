from Gui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import


class MeuApp(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MeuApp, self).__init__(parent)
        super().setupUi(self)

        self.frame_3.hide()



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = MeuApp()
    app.show()
    qt.exec_()