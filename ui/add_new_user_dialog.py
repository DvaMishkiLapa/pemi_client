# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\add_new_user_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_new_user_dialog(object):
    def setupUi(self, add_new_user_dialog):
        add_new_user_dialog.setObjectName("add_new_user_dialog")
        add_new_user_dialog.resize(350, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_new_user_dialog.sizePolicy().hasHeightForWidth())
        add_new_user_dialog.setSizePolicy(sizePolicy)
        add_new_user_dialog.setMinimumSize(QtCore.QSize(350, 275))
        add_new_user_dialog.setMaximumSize(QtCore.QSize(350, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_new_user_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(add_new_user_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_error = QtWidgets.QLabel(add_new_user_dialog)
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 4, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.input_data_box = QtWidgets.QGroupBox(add_new_user_dialog)
        self.input_data_box.setAutoFillBackground(False)
        self.input_data_box.setTitle("")
        self.input_data_box.setFlat(True)
        self.input_data_box.setCheckable(False)
        self.input_data_box.setObjectName("input_data_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.input_data_box)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_pwd = QtWidgets.QLabel(self.input_data_box)
        self.label_pwd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout_2.addWidget(self.label_pwd, 8, 0, 1, 1)
        self.label_pos = QtWidgets.QLabel(self.input_data_box)
        self.label_pos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_pos.setObjectName("label_pos")
        self.gridLayout_2.addWidget(self.label_pos, 7, 0, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_2.addWidget(self.lineEdit_email, 1, 1, 1, 1)
        self.label_email = QtWidgets.QLabel(self.input_data_box)
        self.label_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_email.setObjectName("label_email")
        self.gridLayout_2.addWidget(self.label_email, 1, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 5, 1, 1, 1)
        self.lineEdit_patron = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_patron.setText("")
        self.lineEdit_patron.setObjectName("lineEdit_patron")
        self.gridLayout_2.addWidget(self.lineEdit_patron, 6, 1, 1, 1)
        self.lineEdit_surname = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.gridLayout_2.addWidget(self.lineEdit_surname, 4, 1, 1, 1)
        self.label_confpowd = QtWidgets.QLabel(self.input_data_box)
        self.label_confpowd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_confpowd.setObjectName("label_confpowd")
        self.gridLayout_2.addWidget(self.label_confpowd, 9, 0, 1, 1)
        self.label_patron = QtWidgets.QLabel(self.input_data_box)
        self.label_patron.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_patron.setObjectName("label_patron")
        self.gridLayout_2.addWidget(self.label_patron, 6, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.input_data_box)
        self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 5, 0, 1, 1)
        self.lineEdit_confpwd = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_confpwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_confpwd.setText("")
        self.lineEdit_confpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confpwd.setObjectName("lineEdit_confpwd")
        self.gridLayout_2.addWidget(self.lineEdit_confpwd, 9, 1, 1, 1)
        self.label_surname = QtWidgets.QLabel(self.input_data_box)
        self.label_surname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_surname.setObjectName("label_surname")
        self.gridLayout_2.addWidget(self.label_surname, 4, 0, 1, 1)
        self.lineEdit_pos = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_pos.setObjectName("lineEdit_pos")
        self.gridLayout_2.addWidget(self.lineEdit_pos, 7, 1, 1, 1)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.input_data_box)
        self.lineEdit_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_pwd.setText("")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout_2.addWidget(self.lineEdit_pwd, 8, 1, 1, 1)
        self.gridLayout.addWidget(self.input_data_box, 1, 0, 1, 3)
        self.label_dialog_newuser = QtWidgets.QLabel(add_new_user_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dialog_newuser.sizePolicy().hasHeightForWidth())
        self.label_dialog_newuser.setSizePolicy(sizePolicy)
        self.label_dialog_newuser.setObjectName("label_dialog_newuser")
        self.gridLayout.addWidget(self.label_dialog_newuser, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(add_new_user_dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)
        self.cancel_button = QtWidgets.QPushButton(add_new_user_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 2, 2, 1, 1)
        self.add_button = QtWidgets.QPushButton(add_new_user_dialog)
        self.add_button.setEnabled(True)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 2, 1, 1, 1)

        self.retranslateUi(add_new_user_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_new_user_dialog)
        add_new_user_dialog.setTabOrder(self.lineEdit_email, self.lineEdit_surname)
        add_new_user_dialog.setTabOrder(self.lineEdit_surname, self.lineEdit_name)
        add_new_user_dialog.setTabOrder(self.lineEdit_name, self.lineEdit_patron)
        add_new_user_dialog.setTabOrder(self.lineEdit_patron, self.lineEdit_pos)
        add_new_user_dialog.setTabOrder(self.lineEdit_pos, self.lineEdit_pwd)
        add_new_user_dialog.setTabOrder(self.lineEdit_pwd, self.lineEdit_confpwd)
        add_new_user_dialog.setTabOrder(self.lineEdit_confpwd, self.add_button)
        add_new_user_dialog.setTabOrder(self.add_button, self.cancel_button)

    def retranslateUi(self, add_new_user_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_new_user_dialog.setWindowTitle(_translate("add_new_user_dialog", "Добавление пользователя"))
        self.label_pwd.setText(_translate("add_new_user_dialog", "Пароль:"))
        self.label_pos.setText(_translate("add_new_user_dialog", "Должность:"))
        self.label_email.setText(_translate("add_new_user_dialog", "Email:"))
        self.label_confpowd.setText(_translate("add_new_user_dialog", "Подтверждение пароля:"))
        self.label_patron.setText(_translate("add_new_user_dialog", "Отчество:"))
        self.label_name.setText(_translate("add_new_user_dialog", "Имя:"))
        self.label_surname.setText(_translate("add_new_user_dialog", "Фамилия:"))
        self.label_dialog_newuser.setText(_translate("add_new_user_dialog", "Введите данные во всех полях"))
        self.cancel_button.setText(_translate("add_new_user_dialog", "Отмена"))
        self.add_button.setText(_translate("add_new_user_dialog", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_new_user_dialog = QtWidgets.QDialog()
    ui = Ui_add_new_user_dialog()
    ui.setupUi(add_new_user_dialog)
    add_new_user_dialog.show()
    sys.exit(app.exec_())

