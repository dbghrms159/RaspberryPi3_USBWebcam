# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webcam.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exposedDown = QtWidgets.QPushButton(self.centralwidget)
        self.exposedDown.setGeometry(QtCore.QRect(610, 20, 91, 121))
        self.exposedDown.setObjectName("exposedDown")
        self.exposedUp = QtWidgets.QPushButton(self.centralwidget)
        self.exposedUp.setGeometry(QtCore.QRect(710, 20, 91, 121))
        self.exposedUp.setObjectName("exposedUp")
        self.focuseUp = QtWidgets.QPushButton(self.centralwidget)
        self.focuseUp.setGeometry(QtCore.QRect(710, 140, 91, 121))
        self.focuseUp.setObjectName("focuseUp")
        self.focuseDown = QtWidgets.QPushButton(self.centralwidget)
        self.focuseDown.setGeometry(QtCore.QRect(610, 140, 91, 121))
        self.focuseDown.setObjectName("focuseDown")
        self.capture = QtWidgets.QPushButton(self.centralwidget)
        self.capture.setGeometry(QtCore.QRect(610, 270, 191, 161))
        self.capture.setObjectName("capture")
        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(10, 0, 601, 421))
        self.video.setText("")
        self.video.setObjectName("video")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuwebcam = QtWidgets.QMenu(self.menubar)
        self.menuwebcam.setObjectName("menuwebcam")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuwebcam.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cam"))
        self.exposedDown.setText(_translate("MainWindow", "exposure -"))
        self.exposedUp.setText(_translate("MainWindow", "exposure +"))
        self.focuseUp.setText(_translate("MainWindow", "focus +"))
        self.focuseDown.setText(_translate("MainWindow", "focus -"))
        self.capture.setText(_translate("MainWindow", "촬영"))
        self.menuwebcam.setTitle(_translate("MainWindow", "webcam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

