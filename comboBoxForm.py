# Form implementation generated from reading ui file 'comboBox.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 411)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_cities = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_cities.setGeometry(QtCore.QRect(50, 40, 181, 41))
        self.cb_cities.setObjectName("cb_cities")
        self.lbl_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(260, 40, 161, 41))
        self.lbl_result.setObjectName("lbl_result")
        self.btn_get_items = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_get_items.setGeometry(QtCore.QRect(50, 120, 181, 31))
        self.btn_get_items.setObjectName("btn_get_items")
        self.btn_load_items = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_load_items.setGeometry(QtCore.QRect(260, 120, 161, 31))
        self.btn_load_items.setObjectName("btn_load_items")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
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
        self.lbl_result.setText(_translate("MainWindow", "TextLabel"))
        self.btn_get_items.setText(_translate("MainWindow", "get item"))
        self.btn_load_items.setText(_translate("MainWindow", "load item"))