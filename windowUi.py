# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(767, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/PNG/png/stunjelly-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/PNG/png/stunjelly-logo.png")))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(296, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.plainTextEdit.setFrameShape(QtGui.QFrame.StyledPanel)
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout_5.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.widget)
        self.date = QtGui.QLabel(self.centralwidget)
        self.date.setMinimumSize(QtCore.QSize(0, 0))
        self.date.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.date.setObjectName(_fromUtf8("date"))
        self.verticalLayout.addWidget(self.date)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.widget_5 = QtGui.QWidget(self.centralwidget)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.widget_6 = QtGui.QWidget(self.widget_5)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget_3 = QtGui.QWidget(self.widget_6)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add = QtGui.QPushButton(self.widget_3)
        self.add.setObjectName(_fromUtf8("add"))
        self.horizontalLayout_2.addWidget(self.add)
        self.remove = QtGui.QPushButton(self.widget_3)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.horizontalLayout_2.addWidget(self.remove)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.subtotal = QtGui.QLabel(self.widget_3)
        self.subtotal.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subtotal.setFont(font)
        self.subtotal.setTextFormat(QtCore.Qt.AutoText)
        self.subtotal.setScaledContents(False)
        self.subtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subtotal.setObjectName(_fromUtf8("subtotal"))
        self.horizontalLayout_2.addWidget(self.subtotal)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.widget_6)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.import_2 = QtGui.QPushButton(self.widget_4)
        self.import_2.setObjectName(_fromUtf8("import_2"))
        self.horizontalLayout_3.addWidget(self.import_2)
        self.save = QtGui.QPushButton(self.widget_4)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout_3.addWidget(self.save)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.discount_label = QtGui.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.discount_label.setFont(font)
        self.discount_label.setObjectName(_fromUtf8("discount_label"))
        self.horizontalLayout_3.addWidget(self.discount_label)
        self.discount = QtGui.QLabel(self.widget_4)
        self.discount.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.discount.setFont(font)
        self.discount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.discount.setObjectName(_fromUtf8("discount"))
        self.horizontalLayout_3.addWidget(self.discount)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtGui.QWidget(self.widget_6)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.total = QtGui.QLabel(self.widget_2)
        self.total.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total.setFont(font)
        self.total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total.setObjectName(_fromUtf8("total"))
        self.horizontalLayout.addWidget(self.total)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Stunjelly Quote Calculator", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Stunjelly\n"
"80/82 Chiswick High Road\n"
"London\n"
"W4 1SY", None))
        self.date.setText(_translate("MainWindow", "Date", None))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Title", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Type", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Pages", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Panels", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Price", None))
        self.add.setText(_translate("MainWindow", "Add", None))
        self.remove.setText(_translate("MainWindow", "Remove", None))
        self.label_4.setText(_translate("MainWindow", "Sub-Total", None))
        self.subtotal.setText(_translate("MainWindow", "£0.00", None))
        self.import_2.setText(_translate("MainWindow", "Import CSV", None))
        self.save.setText(_translate("MainWindow", " Export to Excel ", None))
        self.discount_label.setText(_translate("MainWindow", "Discount", None))
        self.discount.setText(_translate("MainWindow", "£0.00", None))
        self.label.setText(_translate("MainWindow", "Total", None))
        self.total.setText(_translate("MainWindow", "£0.00", None))

import icons_rc
