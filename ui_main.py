# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUzkVuH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 176)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.extraxt_link_btn = QPushButton(self.frame_2)
        self.extraxt_link_btn.setObjectName(u"extraxt_link_btn")

        self.horizontalLayout_2.addWidget(self.extraxt_link_btn)

        self.stop_link_btn = QPushButton(self.frame_2)
        self.stop_link_btn.setObjectName(u"stop_link_btn")

        self.horizontalLayout_2.addWidget(self.stop_link_btn)

        self.clk_links_btn = QPushButton(self.frame_2)
        self.clk_links_btn.setObjectName(u"clk_links_btn")

        self.horizontalLayout_2.addWidget(self.clk_links_btn)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 676, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extraxt_link_btn.setText(QCoreApplication.translate("MainWindow", u"Extract Links", None))
        self.stop_link_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.clk_links_btn.setText(QCoreApplication.translate("MainWindow", u"Click Links", None))
    # retranslateUi

