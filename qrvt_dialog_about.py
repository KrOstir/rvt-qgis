# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrvt_dialog_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RvtAbout(object):
    def setupUi(self, RvtAbout):
        RvtAbout.setObjectName("RvtAbout")
        RvtAbout.resize(600, 700)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(RvtAbout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(RvtAbout)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(RvtAbout)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(RvtAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(240, 147))
        self.label_9.setMaximumSize(QtCore.QSize(240, 147))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("icon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(RvtAbout)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(RvtAbout)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(RvtAbout)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(RvtAbout)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(RvtAbout)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(RvtAbout)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.button_report_bug = QtWidgets.QPushButton(RvtAbout)
        self.button_report_bug.setObjectName("button_report_bug")
        self.horizontalLayout_3.addWidget(self.button_report_bug)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.button_close = QtWidgets.QPushButton(RvtAbout)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout_3.addWidget(self.button_close)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 5)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(RvtAbout)
        QtCore.QMetaObject.connectSlotsByName(RvtAbout)

    def retranslateUi(self, RvtAbout):
        _translate = QtCore.QCoreApplication.translate
        RvtAbout.setWindowTitle(_translate("RvtAbout", "RvtAbout"))
        self.label.setText(_translate("RvtAbout", "Relief Visualization Toolbox (RVT) QGIS plugin, ver. 0.3"))
        self.label_2.setText(_translate("RvtAbout", "<html><head/><body>\n"
"<span style=\" font-weight:600;\">○ By:</span>\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Žiga Kokalj\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Krištof Oštir\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Klemen Zakšek\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Peter Pehani\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Klemen Čotar\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Maja Somrak\n"
"\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Žiga Maroh (plugin author and maintainer)\n"
"<br>\n"
"<\\body>\n"
"<\\html>"))
        self.label_3.setText(_translate("RvtAbout", "<html><head/><body>\n"
"<span style=\" font-weight:600;\">○ Online resources:</span><br>\n"
"\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;• <a href=\"https://github.com/EarthObservation/rvt-qgis\"><span style=\" text-decoration: none; color:#0000ff;\">RVT QGIS plugin GitHub</span></a><br>\n"
"\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;• <a href=\"https://github.com/EarthObservation/RVT_py\"><span style=\" text-decoration: none; color:#0000ff;\">RVT core python library GitHub</span></a><br>\n"
"\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;• <a href=\"https://github.com/EarthObservation/rvt-arcgis-pro\"><span style=\" text-decoration: none; color:#0000ff;\">RVT ArcGIS Pro raster functions GitHub</span></a><br>\n"
"\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;• <a href=\"https://iaps.zrc-sazu.si/en/rvt#v\"><span style=\" text-decoration: none; color:#0000ff;\">Old RVT</span></a><br>\n"
"\n"
"<\\body>\n"
"<\\html>"))
        self.label_4.setText(_translate("RvtAbout", "<html><head/><body>\n"
"<span style=\" font-weight:600;\">○ License agreement:</span> <br>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;This software is distributed without any warranty and without even the implied warranty of merchantability or fitness \n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
" for a particulat pupose.\n"
"<br>\n"
"<\\body>\n"
"<\\html>"))
        self.label_5.setText(_translate("RvtAbout", "<html><head/><body><p><span style=\" font-weight:600;\">○ Acknowledgment:</span><br/>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"Development of RVT was partly financed by the European Commission\'s Culture Programme through \n"
"<br/>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"the ArchaeoLandscapes Europe project and by the Slovenian Research Agency core funding No. P2-0406,\n"
"<br/>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
" and by research projects No. J6-7085 and No. J6-9395. <br/></p></body></html>"))
        self.label_7.setText(_translate("RvtAbout", "<html><head/><body><p><span style=\" font-weight:600;\">○  Refrences:</span><br/>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"When using tools, please cite: <br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Kokalj, Ž., Somrak, M. 2019. Why Not a Single Image? Combining Visualizations to Facilitate Fieldwork and\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
" On-Screen Mapping. Remote Sensing 11(7): 747.\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Zakšek, K., Oštir, K., Kokalj, Ž. 2011. Sky-View Factor as a Relief Visualization Technique.\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
" Remote Sensing 3: 398-415.\n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"• Kokalj, Ž., Zakšek, K., Oštir, K. 2011. Application of Sky-View Factor for the Visualization of Historic Landscape \n"
"<br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"Features in Lidar-Derived Relief Models. Antiquity 85, 327: 263-273.\n"
"<br>\n"
"</body></html>"))
        self.label_8.setText(_translate("RvtAbout", "<html><head/><body><p><span style=\" font-weight:600;\">○ Bugs and Suggestions:</span><br/>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"Please report any bugs to <a href=\"https://github.com/EarthObservation/rvt-qgis/issues\"><span style=\" text-decoration: none; color:#0000ff;\">Issues</span></a> or to email: ziga.maroh@icloud.com\n"
"<br>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"Suggestions for improvments can be sent to email: ziga.kokalj@zrc-sazu.si\n"
"<br>\n"
"</body></html>"))
        self.label_6.setText(_translate("RvtAbout", "<html><head/><body><p><span style=\" font-weight:600;\">○ © Copyright:</span><br/>\n"
"&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
"Research Center of the Slovenian Academy of Sciences and Arts (ZRC SAZU) and <br>&#8203;&#32;&#8203;&#32;&#8203;&#32;&#8203;&#32;\n"
" University of Ljubljana, Faculty of civil and geodetic engineering (UL FGG), 2020\n"
"<br>\n"
"</body></html>"))
        self.button_report_bug.setText(_translate("RvtAbout", "Report a bug"))
        self.button_close.setText(_translate("RvtAbout", "Close"))
