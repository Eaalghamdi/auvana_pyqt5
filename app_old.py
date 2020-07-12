# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_software_page_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import sys
import os

from auvanaWidget import (VideoWindow, Canvas, pandasModel)
from functions.videoAnalysis import VideoAnalysis
from frame_extraction import frameExtraction
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s): return s

df = pd.DataFrame({'a': ['Mary', 'Jim', 'John'],
                   'b': [100, 200, 300],
                   'c': ['a', 'b', 'c']})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1240, 699)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setTabletTracking(True)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.Frame_extraction_tab = QtWidgets.QWidget()
        self.Frame_extraction_tab.setObjectName("Frame_extraction_tab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.Frame_extraction_tab)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.w1_ui1_frame = QtWidgets.QFrame(self.Frame_extraction_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w1_ui1_frame.sizePolicy().hasHeightForWidth())
        self.w1_ui1_frame.setSizePolicy(sizePolicy)
        self.w1_ui1_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.w1_ui1_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.w1_ui1_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.w1_ui1_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.w1_ui1_frame.setObjectName("w1_ui1_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.w1_ui1_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.w1_ui1_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # use an instance of videowindow class and add it to the layout
        self.myVideo = VideoWindow()
        # self.myVideo.setFixedWidth(600 + 40)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.myVideo.sizePolicy().hasHeightForWidth())
        self.myVideo.setSizePolicy(sizePolicy)
        self.myVideo.setMinimumSize(QtCore.QSize(0, 0))
        self.myVideo.setMaximumSize(QtCore.QSize(570, 400))
        self.gridLayout_4.addWidget(self.myVideo, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        # self.graphicsView = QtWidgets.QGraphicsView(self.frame_3)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        # self.graphicsView.setSizePolicy(sizePolicy)
        # self.graphicsView.setMinimumSize(QtCore.QSize(540, 0))
        # self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.graphicsView.setInteractive(True)
        # self.graphicsView.setObjectName("graphicsView")
        # self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
        # self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.option_frame = QtWidgets.QFrame(self.w1_ui1_frame)
        self.option_frame.setMinimumSize(QtCore.QSize(500, 0))
        self.option_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.option_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_frame.setObjectName("option_frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.option_frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label = QtWidgets.QLabel(self.option_frame)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_extraxtion_groupBox = QtWidgets.QGroupBox(self.option_frame)
        self.frame_extraxtion_groupBox.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_extraxtion_groupBox.setFont(font)
        self.frame_extraxtion_groupBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_extraxtion_groupBox.setFlat(False)
        self.frame_extraxtion_groupBox.setObjectName(
            "frame_extraxtion_groupBox")
        self.gridLayout_22 = QtWidgets.QGridLayout(
            self.frame_extraxtion_groupBox)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.shot_bt = QtWidgets.QRadioButton(self.frame_extraxtion_groupBox)
        self.shot_bt.setMinimumSize(QtCore.QSize(100, 0))
        self.shot_bt.setObjectName("shot_bt")
        self.gridLayout_22.addWidget(self.shot_bt, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame_extraxtion_groupBox)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.key_frame_methods = QtWidgets.QComboBox(self.groupBox)
        self.key_frame_methods.setMinimumSize(QtCore.QSize(220, 0))
        self.key_frame_methods.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.key_frame_methods.setFont(font)
        self.key_frame_methods.setObjectName("key_frame_methods")
        self.key_frame_methods.addItem("")
        self.key_frame_methods.addItem("")
        self.gridLayout_6.addWidget(self.key_frame_methods, 0, 1, 1, 1)
        self.treshold_label = QtWidgets.QLabel(self.groupBox)
        self.treshold_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treshold_label.setFont(font)
        self.treshold_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.treshold_label.setObjectName("treshold_label")
        self.gridLayout_6.addWidget(self.treshold_label, 0, 2, 1, 1)
        self.trashold_btn = QtWidgets.QSpinBox(self.groupBox)
        self.trashold_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.trashold_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trashold_btn.setFont(font)
        self.trashold_btn.setObjectName("trashold_btn")
        self.gridLayout_6.addWidget(self.trashold_btn, 0, 3, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox, 1, 0, 1, 1)
        self.frame_rate_bt = QtWidgets.QRadioButton(
            self.frame_extraxtion_groupBox)
        self.frame_rate_bt.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_rate_bt.setObjectName("frame_rate_bt")
        self.gridLayout_22.addWidget(self.frame_rate_bt, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_extraxtion_groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_rate_option = QtWidgets.QSpinBox(self.groupBox_2)
        self.frame_rate_option.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_rate_option.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_rate_option.setFont(font)
        self.frame_rate_option.setObjectName("frame_rate_option")
        self.gridLayout_2.addWidget(self.frame_rate_option, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_extraxtion_groupBox)
        self.gridLayout_9.addLayout(self.verticalLayout_2, 2, 0, 1, 3)
        self.extraxt_btn = QtWidgets.QPushButton(self.option_frame)
        self.extraxt_btn.setMinimumSize(QtCore.QSize(110, 0))
        self.extraxt_btn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.extraxt_btn.setObjectName("extraxt_btn")
        self.gridLayout_9.addWidget(self.extraxt_btn, 3, 2, 1, 1)

# video extract frames
        self.extraxt_btn.clicked.connect(self.extractFrame)

        self.lineEdit = QtWidgets.QLineEdit(self.option_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_9.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.upload_btn = QtWidgets.QPushButton(self.option_frame)
        self.upload_btn.setObjectName("upload_btn")
 # video upload
        self.upload_btn.clicked.connect(self.uploadFile)

        self.gridLayout_9.addWidget(self.upload_btn, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.option_frame, 0, 2, 1, 1)
        self.gridLayout_20.addWidget(self.w1_ui1_frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.Frame_extraction_tab)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
 # frames display
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1211, 400))
        self.listWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.listWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.listWidget.setBaseSize(QtCore.QSize(0, 0))
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(0)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setIconSize(QtCore.QSize(157, 160))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_20.addWidget(self.frame_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Frame_extraction_tab, "")

        self.Feature_tab = QtWidgets.QWidget()
        self.Feature_tab.setObjectName("Feature_tab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.Feature_tab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.features_extraction_frame = QtWidgets.QFrame(self.Feature_tab)
        self.features_extraction_frame.setMinimumSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.features_extraction_frame.setFont(font)
        self.features_extraction_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.features_extraction_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.features_extraction_frame.setObjectName(
            "features_extraction_frame")
        self.gridLayout_15 = QtWidgets.QGridLayout(
            self.features_extraction_frame)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.colorfulness_groupBox = QtWidgets.QGroupBox(
            self.features_extraction_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.colorfulness_groupBox.setFont(font)
        self.colorfulness_groupBox.setObjectName("colorfulness_groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.colorfulness_groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.color_label = QtWidgets.QLabel(self.colorfulness_groupBox)
        self.color_label.setObjectName("color_label")
        self.gridLayout_8.addWidget(self.color_label, 0, 0, 1, 1)
        self.color_comboBox = QtWidgets.QComboBox(self.colorfulness_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.color_comboBox.setFont(font)
        self.color_comboBox.setObjectName("color_comboBox")
        self.color_comboBox.addItem("")
        self.color_comboBox.setItemText(0, "")
        self.color_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.color_comboBox, 0, 1, 1, 2)
        self.color_pairs = QtWidgets.QCheckBox(self.colorfulness_groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.color_pairs.setFont(font)
        self.color_pairs.setObjectName("color_pairs")
        self.gridLayout_8.addWidget(self.color_pairs, 1, 2, 1, 1)
        self.color_single = QtWidgets.QCheckBox(self.colorfulness_groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.color_single.setFont(font)
        self.color_single.setObjectName("color_single")
        self.gridLayout_8.addWidget(self.color_single, 1, 1, 1, 1)
        self.gridLayout_15.addWidget(self.colorfulness_groupBox, 0, 0, 1, 1)
        self.compression_groupBox = QtWidgets.QGroupBox(
            self.features_extraction_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.compression_groupBox.setFont(font)
        self.compression_groupBox.setObjectName("compression_groupBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.compression_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.MPEG = QtWidgets.QCheckBox(self.compression_groupBox)
        self.MPEG.setObjectName("MPEG")
        self.gridLayout_10.addWidget(self.MPEG, 0, 0, 1, 1)
        self.H264 = QtWidgets.QCheckBox(self.compression_groupBox)
        self.H264.setObjectName("H264")
        self.gridLayout_10.addWidget(self.H264, 0, 1, 1, 1)
        self.H263 = QtWidgets.QCheckBox(self.compression_groupBox)
        self.H263.setObjectName("H263")
        self.gridLayout_10.addWidget(self.H263, 0, 2, 1, 1)
        self.gridLayout_15.addWidget(self.compression_groupBox, 2, 0, 1, 1)
        self.visual_complexity_groupBox_2 = QtWidgets.QGroupBox(
            self.features_extraction_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.visual_complexity_groupBox_2.setFont(font)
        self.visual_complexity_groupBox_2.setObjectName(
            "visual_complexity_groupBox_2")
        self.gridLayout_14 = QtWidgets.QGridLayout(
            self.visual_complexity_groupBox_2)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.SSI_label = QtWidgets.QLabel(self.visual_complexity_groupBox_2)
        self.SSI_label.setObjectName("SSI_label")
        self.gridLayout_14.addWidget(self.SSI_label, 0, 0, 1, 1)
        self.color_comboBox_2 = QtWidgets.QComboBox(
            self.visual_complexity_groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.color_comboBox_2.setFont(font)
        self.color_comboBox_2.setObjectName("color_comboBox_2")
        self.color_comboBox_2.addItem("")
        self.color_comboBox_2.setItemText(0, "")
        self.color_comboBox_2.addItem("")
        self.gridLayout_14.addWidget(self.color_comboBox_2, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(
            self.visual_complexity_groupBox_2, 1, 0, 1, 1)
        self.motion_groupBox = QtWidgets.QGroupBox(
            self.features_extraction_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.motion_groupBox.setFont(font)
        self.motion_groupBox.setObjectName("motion_groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.motion_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.motion_label = QtWidgets.QLabel(self.motion_groupBox)
        self.motion_label.setObjectName("motion_label")
        self.gridLayout_5.addWidget(self.motion_label, 0, 0, 1, 1)
        self.contourSizeValue = QtWidgets.QSpinBox(self.motion_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contourSizeValue.setFont(font)
        self.contourSizeValue.setObjectName("contourSizeValue")
        self.gridLayout_5.addWidget(self.contourSizeValue, 2, 3, 1, 1)
        self.kernalSizeValue = QtWidgets.QSpinBox(self.motion_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kernalSizeValue.setFont(font)
        self.kernalSizeValue.setObjectName("kernalSizeValue")
        self.gridLayout_5.addWidget(self.kernalSizeValue, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.motion_groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.motion_groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.motion_detection_comboBox = QtWidgets.QComboBox(
            self.motion_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.motion_detection_comboBox.setFont(font)
        self.motion_detection_comboBox.setObjectName(
            "motion_detection_comboBox")
        self.motion_detection_comboBox.addItem("")
        self.motion_detection_comboBox.setItemText(0, "")
        self.motion_detection_comboBox.addItem("")
        self.motion_detection_comboBox.addItem("")
        self.motion_detection_comboBox.addItem("")
        self.motion_detection_comboBox.addItem("")
        self.gridLayout_5.addWidget(self.motion_detection_comboBox, 0, 1, 1, 3)
        self.gridLayout_15.addWidget(self.motion_groupBox, 4, 0, 1, 1)
        self.face_detection_groupBox = QtWidgets.QGroupBox(
            self.features_extraction_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.face_detection_groupBox.setFont(font)
        self.face_detection_groupBox.setObjectName("face_detection_groupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(
            self.face_detection_groupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.face_detection_label = QtWidgets.QLabel(
            self.face_detection_groupBox)
        self.face_detection_label.setObjectName("face_detection_label")
        self.gridLayout_13.addWidget(self.face_detection_label, 0, 0, 1, 1)
        self.face_detection_comboBox = QtWidgets.QComboBox(
            self.face_detection_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.face_detection_comboBox.setFont(font)
        self.face_detection_comboBox.setObjectName("face_detection_comboBox")
        self.face_detection_comboBox.addItem("")
        self.face_detection_comboBox.setItemText(0, "")
        self.face_detection_comboBox.addItem("")
        self.gridLayout_13.addWidget(self.face_detection_comboBox, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.face_detection_groupBox, 3, 0, 1, 1)
        self.gridLayout_16.addWidget(
            self.features_extraction_frame, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.Feature_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(550, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.object_detection_groupBox_2 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.object_detection_groupBox_2.setFont(font)
        self.object_detection_groupBox_2.setObjectName(
            "object_detection_groupBox_2")
        self.gridLayout_18 = QtWidgets.QGridLayout(
            self.object_detection_groupBox_2)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.object_detection_checkBox_2 = QtWidgets.QCheckBox(
            self.object_detection_groupBox_2)
        self.object_detection_checkBox_2.setObjectName(
            "object_detection_checkBox_2")
        self.gridLayout_18.addWidget(
            self.object_detection_checkBox_2, 0, 0, 1, 1)
        self.staticSaliencyApproch = QtWidgets.QComboBox(
            self.object_detection_groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.staticSaliencyApproch.setFont(font)
        self.staticSaliencyApproch.setObjectName("staticSaliencyApproch")
        self.staticSaliencyApproch.addItem("")
        self.staticSaliencyApproch.setItemText(0, "")
        self.staticSaliencyApproch.addItem("")
        self.staticSaliencyApproch.addItem("")
        self.gridLayout_18.addWidget(self.staticSaliencyApproch, 0, 1, 1, 1)
        self.object_detection_checkBox_3 = QtWidgets.QCheckBox(
            self.object_detection_groupBox_2)
        self.object_detection_checkBox_3.setObjectName(
            "object_detection_checkBox_3")
        self.gridLayout_18.addWidget(
            self.object_detection_checkBox_3, 1, 0, 1, 1)
        self.motionSaliencyApproch = QtWidgets.QComboBox(
            self.object_detection_groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.motionSaliencyApproch.setFont(font)
        self.motionSaliencyApproch.setObjectName("motionSaliencyApproch")
        self.motionSaliencyApproch.addItem("")
        self.motionSaliencyApproch.setItemText(0, "")
        self.motionSaliencyApproch.addItem("")
        self.gridLayout_18.addWidget(self.motionSaliencyApproch, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(
            self.object_detection_groupBox_2, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem1, 2, 2, 1, 1)
        self.outPut_result_formBox = QtWidgets.QGroupBox(self.frame)
        self.outPut_result_formBox.setMinimumSize(QtCore.QSize(0, 0))
        self.outPut_result_formBox.setMaximumSize(QtCore.QSize(16777215, 167))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outPut_result_formBox.setFont(font)
        self.outPut_result_formBox.setFlat(False)
        self.outPut_result_formBox.setCheckable(False)
        self.outPut_result_formBox.setObjectName("outPut_result_formBox")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.outPut_result_formBox)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.result_linetext = QtWidgets.QLineEdit(self.outPut_result_formBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_linetext.setFont(font)
        self.result_linetext.setObjectName("result_linetext")
        self.gridLayout_19.addWidget(self.result_linetext, 2, 1, 1, 1)
        self.saveResult_btn = QtWidgets.QPushButton(self.outPut_result_formBox)
        self.saveResult_btn.setObjectName("saveResult_btn")
        self.gridLayout_19.addWidget(self.saveResult_btn, 3, 2, 1, 1)
        self.browse_output_btn = QtWidgets.QPushButton(
            self.outPut_result_formBox)
        self.browse_output_btn.setCheckable(False)
        self.browse_output_btn.setObjectName("browse_output_btn")
        self.gridLayout_19.addWidget(self.browse_output_btn, 2, 2, 1, 1)
        self.output_result_label = QtWidgets.QLabel(self.outPut_result_formBox)
        self.output_result_label.setObjectName("output_result_label")
        self.gridLayout_19.addWidget(self.output_result_label, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.outPut_result_formBox, 3, 0, 1, 3)
        self.object_detection_groupBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.object_detection_groupBox.setFont(font)
        self.object_detection_groupBox.setObjectName(
            "object_detection_groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(
            self.object_detection_groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ObjDetVideo = QtWidgets.QRadioButton(
            self.object_detection_groupBox)
        self.ObjDetVideo.setObjectName("ObjDetVideo")
        self.gridLayout_11.addWidget(self.ObjDetVideo, 0, 2, 1, 1)
        self.ObjDetKeyFrame = QtWidgets.QRadioButton(
            self.object_detection_groupBox)
        self.ObjDetKeyFrame.setObjectName("ObjDetKeyFrame")
        self.gridLayout_11.addWidget(self.ObjDetKeyFrame, 0, 0, 1, 1)
        self.detector_label = QtWidgets.QLabel(self.object_detection_groupBox)
        self.detector_label.setIndent(19)
        self.detector_label.setObjectName("detector_label")
        self.gridLayout_11.addWidget(self.detector_label, 1, 0, 1, 1)
        self.object_detector_comboBox = QtWidgets.QComboBox(
            self.object_detection_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.object_detector_comboBox.setFont(font)
        self.object_detector_comboBox.setObjectName("object_detector_comboBox")
        self.object_detector_comboBox.addItem("")
        self.object_detector_comboBox.setItemText(0, "")
        self.object_detector_comboBox.addItem("")
        self.gridLayout_11.addWidget(self.object_detector_comboBox, 1, 2, 1, 1)
        self.gridLayout_12.addWidget(
            self.object_detection_groupBox, 1, 0, 1, 3)
        self.gridLayout_16.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem3, 1, 1, 1, 1)
        self.tabWidget.addTab(self.Feature_tab, "")


# page three
        self.visulaization_tab = QtWidgets.QWidget()
        self.visulaization_tab.setObjectName("visulaization_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.visulaization_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.visulaization_fatures_frame = QtWidgets.QFrame(
            self.visulaization_tab)
        self.visulaization_fatures_frame.setMaximumSize(
            QtCore.QSize(350, 16777215))
        self.visulaization_fatures_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.visulaization_fatures_frame.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.visulaization_fatures_frame.setObjectName(
            "visulaization_fatures_frame")
        self.gridLayout_17 = QtWidgets.QGridLayout(
            self.visulaization_fatures_frame)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.vis_label = QtWidgets.QLabel(self.visulaization_fatures_frame)
        self.vis_label.setObjectName("vis_label")
        self.gridLayout_17.addWidget(self.vis_label, 0, 0, 1, 1)
        self.listWidget_visulaization = QtWidgets.QListWidget(
            self.visulaization_fatures_frame)
        self.listWidget_visulaization.setObjectName("listWidget_visulaization")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_visulaization.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_visulaization.addItem(item)
        self.gridLayout_17.addWidget(self.listWidget_visulaization, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(
            self.visulaization_fatures_frame, 0, 0, 1, 1)
        self.visulaization_canvas_frame = QtWidgets.QFrame(
            self.visulaization_tab)
        self.visulaization_canvas_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.visulaization_canvas_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.visulaization_canvas_frame.setObjectName(
            "visulaization_canvas_frame")
        self.gridLayout_21 = QtWidgets.QGridLayout(
            self.visulaization_canvas_frame)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.vis = Canvas()
        self.gridLayout_21.addWidget(self.vis, 0, 0, 1, 1)

        # reseults in table
        # self.results = pandasModel(df)
        # self.view1 =  QTableView()
        # self.view1.setModel(self.results)
        # self.view1.show()
        # self.gridLayout_21.addWidget(self.view1, 0, 0, 1, 1)

        self.gridLayout_7.addWidget(
            self.visulaization_canvas_frame, 0, 1, 1, 1)

        self.tabWidget.addTab(self.visulaization_tab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


### my functions ###


    def uploadFile(self):
        global fileName, path
        fileName, _ = QFileDialog.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", QDir.homePath())
        self.lineEdit.setText(fileName)
        if fileName != '':
            self.myVideo.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.myVideo.playButton.setEnabled(True)

        # create project folder
        dic = QDir()
        path = QDir(fileName).dirName()
        path = path.replace(".", "-")
        # path = './output/'
        dic.mkdir(path)
        dic.setCurrent(path)

    def extractFrame(self):
        self.listWidget.clear()
        files = QDir().entryList(["*.jpg"], QDir.Files)
        for x in files:
            QDir().remove(x)

        if self.shot_bt.isChecked() == True:
            if self.key_frame_methods.currentIndex() == 0:
                # print("method is 0")
                method = 0
                treshold = self.trashold_btn.value()
                frameExtraction(fileName, method, treshold)

            if self.key_frame_methods.currentIndex() == 1:
                method = 1
                treshold = self.trashold_btn.value()
                frameExtraction(fileName, method, treshold)
                # print ("method is 01")

        if self.frame_rate_bt.isChecked() == True:
            frameRate = self.frame_rate_option.value()
            vid = VideoAnalysis(fileName)
            vid.extractFrames(frameRate)

#  QDir.Reverse\
        dic = QDir()
        files = dic.entryList(["*.jpg"], QDir.Files, QDir.Time)
        for x in files[::-1]:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(x)),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.listWidget.addItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AUVANA"))
        self.label.setText(_translate("MainWindow", "Upload Video"))
        self.frame_extraxtion_groupBox.setTitle(
            _translate("MainWindow", "Frame Extraxtion Option"))
        self.shot_bt.setText(_translate("MainWindow", "Shot Boundary"))
        self.label_3.setText(_translate("MainWindow", "Extraction Method"))
        self.key_frame_methods.setItemText(
            0, _translate("MainWindow", "Content-Aware Detector"))
        self.key_frame_methods.setItemText(
            1, _translate("MainWindow", "Threshold Detector"))
        self.treshold_label.setText(_translate("MainWindow", "Threshold"))
        self.frame_rate_bt.setText(_translate("MainWindow", "Frame"))
        self.label_2.setText(_translate("MainWindow", "Time window in seonds"))
        self.extraxt_btn.setText(_translate("MainWindow", "Extract"))
        self.upload_btn.setText(_translate("MainWindow", "Browse"))
        self.listWidget.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Frame_extraction_tab), _translate("MainWindow", "Frame Extraction"))
        self.colorfulness_groupBox.setTitle(
            _translate("MainWindow", "Colorfulness"))
        self.color_label.setText(_translate("MainWindow", "Method"))
        self.color_comboBox.setItemText(
            1, _translate("MainWindow", "Hasler & Suesstrunk"))
        self.color_pairs.setText(_translate("MainWindow", "Pairs"))
        self.color_single.setText(_translate("MainWindow", "Single"))
        self.compression_groupBox.setTitle(
            _translate("MainWindow", "Compression"))
        self.MPEG.setText(_translate("MainWindow", "MPEG"))
        self.H264.setText(_translate("MainWindow", "AVA (H264)"))
        self.H263.setText(_translate("MainWindow", "H263"))
        self.visual_complexity_groupBox_2.setTitle(
            _translate("MainWindow", "Frame Structural Simiarity"))
        self.SSI_label.setText(_translate("MainWindow", "Method"))
        self.color_comboBox_2.setItemText(1, _translate(
            "MainWindow", "Structural Similarity Index"))
        self.motion_groupBox.setTitle(_translate("MainWindow", "Motion"))
        self.motion_label.setText(_translate("MainWindow", "Method"))
        self.label_8.setText(_translate("MainWindow", "Contour Size"))
        self.label_7.setText(_translate("MainWindow", "Kernal Size"))
        self.motion_detection_comboBox.setItemText(
            1, _translate("MainWindow", "Canny Edge Detection"))
        self.motion_detection_comboBox.setItemText(
            2, _translate("MainWindow", "Frame Differencing"))
        self.motion_detection_comboBox.setItemText(
            3, _translate("MainWindow", "Sobel Detection"))
        self.motion_detection_comboBox.setItemText(
            4, _translate("MainWindow", "Background Substracking"))
        self.face_detection_groupBox.setTitle(_translate(
            "MainWindow", "Face Recogntion and Tracking"))
        self.face_detection_label.setText(_translate("MainWindow", "Method"))
        self.face_detection_comboBox.setItemText(
            1, _translate("MainWindow", "Cascade Classifier"))
        self.object_detection_groupBox_2.setTitle(
            _translate("MainWindow", "Saliency"))
        self.object_detection_checkBox_2.setText(
            _translate("MainWindow", "Static saliency (keyframes)"))
        self.staticSaliencyApproch.setItemText(
            1, _translate("MainWindow", "Spectral Residual"))
        self.staticSaliencyApproch.setItemText(
            2, _translate("MainWindow", "Fine Grained"))
        self.object_detection_checkBox_3.setText(
            _translate("MainWindow", "Motion saliency"))
        self.motionSaliencyApproch.setItemText(
            1, _translate("MainWindow", "BinWangApr2014"))
        self.outPut_result_formBox.setTitle(
            _translate("MainWindow", "Save Output"))
        self.saveResult_btn.setText(_translate("MainWindow", "Save"))
        self.browse_output_btn.setText(_translate("MainWindow", "Browse"))
        self.output_result_label.setText(
            _translate("MainWindow", "Output Directory"))
        self.object_detection_groupBox.setTitle(
            _translate("MainWindow", "Object Detection"))
        self.ObjDetVideo.setText(_translate("MainWindow", "Video"))
        self.ObjDetKeyFrame.setText(_translate("MainWindow", "KeyFrames"))
        self.detector_label.setText(_translate("MainWindow", "Detector"))
        self.object_detector_comboBox.setItemText(
            1, _translate("MainWindow", "YOLO v3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Feature_tab), _translate("MainWindow", "Features Option"))
        self.vis_label.setText(_translate(
            "MainWindow", "Choose result to visualize"))
        __sortingEnabled = self.listWidget_visulaization.isSortingEnabled()
        self.listWidget_visulaization.setSortingEnabled(False)
        item = self.listWidget_visulaization.item(0)
        item.setText(_translate("MainWindow", "Colorfulness"))
        item = self.listWidget_visulaization.item(1)
        item.setText(_translate("MainWindow", "Number of Objects"))
        self.listWidget_visulaization.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.visulaization_tab), _translate("MainWindow", "Visualization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
