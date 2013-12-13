# -*- coding: utf-8 -*-
import os, sys
from PyQt4 import QtCore, QtGui
from windowUi import Ui_MainWindow
from addUi import Ui_Dialog
import csv
import urllib
import urllib2

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self._dialog = None



		# Flat
		self.c1prep = 45
		self.c1ppg = 0.3
		# Complex
		self.c2prep = 45
		self.c2ppg = 0.5
		# Comic
		self.c3prep = 45
		self.c3ppg = 0.00
		self.c3ppl = 0.30

		self.ui.add.clicked.connect(self.AddBook)
		self.ui.remove.clicked.connect(self.RemoveBook)
		self.ui.recalc.clicked.connect(self.reCalc)
		self.ui.save.clicked.connect(self.Export)

		self.ui.treeWidget.setColumnWidth(0, 300)
		self.ui.treeWidget.setColumnWidth(1, 120)
		self.ui.treeWidget.setColumnWidth(2, 80)
		self.ui.treeWidget.setColumnWidth(3, 80)
		self.ui.treeWidget.setColumnWidth(4, 80)

	def Export(self):
		root = self.ui.treeWidget.invisibleRootItem()
		child_count = root.childCount()
		data = [['Title', 'Type', 'Pages', 'Panels', 'Price']]
		for i in range(child_count):
			item = root.child(i)
			data.append([str(item.text(0)), str(item.text(1)), str(item.text(2)), str(item.text(3)), str(item.text(4))])
		print data
		with open('test.csv', 'w') as fp:
			a = csv.writer(fp, delimiter=',')
			a.writerows(data)

	def AddBook(self):
		root = self.ui.treeWidget.invisibleRootItem()
		child_count = root.childCount()
		if child_count < 20:
			self.new_book = Add(self)
			self.new_book.show()

	def RemoveBook(self):
		self.ui.treeWidget.takeTopLevelItem(self.ui.treeWidget.indexOfTopLevelItem(self.ui.treeWidget.currentItem()))
		self.reCalc()

	def handleOpenDialog(self):
		if self._dialog is None:
			self._dialog = QtGui.QDialog(self)
			self._dialog.resize(200, 100)
		self._dialog.show()

	def reCalc(self):
		min_amount_for_discount = 10.0
		max_available_for_discount = 20.0

		discount_percentage_min = 5.0
		discount_percentage_max = 20.0

		off = 0.0

		total = float(0.00)
		discount = float(0.00)
		root = self.ui.treeWidget.invisibleRootItem()
		child_count = root.childCount()
		for i in range(child_count):
			item = root.child(i)
			total += float(item.text(4))
		self.ui.subtotal.setText(u'£' + str("%.2f" % round(total, 2)))
		root = self.ui.treeWidget.invisibleRootItem()
		if child_count > min_amount_for_discount:
			# Discounts!
			percentage = min((float((child_count - min_amount_for_discount)) / float((max_available_for_discount - min_amount_for_discount))), 1)
			discount = (percentage * (discount_percentage_max - discount_percentage_min)) + discount_percentage_min
			print percentage, discount
			off = total * (discount/100)
			self.ui.discount_label.setText('Discount (' + str(round(discount)) + '%)')
			self.ui.discount.setText(u'£-'+ str("%.2f" % round(off, 2)))
		self.ui.total.setText(u'£' + str("%.2f" % round(total-round(off), 2)))


class Add(QtGui.QDialog):
	def __init__(self, main):
		QtGui.QDialog.__init__(self)
		# This is always the same
		self.addui = Ui_Dialog()
		self.addui.setupUi(self)
		self.m = main


		root = self.m.ui.treeWidget.invisibleRootItem()
		child_count = root.childCount()
		self.addui.title.setText("Book " + str(child_count+1))

	def accept(self):
		if self.addui.pages.value() > -1:
			new = Book()
			new.title = self.addui.title.text()
			new.type = self.addui.type.currentIndex()
			new.pages = self.addui.pages.value()
			new.panels = self.addui.panels.value()

			item = QtGui.QTreeWidgetItem()
			item.setText(0, new.title)
			cost = float(000.00)
			if new.type == 0:
				# Fixed Layout EPUB3 (FLAT)
				item.setText(1, self.addui.type.itemText(0))
				cost = self.m.c1prep + (new.pages * self.m.c1ppg)
			elif new.type == 1:
				# Fixed Layout EPUB3 (COMPLEX)
				item.setText(1, self.addui.type.itemText(1))
				cost = self.m.c2prep + (new.pages * self.m.c2ppg)
			elif new.type == 2:
				# Amazon KF8 Comic (COMIC)
				item.setText(1, self.addui.type.itemText(2))
				cost = self.m.c3prep + (new.pages * self.m.c3ppg) + (new.panels * self.m.c3ppl)
			item.setText(2, str(new.pages))
			item.setText(3, str(new.panels))
			item.setText(4, str("%.2f" % round(cost, 2)))
			self.m.ui.treeWidget.addTopLevelItem(item)
			self.m.ui.treeWidget.repaint()
			self.m.reCalc()
			self.hide()
		else:
			print "Pages much be greater than 1"


class Book(object):
	title = ''
	type = ''
	pages = 0
	panels = 0

	def __init__(self):
		pass


def main():
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()