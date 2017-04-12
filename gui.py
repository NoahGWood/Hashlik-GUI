# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HashlikGUI(object):
    def setupUi(self, HashlikGUI):
        HashlikGUI.setObjectName(_fromUtf8("HashlikGUI"))
        HashlikGUI.resize(400, 320)
        HashlikGUI.setMinimumSize(QtCore.QSize(400, 320))
        self.pushButton = QtGui.QPushButton(HashlikGUI)
        self.pushButton.setGeometry(QtCore.QRect(210, 270, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(HashlikGUI)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 270, 85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit = QtGui.QTextEdit(HashlikGUI)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(HashlikGUI)
        QtCore.QMetaObject.connectSlotsByName(HashlikGUI)

    def retranslateUi(self, HashlikGUI):
        HashlikGUI.setWindowTitle(_translate("HashlikGUI", "Hashlik GUI", None))
        self.pushButton.setText(_translate("HashlikGUI", "Select APK", None))
        self.pushButton_2.setText(_translate("HashlikGUI", "Install", None))

