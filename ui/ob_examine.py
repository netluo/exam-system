# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ob-examine.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.current_options = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.preButton = QtWidgets.QPushButton(self.centralwidget)
        self.preButton.setMaximumSize(QtCore.QSize(304, 16777215))
        self.preButton.setObjectName("preButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.preButton)
        self.horizontalLayout.addWidget(self.preButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.buttonGroup.addButton(self.nextButton)
        self.horizontalLayout.addWidget(self.nextButton)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncommit = QtWidgets.QAction(MainWindow)
        self.actioncommit.setObjectName("actioncommit")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionfrom_excel = QtWidgets.QAction(MainWindow)
        self.actionfrom_excel.setObjectName("actionfrom_excel")
        self.actionfrom_db = QtWidgets.QAction(MainWindow)
        self.actionfrom_db.setObjectName("actionfrom_db")
        self.actionfrom_qid = QtWidgets.QAction(MainWindow)
        self.actionfrom_qid.setObjectName("actionfrom_qid")
        self.menu_2.addAction(self.actionfrom_excel)
        self.menu_2.addAction(self.actionfrom_db)
        self.menu_2.addAction(self.actionfrom_qid)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actioncommit)
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())
        self.nextButton.setDisabled(True)
        self.preButton.setDisabled(True)

        self.radio_button_A = QtWidgets.QRadioButton()
        self.radio_button_B = QtWidgets.QRadioButton()
        self.radio_button_C = QtWidgets.QRadioButton()
        self.radio_button_D = QtWidgets.QRadioButton()
        self.radio_button_E = QtWidgets.QRadioButton()
        self.radio_button_F = QtWidgets.QRadioButton()
        self.radio_button_G = QtWidgets.QRadioButton()
        self.radio_button_dict = {'A': self.radio_button_A, 'B': self.radio_button_B, 'C': self.radio_button_C,
                                  'D': self.radio_button_D, 'E': self.radio_button_E, 'F': self.radio_button_F,
                                  'G': self.radio_button_G}
        self.checkBox_A = QtWidgets.QCheckBox()
        self.checkBox_B = QtWidgets.QCheckBox()
        self.checkBox_C = QtWidgets.QCheckBox()
        self.checkBox_D = QtWidgets.QCheckBox()
        self.checkBox_E = QtWidgets.QCheckBox()
        self.checkBox_F = QtWidgets.QCheckBox()
        self.checkBox_G = QtWidgets.QCheckBox()
        self.checkBox_H = QtWidgets.QCheckBox()
        self.checkBox_I = QtWidgets.QCheckBox()
        self.checkBox_J = QtWidgets.QCheckBox()

        self.checkBox_dict = {'A': self.checkBox_A, 'B': self.checkBox_B, 'C': self.checkBox_C, 'D': self.checkBox_D,
                              'E': self.checkBox_E, 'F': self.checkBox_F,
                              'G': self.checkBox_G, 'H': self.checkBox_H, 'I': self.checkBox_I, 'J': self.checkBox_J}

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionfrom_excel.triggered.connect(self.get_filename)
        self.actionexit.triggered.connect(self.close_all)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "题目自测系统"))
        self.preButton.setText(_translate("MainWindow", "Pre"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "打开"))
        self.actioncommit.setText(_translate("MainWindow", "提交"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionfrom_excel.setText(_translate("MainWindow", "从excel读取"))
        self.actionfrom_db.setText(_translate("MainWindow", "从数据库读取"))
        self.actionfrom_qid.setText(_translate("MainWindow", "查看错题"))

    def close_all(self):
        self.close()

    def get_filename(self):
        xls_name, _ = QFileDialog.getOpenFileName(None, '请选择文件', '', 'Excel文件(*.xls),Excel(*.xlsx)')
        return xls_name

    def add_question(self, q_dict: dict):
        # 按照不同的规则，添加选项
        # type :
        # 1 : 单选
        # 2 : 多选
        # 3 : 判断

        self.textBrowser.setText(q_dict['question'])
        self.options = self.add_options(q_dict['options'])
        self.current_options.clear()
        if q_dict['type'] == 1 or q_dict['type'] == 3:
            # 如果是单选或者多选，添加QRadioButton
            for key in self.options.keys():
                self.radio_button_dict[key].setChecked(False)
                self.radio_button_dict[key].setText("{}: ".format(key) + self.options[key])
                self.verticalLayout.addWidget(self.radio_button_dict[key])
                self.current_options.update({key: self.radio_button_dict[key]})
        if q_dict['type'] == 2:
            # 如果是多选，添加QCheckBox
            # 用exec动态生成对象名字（骚操作）
            for key in self.options.keys():
                # keys : 'A' 'B' ...
                self.checkBox_dict[key].setChecked(False)
                self.checkBox_dict[key].setText("{}: ".format(key) + self.options[key])
                self.verticalLayout.addWidget(self.checkBox_dict[key])
                self.current_options.update({key: self.checkBox_dict[key]})
        # print("addquestion:", self.current_options)  # addquestion: {'radio_button_A': 'A', 'radio_button_B': 'B'}

    def add_options(self, options: list):
        options_dict = {}
        # char_ascii 代表 A
        char_ascii = 97
        for idx_option in range(len(options)):
            options_dict.update({chr(char_ascii).upper(): options[idx_option]})
            char_ascii += 1
        # print(options_dict)     # {'A': '正确', 'B': '错误'}
        return options_dict

    def emit_widget_name(self):
        self.qid_list_done = []
        print(self.qid_list_done)
