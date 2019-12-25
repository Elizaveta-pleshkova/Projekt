from PySide2 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime


class Glavnaya(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 374)
        # работа с внешним видом
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    background-color: #F1F9D2;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    background-color: #F8FAF4;\n"
                                 "    font: 63 12pt 'Yu Gothic UI Semibold';\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    background-color: #D8DCCA;\n"
                                 "}\n"
                                 "QLCDNumber {\n"
                                 "    background-color: #F5F6EF;\n}"
                                 'QLabel{\n'
                                 '    font: 10pt "Noto Kufi Arabic";\n'
                                 '}')
        # объявление переменных
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 30, 151, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(str(self.schetmonth()))

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(500, 80, 151, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(str(self.schet()))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 361, 91))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 361, 91))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 30, 91, 40))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 90, 91, 21))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar"
                                     )
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Домашняя"
                                                                                 " бухгалтерия",
                                                                   None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow",
                                                                   "Просмотр доходов и расходов",
                                                                   None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Внесение изменений",
                                                                 None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", " Баланс\n"
                                                                          "        за месяц",
                                                            None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow",
                                                              "Общий баланс", None, -1))
#показание баланса
    #за все время
    def schet(self):
        tab = sqlite3.connect("baza.db")
        cur = tab.cursor()

        result0 = cur.execute("""SELECT sum(summa) FROM Dohodi
                                WHERE transact = 0""").fetchone()
        result1 = cur.execute("""SELECT sum(summa) FROM Dohodi
                                        WHERE transact = 1""").fetchone()
        return str(result1[0] - result0[0])
    #за текущий месяц
    def schetmonth(self):
        now = datetime.datetime.now()
        m = now.month
        print(m)
        tab = sqlite3.connect("baza.db")
        cur = tab.cursor()
        result0 = cur.execute(f"""SELECT sum(summa) FROM Dohodi
                                        WHERE transact = 0 and month = {m}""").fetchone()
        print(result0)
        result1 = cur.execute(f"""SELECT sum(summa) FROM Dohodi
                                                WHERE transact = 1 and month = {m}""").fetchone()
        if result0 == (None,) or type(result1) == (None,):
            return 0
        else:
            return str(result1[0] - result0[0])

#для запуска главного окна из этого файла
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Glavnaya()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
