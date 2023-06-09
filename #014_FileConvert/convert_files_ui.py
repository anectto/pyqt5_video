# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Projects/FileConvert\convert_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/static/refresh-128 #4169E1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/* Style for QComoBox \n"
"    ============================================== START */\n"
"QComboBox {\n"
"    border: none;\n"
"    min-height:26px;\n"
"    border-radius: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 5px;\n"
"    border: 2px solid #fff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/static/arrow-208-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"     border: 2px solid #E59866;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"    border:1px solid rgba(0,0,0,10%);\n"
"    padding:5px;\n"
"    background: transparent;\n"
"    background-color: #FFFFFF;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    padding:5px;\n"
"    background-color:#FFFFFF;\n"
"}\n"
"\n"
"QComboBox::item:hover,\n"
"QComboBox::item:selected\n"
"{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"/* Style for QComoBox\n"
"     ==============================================  END */\n"
"\n"
"/* Style for special QFrame \n"
"     ============================================== START */\n"
"#frame {\n"
"    border-image: url(:/imgs/static/mountains-gfcb2d4ac0_1920.jpg);\n"
"}\n"
"\n"
"#warning_frame {\n"
"    border-radius: 5px;\n"
"    background: #FDFEFE;\n"
"}\n"
"/* Style for special QFrame  \n"
"    =============================================== END */\n"
"\n"
"/* Style for QPushButton\n"
"     ============================================== START */\n"
"QPushButton {\n"
"    border: 5px solid #fff;\n"
"    border-radius: 5px;\n"
"    border: 4px solid #F9E79F;\n"
"    padding: 1px 5px;\n"
"    min-width: 120px;\n"
"    min-height:20px;\n"
"    background-color: #F9E79F;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F4D03F;\n"
"    border-color: #F4D03F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #FEF9E7;\n"
"}\n"
"/* Style for QPushButton\n"
"     ============================================== END */\n"
"\n"
"/* Style for QLineEdit\n"
"     ============================================= START */\n"
"QLineEdit  {\n"
"    border: none;\n"
"    min-height:26px;\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border:  2px solid #fff;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:  2px solid #E59866;\n"
"}\n"
"/* Style for QLineEdit\n"
"     ============================================== END */\n"
"\n"
"/* Style for QCheckBox\n"
"     ============================================= START */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 14px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/static/square-rounded-64 #fff.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/static/check-mark-8-64 #42c0fb.ico);\n"
"}\n"
"/* Style for QCheckBox\n"
"     ============================================== END */\n"
"\n"
"/* Style for QLabel\n"
"     ============================================= START */\n"
"QLabel {\n"
"    color: #A00101;\n"
"}\n"
"\n"
"#result_count {\n"
"    color: #fff;\n"
"    font-size: 12px;\n"
"}\n"
"/* Style for QLabel\n"
"     ============================================== END */\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.warning_frame = QtWidgets.QFrame(self.frame_2)
        self.warning_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.warning_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.warning_frame.setObjectName("warning_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.warning_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.warning_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.warning_frame, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/static/python-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/static/sinchronize-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 10, -1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        self.checkBox.setFont(font)
        self.checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.result_count = QtWidgets.QLabel(self.frame)
        self.result_count.setText("")
        self.result_count.setObjectName("result_count")
        self.horizontalLayout.addWidget(self.result_count)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/static/folder-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convert Ui File to Py File"))
        self.groupBox.setTitle(_translate("MainWindow", "Files list"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Convert Version"))
        self.comboBox.setItemText(1, _translate("MainWindow", "PyQt6"))
        self.comboBox.setItemText(2, _translate("MainWindow", "PyQt5"))
        self.comboBox.setItemText(3, _translate("MainWindow", "PySide6"))
        self.comboBox.setItemText(4, _translate("MainWindow", "PySide2"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Convert"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset Settings"))
        self.checkBox.setText(_translate("MainWindow", "UI files"))
        self.checkBox_2.setText(_translate("MainWindow", "Resource files"))
        self.pushButton.setText(_translate("MainWindow", "Selected Path"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Convert folder path"))
import resource_rc
