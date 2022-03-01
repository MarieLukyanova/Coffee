import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QButtonGroup
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.addcoffee)
        self.load_table()

    def load_table(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Название', 'Степень обжарки', 'Молотый/в зёрнах', 'Описание вкуса',
                                              'Цена', 'Объём упаковки'])
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        rows = cur.execute("""SELECT * FROM кофе""").fetchall()
        for i, row in enumerate(rows):
            if self.table.rowCount() < len(rows):
                self.table.setRowCount(
                    self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()
        con.close()

    def addcoffee(self):
        ex1 = Add()
        ex1.show()
        self.load_table()


class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.addcoffee)
        var = ['Слабая', 'Средняя', 'Сильная', 'Высшая степень']
        self.combo.addItems(var)
        self.rad1.toggled.connect(self.check)
        self.rad2.toggled.connect(self.check)
        self.butts = QButtonGroup()
        self.butts.addButton(self.rad1)
        self.butts.addButton(self.rad2)

    def check(self):
        self.cer = self.sender().text()

    def addcoffee(self):
        name = self.editsort.text()
        text = self.plainTextEdit.toPlainText()
        v = self.volume.text()
        p = self.price.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO кофе(Название, Степень обжарки, Молотый/в зёрнах, Описание вкуса, Цена,
                                        Объём упаковки)
                                        VALUES('{name}', '{self.combo.currentText()}', '{self.cer}', '{text}', '{v}',
                                                '{p}');""")

        con.commit()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())