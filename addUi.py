# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created: Fri Mar 21 08:56:58 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(321, 169)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.title = QtGui.QLineEdit(self.widget)
        self.title.setObjectName(_fromUtf8("title"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.title)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.type = QtGui.QComboBox(self.widget)
        self.type.setObjectName(_fromUtf8("type"))
        self.type.addItem(_fromUtf8(""))
        self.type.addItem(_fromUtf8(""))
        self.type.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.type)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.pages = QtGui.QSpinBox(self.widget)
        self.pages.setMaximum(9999)
        self.pages.setObjectName(_fromUtf8("pages"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pages)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.panels = QtGui.QSpinBox(self.widget)
        self.panels.setMaximum(9999)
        self.panels.setObjectName(_fromUtf8("panels"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.panels)
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Book Title", None))
        self.label_2.setText(_translate("Dialog", "Conversion Type", None))
        self.type.setItemText(0, _translate("Dialog", "EPUB3 (FLAT)", None))
        self.type.setItemText(1, _translate("Dialog", "EPUB3 (COMPLEX)", None))
        self.type.setItemText(2, _translate("Dialog", "Amazon KF8 (COMIC)", None))
        self.label_3.setText(_translate("Dialog", "Pages", None))
        self.label_4.setText(_translate("Dialog", "Panels", None))

