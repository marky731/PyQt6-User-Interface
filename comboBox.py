from PyQt6 import QtWidgets as qw
from comboBoxForm import Ui_MainWindow
import sys

class Window(qw.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_cities.addItem('Washington')
        self.ui.cb_cities.addItem('Yozgat')
        self.ui.cb_cities.addItem('Las Vegas')
        self.ui.cb_cities.addItem('New York')
        # self.ui.cb_cities.addItems(['Paris','Berlin','Tokyo'])

        self.ui.btn_load_items.clicked.connect(self.LoadItems)
        self.ui.btn_get_items.clicked.connect(self.getItems)
        self.ui.cb_cities.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cb_cities.currentTextChanged.connect(self.selectedChangedIndex)

    def LoadItems(self):
        cities = ['Paris','Berlin','Tokyo','Rome','Chicago','Rome', 'Barcelona', 'Madrid', 'Pekin', 'Milano', 'Miami']
        self.ui.cb_cities.addItems(cities)

    def getItems(self):
        print(self.ui.cb_cities.currentText())
        print(self.ui.cb_cities.currentIndex())
        count = self.ui.cb_cities.count()
        for index in range(count):
            print(self.ui.cb_cities.itemText(index))

    def selectedChangedIndex(self, index):
        print(index)

    # def selectedChangedText(self, text):
    #     print(text)

app = qw.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
# app.exec()

print("terminated.")