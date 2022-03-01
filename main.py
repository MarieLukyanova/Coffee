import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())