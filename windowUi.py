# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Dec 13 14:46:04 2013
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(707, 459)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add = QtGui.QPushButton(self.widget_3)
        self.add.setObjectName(_fromUtf8("add"))
        self.horizontalLayout_2.addWidget(self.add)
        self.remove = QtGui.QPushButton(self.widget_3)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.horizontalLayout_2.addWidget(self.remove)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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
        self.subtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subtotal.setObjectName(_fromUtf8("subtotal"))
        self.horizontalLayout_2.addWidget(self.subtotal)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.centralwidget)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.save = QtGui.QPushButton(self.widget)
        self.save.setObjectName(_fromUtf8("save"))
        self.gridLayout.addWidget(self.save, 0, 5, 1, 1)
        self.recalc = QtGui.QPushButton(self.widget)
        self.recalc.setObjectName(_fromUtf8("recalc"))
        self.gridLayout.addWidget(self.recalc, 0, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Stunjelly Quote Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Panels", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.remove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Sub-Total", None, QtGui.QApplication.UnicodeUTF8))
        self.subtotal.setText(QtGui.QApplication.translate("MainWindow", "£0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.discount_label.setText(QtGui.QApplication.translate("MainWindow", "Discount", None, QtGui.QApplication.UnicodeUTF8))
        self.discount.setText(QtGui.QApplication.translate("MainWindow", "-£0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.total.setText(QtGui.QApplication.translate("MainWindow", "£0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("MainWindow", " Export to Excel ", None, QtGui.QApplication.UnicodeUTF8))
        self.recalc.setText(QtGui.QApplication.translate("MainWindow", "Recalculate Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Stunjelly eBook Conversion Calculator", None, QtGui.QApplication.UnicodeUTF8))

