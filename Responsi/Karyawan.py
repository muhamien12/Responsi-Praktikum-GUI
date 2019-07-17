

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit, QMessageBox


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 350)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 40, 341, 247))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName ("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)


        self.verticalLayout.addWidget(self.pushButton_7)
        #self.verticalLayout.addWidget(self.pushButton_8)
        self.horizontalLayout.addLayout(self.verticalLayout)


        self.pushButton.clicked.connect (self.Add)
        self.pushButton_2.clicked.connect (self.Edit)
        self.pushButton_3.clicked.connect (self.Remove)
        self.pushButton_4.clicked.connect (self.Up)
        self.pushButton_5.clicked.connect (self.Down)
        self.pushButton_6.clicked.connect (self.Sort)
        self.pushButton_7.clicked.connect (self.Close)
        self.pushButton_8.clicked.connect (self.Clear)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Karyawan()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Karyawan"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Edit"))
        self.pushButton_3.setText(_translate("Dialog", "Remove"))
        self.pushButton_4.setText(_translate("Dialog", "Up"))
        self.pushButton_5.setText(_translate("Dialog", "Down"))
        self.pushButton_6.setText(_translate("Dialog", "Sort"))
        self.pushButton_7.setText(_translate("Dialog", "Close"))
        self.pushButton_8.setText(_translate("Dialog", "Clear"))
    def Karyawan(self):
        self.Karyawan = ["Bambang", "Parjo"]
        self.listWidget.addItems(self.Karyawan)
        self.listWidget.setCurrentRow(0)

    def Add(self):
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText (self, "Karyawan Dialog","Masukan Nama Karyawan")

        if ok and text is not None:
            self.listWidget.insertItem(row, text)

    def Edit (self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is not None:
            string, ok = QInputDialog.getText (self, "Karyawan Dialog", "Edit Nama Karyawan", QLineEdit.Normal, item.text())

            if ok and string is not None:
                item.setText (string)

    def Remove (self):
        row = self.listWidget.currentRow ()
        item = self.listWidget.item (row)

        if item is None:
            return

        reply = QMessageBox.question(self, "Hapus Karyawan", "Apakah Anda Ingin Menghapus Karyawan " +str(item.text()),
                                        QMessageBox.Yes | QMessageBox.No )

        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem (row)
            del item



    def Up (self):
        row = self.listWidget.currentRow ()

        if row >=1 :
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row -1, item)
            self.listWidget.setCurrentItem (item)

    def Down(self):
        row = self.listWidget.currentRow ()

        if row < self.listWidget.count () -1 :
                item = self.listWidget.takeItem(row)
                self.listWidget.insertItem(row +1, item)
                self.listWidget.setCurrentItem (item)

    def Sort(self):
        self.listWidget.sortItems ()

    def Clear(self):
        self.listWidget. clear ()

    def Close(self):
        quit ()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
