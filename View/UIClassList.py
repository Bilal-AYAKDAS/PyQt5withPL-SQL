# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassList.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Classes(object):
    def setupUi(self, Classes):
        Classes.setObjectName("Classes")
        Classes.resize(539, 404)
        self.centralwidget = QtWidgets.QWidget(Classes)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_classid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_classid.setObjectName("txt_classid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_classid)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_teacher = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_teacher.setObjectName("txt_teacher")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_teacher)
        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(90, 70, 81, 28))
        self.btn_new.setObjectName("btn_new")
        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setGeometry(QtCore.QRect(0, 70, 81, 28))
        self.btn_view.setObjectName("btn_view")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(280, 70, 81, 28))
        self.btn_delete.setObjectName("btn_delete")
        self.tbl_classes = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_classes.setGeometry(QtCore.QRect(0, 120, 531, 241))
        self.tbl_classes.setObjectName("tbl_classes")
        self.tbl_classes.setColumnCount(0)
        self.tbl_classes.setRowCount(0)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(180, 70, 81, 28))
        self.btn_save.setObjectName("btn_save")
        Classes.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Classes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 26))
        self.menubar.setObjectName("menubar")
        Classes.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Classes)
        self.statusbar.setObjectName("statusbar")
        Classes.setStatusBar(self.statusbar)

        self.retranslateUi(Classes)
        QtCore.QMetaObject.connectSlotsByName(Classes)

    def retranslateUi(self, Classes):
        _translate = QtCore.QCoreApplication.translate
        Classes.setWindowTitle(_translate("Classes", "MainWindow"))
        self.label.setText(_translate("Classes", "Class ID"))
        self.label_2.setText(_translate("Classes", "Teacher ID"))
        self.btn_new.setText(_translate("Classes", "New"))
        self.btn_view.setText(_translate("Classes", "View"))
        self.btn_delete.setText(_translate("Classes", "Delete"))
        self.btn_save.setText(_translate("Classes", "Save"))
