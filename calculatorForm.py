# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 372)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 75, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 125, 71, 21))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(250, 75, 171, 31))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(250, 125, 171, 31))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 175, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 175, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 175, 80, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 175, 80, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lbl_sonuc = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(250, 220, 141, 21))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number 1: "))
        self.label_2.setText(_translate("MainWindow", "Number 2:"))
        self.pushButton.setText(_translate("MainWindow", "sum"))
        self.pushButton_2.setText(_translate("MainWindow", "subtrack"))
        self.pushButton_3.setText(_translate("MainWindow", "multiply"))
        self.pushButton_4.setText(_translate("MainWindow", "divide"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Result"))
