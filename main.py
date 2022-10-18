from Gui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from pytube import YouTube
from time import sleep
from tmb_download import img_jpg
from threading import Thread

class MeuApp(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MeuApp, self).__init__(parent)
        super().setupUi(self)

        self.progressBar.hide()
        self.label_2.hide()
        self.pushButton_5.hide()
        self.label.hide()

        self.pushButton_4.clicked.connect(self.link)

    def link(self):
        self.link = self.lineEdit.text()
        if self.link == '':
            QtWidgets.QMessageBox.about(self.page, "Opa", "Cade o link?")
            return
        try:
            self.yt = YouTube(str(self.link))
        except:
            QtWidgets.QMessageBox.about(self.page, 'opa', 'O link esta igual tua cara')
            return

        else:
            Thread(target=self.pbar).start()
            thumb_link = self.yt.thumbnail_url

            img_jpg(thumb_link, 'img/', 'thumb')
            self.label.setStyleSheet("border-image: url(img/thumb.jpg);")

            self.label_2.setText(self.yt.streams[0].title)
            self.progressBar.hide()
            self.label_2.show()
            self.pushButton_5.show()
            self.label.show()

            self.lineEdit.setText('')
    def pbar(self):
        self.progressBar.show()
        self.pb = self.progressBar
        for i in range(101):
            sleep(0.018)
            self.pb.setValue(i)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = MeuApp()
    app.show()
    qt.exec_()