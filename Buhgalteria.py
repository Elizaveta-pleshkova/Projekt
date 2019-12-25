from PySide2 import QtCore, QtGui, QtWidgets
from glavnayastr import Glavnaya
from rashod import Rashod
from vnos import Vnos
import sys

#
app = QtWidgets.QApplication(sys.argv)

#
MainWindow = QtWidgets.QMainWindow()
ui = Glavnaya()
ui.setupUi(MainWindow)
MainWindow.show()


# тело программы

# открытие и работы с окном просмотра

def smotr():
    smot = QtWidgets.QVBoxLayout()
    Form = QtWidgets.QWidget()
    rash = Rashod()
    rash.setupUi(Form)
    Form.show()
    smot.exec_()


# открытие и раота с окном изменения

def vnos():
    vn = QtWidgets.QVBoxLayout()
    Form = QtWidgets.QWidget()
    vnoss = Vnos()
    vnoss.setupUi(Form)
    Form.show()
    vn.exec_()


# работа с кнопками

ui.pushButton_2.clicked.connect(smotr)
ui.pushButton.clicked.connect(vnos)
#
sys.exit(app.exec_())
