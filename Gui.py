# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 580)
        MainWindow.setMinimumSize(QtCore.QSize(400, 580))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("background-color: rgb(236, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 9, 0, 3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 75 14pt \"Verdana\";\n"
"    color: white;\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid rgb(231, 15, 0);\n"
"    border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid  rgb(231, 15, 0);\n"
"    border-bottom:3px  solid rgb(255,2555,255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 75 14pt \"Verdana\";\n"
"    color: white;\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid rgb(231, 15, 0);\n"
"    border-bottom: 0px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid  rgb(231, 15, 0);\n"
"    border-bottom:0px  solid rgb(255,2555,255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    font: 75 14pt \"Verdana\";\n"
"    color: white;\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid rgb(231, 15, 0);\n"
"    border-bottom: 0px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 15, 0);\n"
"    border-radius: 0px; border: 3px solid  rgb(231, 15, 0);\n"
"    border-bottom:0px  solid rgb(255,2555,255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(9, 0, 9, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setStyleSheet("border-bottom: 3px rgb(0,0,0);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(500, 20))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(213, 15, 0);\n"
"    border-radius: 0px; border: 0px solid  rgb(213,15,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231,15,0);\n"
"border-radius: 0px; border: 0px solid  rgb(213,15,0);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 452))
        self.frame_3.setStyleSheet("\n"
"background-color: rgb(218, 218, 218);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(500, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(500, 50))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(500, 60))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(213, 15, 0);\n"
"    border-radius: 9px; border: 3px solid  rgb(213,15,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231,15,0);\n"
"border-radius: 9px; border: 3px solid  rgb(213,15,0);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(9, 0, 9, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 452))
        self.frame_5.setStyleSheet("\n"
"background-color: rgb(218, 218, 218);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QtCore.QSize(500, 60))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(213, 15, 0);\n"
"    border-radius: 9px; border: 3px solid  rgb(213,15,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231,15,0);\n"
"border-radius: 9px; border: 3px solid  rgb(213,15,0);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QtCore.QSize(500, 20))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(213, 15, 0);\n"
"    border-radius: 0px; border: 0px solid  rgb(213,15,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(231,15,0);\n"
"border-radius: 0px; border: 0px solid  rgb(213,15,0);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_2.setStyleSheet("border-bottom: 3px rgb(0,0,0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setMaximumSize(QtCore.QSize(50, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_2.setText(_translate("MainWindow", "DOWLOAD"))
        self.pushButton_3.setText(_translate("MainWindow", "CONFIG"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Insira URL Para Baixar"))
        self.pushButton_4.setText(_translate("MainWindow", "LINK"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">foto</p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "TITULO VIDEO"))
        self.pushButton_5.setText(_translate("MainWindow", "CONTINUAR"))
        self.label_3.setText(_translate("MainWindow", "QUALIDADE"))
        self.pushButton_7.setText(_translate("MainWindow", "BAIXAR"))
        self.pushButton_6.setText(_translate("MainWindow", "PASTA"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Local Onde Será Salvo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())