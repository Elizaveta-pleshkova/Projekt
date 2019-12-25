from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3


class Rashod(object):
    def setupUi(self, Form):
        #словарь для перевода месяцев
        self.data = {"Январь": '01', "Февраль": '02', "Март": '03', "Апрель": '04', "Май": '05',
                     "Июнь": '06',
                     "Июль": '07',
                     "Август": '08', "Сентябрь": '09', "Октябрь": '10', "Ноябрь": '11',
                     "Декабрь": '12'}
        Form.setObjectName("Form")
        Form.resize(400, 328)
        #работа с внешним видом
        Form.setStyleSheet("QWidget{\n"
                           "    background-color: #F1F9D2;\n"
                           "}\n"
                           "QTabWidget{\n"
                           "    background-color: #F8FAF4;\n"
                           "}\n"
                           "QTabWidget:hover{\n"
                           "     background-color: #D8DCCA;\n"
                           "}\n"
                           "QTableWidget{\n"
                           "     background-color: #FFFFFF;\n"
                           "}\n"
                           "QComboBox{\n"
                           "     background-color: #FFFFFF;\n"
                           "}\n"
                           "QPushButton{\n"
                           "    background-color: #F8FAF4;\n"
                           "}\n"
                           "QPushButtont:hover{\n"
                           "     background-color: #D8DCCA;\n"
                           "}\n")
        #объявление переменных
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 201, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 10, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Январь", "Февраль",
                                "Март", "Апрель", "Май", "Июнь", "Июль",
                                "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 381, 251))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_dohod = QtWidgets.QWidget()
        self.tab_dohod.setObjectName("tab_dohod")

        self.tableView_2 = QtWidgets.QTableView(self.tab_dohod)
        self.tableView_2.setGeometry(QtCore.QRect(5, 11, 361, 211))
        self.tableView_2.setObjectName("tableView_2")

        self.tableWidget = QtWidgets.QTableWidget(self.tab_dohod)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 371, 221))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")

        self.tabWidget.addTab(self.tab_dohod, "")

        self.tab_rashod = QtWidgets.QWidget()
        self.tab_rashod.setObjectName("tab_rashod")

        self.tableView = QtWidgets.QTableView(self.tab_rashod)
        self.tableView.setGeometry(QtCore.QRect(5, 11, 361, 211))
        self.tableView.setObjectName("tableView")

        self.tabWidget.addTab(self.tab_rashod, "")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_rashod)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 10, 371, 221))
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 10, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems([str(i) for i in range(2017, 2030)])

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 61, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 31, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form",
                                                             "Ваши доходы и расходы за месяц",
                                                             None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Показать",
                                                                 None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dohod),
                                  QtWidgets.QApplication.translate("Form", "Доходы", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rashod),
                                  QtWidgets.QApplication.translate("Form", "Расходы", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Месяц", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Год", None, -1))
#создание таблицы о расходах из базы данных
    def fill(self):
        self.tableWidget_2.clear()

        labels = ['Сумма', 'Операция', 'День', 'Месяц', 'Год']

        self.tableWidget_2.setColumnCount(len(labels))
        self.tableWidget_2.setHorizontalHeaderLabels(labels)
        m = self.data.get(self.comboBox.currentText())
        y = self.comboBox_2.currentText()
        with sqlite3.connect("baza.db") as connect:
            for summa, operacia, day, month, year, transact, slot in connect.execute(
                    f"""SELECT * FROM Dohodi where transact=0 and month = {m} and year = {y} ORDER BY slot"""):
                row = self.tableWidget_2.rowCount()
                self.tableWidget_2.setRowCount(row + 1)
                self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(summa)))
                self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(operacia))
                self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(day)))
                self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(str(month)))
                self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(str(year)))

#создание таблицы о доходах из базы данных
    def fill0(self):
        self.tableWidget.clear()

        labels = ['Сумма', 'Операция', 'День', 'Месяц', 'Год']

        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        m = self.data.get(self.comboBox.currentText())
        y = self.comboBox_2.currentText()
        with sqlite3.connect("baza.db") as connect:
            for summa, operacia, day, month, year, transact, slot in connect.execute(
                    f"""SELECT * FROM Dohodi where transact=1 and month = {m} and year = {y} ORDER BY slot"""):
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(summa)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(operacia))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(day)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(month)))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(year)))
#вывод таблиц
    def open(self):
        self.fill()
        self.fill0()

#для запуска окна демонстрации доходов и расходов из этого файла
# if __name__ == "__main__":
#     import sys
#
#     smot = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     rash = Rashod()
#     rash.setupUi(Form)
#     Form.show()
#     sys.exit(smot.exec_())
