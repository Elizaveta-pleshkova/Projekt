from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3


class Vnos(object):
    def setupUi(self, Form):
        #словари для переводов
        self.data = {"Январь": '01', "Февраль": '02', "Март": '03', "Апрель": '04', "Май": '05',
                     "Июнь": '06',
                     "Июль": '07',
                     "Август": '08', "Сентябрь": '09', "Октябрь": '10', "Ноябрь": '11',
                     "Декабрь": '12'}
        self.trans = {'Доход': '1', 'Расход': '0'}

        Form.setObjectName("Внесите данные")
        Form.resize(395, 294)
        # работа с внешним видом
        Form.setStyleSheet("QWidget{\n"
                           "    background-color: #F1F9D2;\n"
                           "}\n"
                           "QLineEdit{\n"
                           "    background-color: #FFFFFF;\n"
                           "    font: 10pt 'Noto Kufi Arabic';\n"
                           "}\n"
                           "QPushButton{\n"
                           "     background-color: #F8FAF4;\n"
                           "     font: 63 12pt 'Yu Gothic UI Semibold';\n"
                           "}\n"
                           "QPushButtont:hover{\n"
                           "     background-color: #D8DCCA;\n"
                           "     font: 63 12pt 'Yu Gothic UI Semibold';\n"
                           "}\n"
                           "QComboBox{\n"
                           "     background-color: #FFFFFF;\n"
                           "}")
        #объявление переменных
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 120, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Январь", "Февраль",
                                "Март", "Апрель", "Май", "Июнь", "Июль",
                                "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 60, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 90, 131, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Доход", "Расход"])

        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 180, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems([str(i) for i in range(2017, 2030)])

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 81, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 71, 32))
        self.label_2.setObjectName("label_2")

        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 150, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems([str(i) for i in range(1, 32)])

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 86, 21))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 81, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 180, 91, 16))
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 351, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.vnosim)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 311, 21))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Внесите данные", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Введите сумму", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Доход или \n"
                                                                      "расход", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Операция", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Выберите месяц", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Выберите день", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Выберите год", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Сохранить изменения",
                                                                 None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "                          ",
                                                              None, -1))
#внос значений в базу данных
    def vnosim(self):
        self.s = sqlite3.connect("baza.db")
        sum = self.lineEdit.text()
        oper = f'"{self.lineEdit_2.text()}"'
        tr = self.trans.get(self.comboBox_2.currentText())
        mon = self.data.get(self.comboBox.currentText())
        print(type(self.data.get(self.comboBox_4.currentText())))
        d = self.comboBox_4.currentText()
        ye = self.comboBox_3.currentText()
        sl = f'{self.comboBox_3.currentText()}' \
            f'{str(self.data.get(self.comboBox.currentText())).zfill(2)}' \
            f'{str(self.comboBox_4.currentText()).zfill(2)}'
        print(f"""INSERT INTO Dohodi(summa, operacia, transact, month, day, year, slot)
           VALUES({sum}, {oper}, {tr}, {mon}, {d}, {ye}, {sl})""")
        self.s.execute(f"""INSERT INTO Dohodi(summa, operacia, transact, month, day, year, slot)
           VALUES({sum}, {oper}, {tr}, {mon}, {d}, {ye}, {sl})""").fetchall()
        self.workform()
        self.s.commit()
#оповещение
    def workform(self):
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "<html><head/>"
                                                                      "<body><p align=\"center\">"
                                                                      "<span style=\""
                                                                      " font-size:12pt;"
                                                                      " color:#ff1f02;\">Данные"
                                                                      " сохранены</span></p></body>"
                                                                      "</html>", None, -1))

#для запуска окна изменения из этого файла
# if __name__ == "__main__":
#     import sys
#
#     vn = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     vnoss = Vnos()
#     vnoss.setupUi(Form)
#     Form.show()
#     sys.exit(vn.exec_())
