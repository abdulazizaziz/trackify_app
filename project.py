from PyQt5 import QtCore, QtGui, QtWidgets


class Project:
    def __init__(self, scrollAreaWidgetContents, project_name: str, project_time: str, project_idol_time: str,
                 screen_shots: list, clicks: int, presses: int):
        self.project_name = project_name
        self.project_time = project_time
        self.project_idol_time = project_idol_time
        self.screen_shots = screen_shots
        self.clicks = clicks
        self.presses = presses
        _translate = QtCore.QCoreApplication.translate
        self.project_wgt = QtWidgets.QWidget(scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_wgt.sizePolicy().hasHeightForWidth())
        self.project_wgt.setSizePolicy(sizePolicy)
        self.project_wgt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.project_wgt.setStyleSheet("QWidget { \n"
                                       "    background:rgb(254,254,254); \n"
                                       "    color:black;\n"
                                       "    border: 1px solid rgb(179, 179, 179);\n"
                                       "    border-radius: 16px;\n"
                                       " }\n"
                                       "")
        self.project_wgt.setObjectName("self.project_wgt")
        horizontalLayout_8 = QtWidgets.QHBoxLayout(self.project_wgt)
        horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.project_selected_lbl = QtWidgets.QLabel(self.project_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_selected_lbl.sizePolicy().hasHeightForWidth())
        self.project_selected_lbl.setSizePolicy(sizePolicy)
        self.project_selected_lbl.setMinimumSize(QtCore.QSize(16, 0))
        self.project_selected_lbl.setStyleSheet("border:None")
        self.project_selected_lbl.setText("")
        self.project_selected_lbl.setObjectName("self.project_selected_lbl")
        horizontalLayout_8.addWidget(self.project_selected_lbl)
        self.project_name_lbl = QtWidgets.QLabel(self.project_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_name_lbl.sizePolicy().hasHeightForWidth())
        self.project_name_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.project_name_lbl.setFont(font)
        self.project_name_lbl.setObjectName("self.project_name_lbl")
        horizontalLayout_8.addWidget(self.project_name_lbl, 0, QtCore.Qt.AlignTop)
        self.project_time_lbl = QtWidgets.QLabel(self.project_wgt)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.project_time_lbl.setFont(font)
        self.project_time_lbl.setStyleSheet("border:None")
        self.project_time_lbl.setObjectName("self.project_time_lbl")
        horizontalLayout_8.addWidget(self.project_time_lbl)
        self.project_name_lbl.setStyleSheet(_translate("MainWindow", "border:None"))
        self.project_name_lbl.setText(_translate("MainWindow", f'{project_name}'))
        self.project_time_lbl.setText(_translate("MainWindow", self.project_time[:5]))

    def get_project_wgt(self):
        return self.project_wgt

    def get_project_selected_lbl(self):
        return self.project_selected_lbl

    def get_project_name(self):
        return self.project_name_lbl

    def get_project_time(self):
        return self.project_time_lbl
