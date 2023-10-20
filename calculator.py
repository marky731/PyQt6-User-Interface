from PyQt6 import QtWidgets as qw
from calculatorForm import Ui_MainWindow
import sys

class myApp(qw.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.hesapla)
        self.ui.pushButton_2.clicked.connect(self.hesapla)
        self.ui.pushButton_3.clicked.connect(self.hesapla)
        self.ui.pushButton_4.clicked.connect(self.hesapla)


    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == "sum":
            result = int(self.ui.txt_sayi1.toPlainText()) + int(self.ui.txt_sayi2.toPlainText())
        elif sender == "subtrack":
            result = int(self.ui.txt_sayi1.toPlainText()) - int(self.ui.txt_sayi2.toPlainText())
        elif sender == "multiply":
            result = int(self.ui.txt_sayi1.toPlainText()) * int(self.ui.txt_sayi2.toPlainText())
        elif sender == "divide":
            result = int(self.ui.txt_sayi1.toPlainText()) / int(self.ui.txt_sayi2.toPlainText())

        self.ui.lbl_sonuc.setText('sonuc: '+ str(result))


# application = qw.QApplication()

def app():
    app = qw.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())

app()