# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 593)
        MainWindow.setStyleSheet("#logoFrame {\n"
"    image: url(:/icon/icon/key-48.ico);\n"
"    border-bottom: 1px solid #fff;\n"
"}\n"
"\n"
"/* Style for menu widget  */\n"
"#menuWidget {\n"
"    background-color: #353535;\n"
"}\n"
"\n"
"/* Style for QPushButton in menu widget  */\n"
"#menuWidget QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 15px;\n"
"    border: none;\n"
"    background-color: #fff;\n"
"    font-size: 14px;\n"
"    border: 5px solid #353535;\n"
"    height: 25px;\n"
"}\n"
"\n"
"#menuWidget QPushButton:hover {\n"
"    background-color: #e3e3e3;\n"
"}\n"
"\n"
"\n"
"#menuWidget QPushButton:checked {\n"
"    background-color: #0055ff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* Style for main widget */\n"
"#stackedWidget {\n"
"    background-color: #f4f5f8;\n"
"}\n"
"\n"
"/* Style for QLabel in main widget */\n"
"#stackedWidget QLabel {\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"/* Style for QLineEdit and QSpinBox in main widget */\n"
"#stackedWidget QLineEdit, #stackedWidget QSpinBox {\n"
"    border: 1px solid #353535;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* style for  QSpinBox*/\n"
"#stackedWidget QSpinBox::up-arrow {\n"
"    image: url(:/icon/icon/arrow-146-48.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-arrow {\n"
"    image: url(:/icon/icon/arrow-208-48.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button, \n"
"#stackedWidget QSpinBox::up-button {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button:hover, \n"
"#stackedWidget QSpinBox::up-button:hover {\n"
"    background-color: rgb(176, 176, 176);\n"
"}\n"
"\n"
"#stackedWidget QSpinBox::down-button:pressed, \n"
"#stackedWidget QSpinBox::up-button:pressed {\n"
"    background-color: rgb(78, 88, 121);\n"
"}\n"
"\n"
"/* Style for QPushButton in main widget */\n"
"#stackedWidget QPushButton {\n"
"    border: none;\n"
"    font-size: 16px;\n"
"    border-radius: 3px;\n"
"    color: #fff;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"#stackedWidget QPushButton:pressed {\n"
"    padding-left: 20px;\n"
"}\n"
"\n"
"/* Style for sepcial QPushButton in main widget */\n"
"#confEditBtn,\n"
"#generateCopyBtn, \n"
"#generateRestBtn,\n"
"#showSearchBtn\n"
"{\n"
"    background-color: #3554d1;\n"
"}\n"
"\n"
"#confEditBtn:hover, #confEditBtn:pressed, \n"
"#generateCopyBtn:hover,  #generateCopyBtn:pressed, \n"
"#generateRestBtn:hover,  #generateRestBtn:pressed, \n"
"#showSearchBtn:hover,  #showSearchBtn:pressed \n"
"{\n"
"    background-color: #0000ff;\n"
"}\n"
"\n"
"#confSaveBtn,\n"
"#generateSaveBtn, \n"
"#generateCreateBtn\n"
"{\n"
"    background-color: #00aa7f;\n"
"}\n"
"\n"
"#confSaveBtn:hover, #confSaveBtn:pressed, \n"
"#generateSaveBtn:hover, #generateSaveBtn:pressed,\n"
"#generateCreateBtn:hover, #generateCreateBtn:pressed \n"
"{\n"
"    background-color: #00aa00;\n"
"}\n"
"\n"
"#confRefreshBtn,\n"
" #showRefreshBtn\n"
"{\n"
"    background-color: #E59866;\n"
"}\n"
"\n"
"\n"
"#confRefreshBtn:hover, #confRefreshBtn:pressed, \n"
"#showRefreshBtn:hover, #showRefreshBtn:pressed\n"
"{\n"
"    background-color: #DC7633;\n"
"}\n"
"\n"
"/* Style for QCheckBox in main widget */\n"
"QCheckBox {\n"
"    spacing: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icon/icon/checkbox_unchecked.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icon/icon/checkbox_checked.ico);\n"
"}\n"
"\n"
"\n"
"/* Style for QFrame */\n"
"#resultFrame {\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"/* Style for QTableWidget */\n"
"#tableWidget QHeaderView, #tableWidget   {\n"
"    border:0px;\n"
"    background-color:  #fff;\n"
"    border-radius:5px;\n"
"    text-align:left;\n"
"}\n"
"\n"
"#tableWidget QHeaderView::section{\n"
"    font-family:\"Times New Roman\", \"Times\", \"serif\";\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    text-align:left;\n"
"    border-radius:14px;\n"
"    border-bottom:1px solid #353535;\n"
"    border-top:1px solid #353535;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"#tableWidget::item:selected {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#tableWidget::item{\n"
"    border-bottom:1px solid #d0c6ff;\n"
"    padding-left: 10px;\n"
"    color: black;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.menuWidget = QtWidgets.QWidget(self.centralwidget)
        self.menuWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.menuWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.menuWidget.setObjectName("menuWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logoFrame = QtWidgets.QFrame(self.menuWidget)
        self.logoFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.logoFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.logoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoFrame.setObjectName("logoFrame")
        self.verticalLayout.addWidget(self.logoFrame)
        self.pushButton = QtWidgets.QPushButton(self.menuWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/key-4-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/key-4-48-checked.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.menuWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 35))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/generic-text-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/generic-text-48-checked.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.menuWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 35))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/data-configuration-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/data-configuratio-checkedn-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 574, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.exitBtn = QtWidgets.QPushButton(self.menuWidget)
        self.exitBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.exitBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        self.exitBtn.setStyleSheet("#exitBtn {\n"
"    color: #943e3e;\n"
"    text-align: center;\n"
"    padding-left: 0;\n"
"}\n"
"\n"
"#exitBtn:pressed {\n"
"    padding-left: 10px;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/logout-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exitBtn.setIcon(icon3)
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.gridLayout.addWidget(self.menuWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.showRefreshBtn = QtWidgets.QPushButton(self.page)
        self.showRefreshBtn.setMinimumSize(QtCore.QSize(150, 32))
        self.showRefreshBtn.setMaximumSize(QtCore.QSize(150, 32))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/redo-5-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showRefreshBtn.setIcon(icon4)
        self.showRefreshBtn.setObjectName("showRefreshBtn")
        self.gridLayout_3.addWidget(self.showRefreshBtn, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.showSearchBtn = QtWidgets.QPushButton(self.page)
        self.showSearchBtn.setMinimumSize(QtCore.QSize(150, 32))
        self.showSearchBtn.setMaximumSize(QtCore.QSize(150, 32))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/search-7-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showSearchBtn.setIcon(icon5)
        self.showSearchBtn.setObjectName("showSearchBtn")
        self.gridLayout_3.addWidget(self.showSearchBtn, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.resultFrame = QtWidgets.QFrame(self.page)
        self.resultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame.setObjectName("resultFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.resultFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.resultFrame)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.resultFrame, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_6.setContentsMargins(100, 50, 100, -1)
        self.gridLayout_6.setVerticalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.generateRestBtn = QtWidgets.QPushButton(self.page_2)
        self.generateRestBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.generateRestBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        self.generateRestBtn.setIcon(icon4)
        self.generateRestBtn.setObjectName("generateRestBtn")
        self.gridLayout_6.addWidget(self.generateRestBtn, 2, 0, 1, 1)
        self.generateCopyBtn = QtWidgets.QPushButton(self.page_2)
        self.generateCopyBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.generateCopyBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/copy-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateCopyBtn.setIcon(icon6)
        self.generateCopyBtn.setObjectName("generateCopyBtn")
        self.gridLayout_6.addWidget(self.generateCopyBtn, 4, 0, 1, 1)
        self.generatePWLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.generatePWLineEdit.setStyleSheet("#generatePWLineEdit {\n"
"    background-color: #fff;\n"
"    font-size: 30px;\n"
"    border: none;\n"
"}")
        self.generatePWLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.generatePWLineEdit.setReadOnly(True)
        self.generatePWLineEdit.setObjectName("generatePWLineEdit")
        self.gridLayout_6.addWidget(self.generatePWLineEdit, 3, 0, 1, 2)
        self.generateCreateBtn = QtWidgets.QPushButton(self.page_2)
        self.generateCreateBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.generateCreateBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/pressure-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateCreateBtn.setIcon(icon7)
        self.generateCreateBtn.setObjectName("generateCreateBtn")
        self.gridLayout_6.addWidget(self.generateCreateBtn, 2, 1, 1, 1)
        self.generateSaveBtn = QtWidgets.QPushButton(self.page_2)
        self.generateSaveBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.generateSaveBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/save-128.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generateSaveBtn.setIcon(icon8)
        self.generateSaveBtn.setObjectName("generateSaveBtn")
        self.gridLayout_6.addWidget(self.generateSaveBtn, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkBox = QtWidgets.QCheckBox(self.page_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setProperty("value", 8)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(744, 426, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 5, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setContentsMargins(100, 50, 100, -1)
        self.gridLayout_8.setVerticalSpacing(20)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setHorizontalSpacing(10)
        self.gridLayout_7.setVerticalSpacing(20)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_7.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_7.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_7.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_7.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 3)
        self.confEditBtn = QtWidgets.QPushButton(self.page_3)
        self.confEditBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.confEditBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/edit-property-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confEditBtn.setIcon(icon9)
        self.confEditBtn.setObjectName("confEditBtn")
        self.gridLayout_8.addWidget(self.confEditBtn, 1, 0, 1, 1)
        self.confRefreshBtn = QtWidgets.QPushButton(self.page_3)
        self.confRefreshBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.confRefreshBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        self.confRefreshBtn.setIcon(icon4)
        self.confRefreshBtn.setObjectName("confRefreshBtn")
        self.gridLayout_8.addWidget(self.confRefreshBtn, 1, 1, 1, 1)
        self.confSaveBtn = QtWidgets.QPushButton(self.page_3)
        self.confSaveBtn.setMinimumSize(QtCore.QSize(0, 32))
        self.confSaveBtn.setMaximumSize(QtCore.QSize(16777215, 32))
        self.confSaveBtn.setIcon(icon8)
        self.confSaveBtn.setObjectName("confSaveBtn")
        self.gridLayout_8.addWidget(self.confSaveBtn, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 508, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Password Saved"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Configuration"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.showRefreshBtn.setText(_translate("MainWindow", "Refresh"))
        self.label_2.setText(_translate("MainWindow", "Website"))
        self.showSearchBtn.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Website"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Operation"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.generateRestBtn.setText(_translate("MainWindow", "Reset"))
        self.generateCopyBtn.setText(_translate("MainWindow", "Copy"))
        self.generatePWLineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.generateCreateBtn.setText(_translate("MainWindow", "Generate Password"))
        self.generateSaveBtn.setText(_translate("MainWindow", "Save"))
        self.checkBox.setText(_translate("MainWindow", "Uppercase"))
        self.checkBox_2.setText(_translate("MainWindow", "Numbers"))
        self.checkBox_3.setText(_translate("MainWindow", "Special Characters"))
        self.label_3.setText(_translate("MainWindow", "Website"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Length"))
        self.label_6.setText(_translate("MainWindow", "Lowercase"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "abcdefghijklmnopqrstuvwxyz"))
        self.label_7.setText(_translate("MainWindow", "Uppercase"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.label_8.setText(_translate("MainWindow", "Numbers"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "1234567890"))
        self.label_9.setText(_translate("MainWindow", "Special Characters"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "@#$%&^!"))
        self.confEditBtn.setText(_translate("MainWindow", "Edit"))
        self.confRefreshBtn.setText(_translate("MainWindow", "Refresh"))
        self.confSaveBtn.setText(_translate("MainWindow", "Save"))
from static import resource_rc
