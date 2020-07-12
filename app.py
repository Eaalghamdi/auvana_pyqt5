
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl, QAbstractTableModel, QThread
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QTableView,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import sys
import os

import cv2
import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector, ThresholdDetector

from auvanaWidget import (VideoWindow, Canvas, pandasModel)
from functions.videoAnalysis import VideoAnalysis
# from frame_extraction import frameExtraction
import pandas as pd


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s): return s


class freamExtraxtionThread(QThread):
    def __init__(self, fileName, method, treshold, gallery):

        QThread.__init__(self)
        self.fileName = fileName
        self.method = method
        self.treshold = treshold
        self.gallery = gallery

    def __del__(self):
        self.wait()

    def frameExtraction(self, video, method, treshold):

        video_manager = VideoManager([video])
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)

        # Add ContentDetector algorithm (constructor takes detector options like threshold).
        if method == 'ContentDetector':
            scene_manager.add_detector(ContentDetector(treshold))
        if method == 'threshold_detector':
            scene_manager.add_detector(ThresholdDetector(treshold))

        base_timecode = video_manager.get_base_timecode()

        # Set downscale factor to improve processing speed (no args means default).
        video_manager.set_downscale_factor()

        # Start video_manager.
        video_manager.start()

        # Perform scene detection on video_manager.
        scene_manager.detect_scenes(frame_source=video_manager)

        # Obtain list of detected scenes.
        scene_list = scene_manager.get_scene_list(base_timecode)

        cap = cv2.VideoCapture(video)

        for i, scene in enumerate(scene_list):
            i = i+1
            cut_frame = scene[0].get_frames()
            cap.set(1, cut_frame)
            ret, frame = cap.read()
            frame_name = "shot " + str(i) + ".jpg"
            cv2.imwrite(frame_name, frame)

        # sort the list of imnags in dic as they saved
        # imgs = sorted(glob.glob('*.jpg'), key=os.path.getmtime)

    def run(self):

        dic = QDir()
        files = dic.entryList(["*.jpg"], QDir.Files, QDir.Time)
        for x in files[::-1]:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8(x)),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.gallery.addItem(item)
            self.sleep(2)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1680, 1024)
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

        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabs.setFont(font)
        self.tabs.setMouseTracking(True)
        self.tabs.setTabletTracking(True)
        self.tabs.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabs.setObjectName("tabs")

        self.Frame_extraction_tab = QtWidgets.QWidget()
        self.Frame_extraction_tab.setObjectName("Frame_extraction_tab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.Frame_extraction_tab)
        self.gridLayout_20.setObjectName("gridLayout_20")

        self.top_ui = QtWidgets.QFrame(self.Frame_extraction_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.top_ui.sizePolicy().hasHeightForWidth())
        self.top_ui.setSizePolicy(sizePolicy)
        self.top_ui.setMinimumSize(QtCore.QSize(0, 0))
        self.top_ui.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.top_ui.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_ui.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_ui.setObjectName("top_ui")

        self.gridLayout = QtWidgets.QGridLayout(self.top_ui)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.video_player_frame = QtWidgets.QFrame(self.top_ui)
        self.video_player_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.video_player_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.video_player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_player_frame.setObjectName("video_player_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.video_player_frame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # self.video_player = QtWidgets.QGraphicsView(self.video_player_frame)
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.video_player.sizePolicy().hasHeightForWidth())
        # self.video_player.setSizePolicy(sizePolicy)
        # self.video_player.setMinimumSize(QtCore.QSize(540, 0))
        # self.video_player.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.video_player.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.video_player.setInteractive(True)
        # self.video_player.setObjectName("video_player")
        # self.gridLayout_4.addWidget(self.video_player, 0, 0, 1, 1)
        # self.gridLayout.addWidget(self.video_player_frame, 0, 0, 1, 1)

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
        # self.myVideo.setMaximumSize(QtCore.QSize(570, 400))
        self.gridLayout_4.addWidget(self.myVideo, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.video_player_frame, 0, 0, 1, 1)

        self.option_frame = QtWidgets.QFrame(self.top_ui)
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
        self.extraxt_btn.clicked.connect(self.extractFrame)

        self.gridLayout_9.addWidget(self.extraxt_btn, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.option_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_9.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.upload_btn = QtWidgets.QPushButton(self.option_frame)
        self.upload_btn.setObjectName("upload_btn")
        self.upload_btn.clicked.connect(self.uploadFile)

        self.gridLayout_9.addWidget(self.upload_btn, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.option_frame, 0, 2, 1, 1)
        self.gridLayout_20.addWidget(self.top_ui, 0, 0, 1, 1)

        self.bottom_ui = QtWidgets.QFrame(self.Frame_extraction_tab)
        self.bottom_ui.setMinimumSize(QtCore.QSize(0, 200))
        self.bottom_ui.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_ui.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottom_ui.setObjectName("bottom_ui")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bottom_ui)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gallery = QtWidgets.QListWidget(self.bottom_ui)
        self.gallery.setMinimumSize(QtCore.QSize(0, 200))
        self.gallery.setSizeIncrement(QtCore.QSize(0, 0))
        self.gallery.setBaseSize(QtCore.QSize(0, 0))
        self.gallery.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gallery.setAutoFillBackground(True)
        self.gallery.setAutoScroll(True)
        self.gallery.setAutoScrollMargin(0)
        self.gallery.setTabKeyNavigation(False)
        self.gallery.setProperty("showDropIndicator", False)
        self.gallery.setAlternatingRowColors(False)
        self.gallery.setIconSize(QtCore.QSize(157, 157))
        self.gallery.setTextElideMode(QtCore.Qt.ElideNone)
        self.gallery.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.gallery.setMovement(QtWidgets.QListView.Static)
        self.gallery.setFlow(QtWidgets.QListView.LeftToRight)
        self.gallery.setProperty("isWrapping", True)
        self.gallery.setResizeMode(QtWidgets.QListView.Adjust)
        self.gallery.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.gallery.setViewMode(QtWidgets.QListView.IconMode)
        self.gallery.setModelColumn(0)
        self.gallery.setUniformItemSizes(True)
        self.gallery.setWordWrap(True)
        self.gallery.setSelectionRectVisible(False)
        self.gallery.setObjectName("gallery")
        self.verticalLayout.addWidget(self.gallery)
        self.gridLayout_20.addWidget(self.bottom_ui, 1, 0, 1, 1)
        self.tabs.addTab(self.Frame_extraction_tab, "")

        self.Feature_tab = QtWidgets.QWidget()
        self.Feature_tab.setObjectName("Feature_tab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.Feature_tab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.features_top_left_ui = QtWidgets.QFrame(self.Feature_tab)
        self.features_top_left_ui.setMinimumSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.features_top_left_ui.setFont(font)
        self.features_top_left_ui.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.features_top_left_ui.setFrameShadow(QtWidgets.QFrame.Raised)
        self.features_top_left_ui.setObjectName("features_top_left_ui")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.features_top_left_ui)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.colorfulness_groupBox = QtWidgets.QGroupBox(
            self.features_top_left_ui)
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
            self.features_top_left_ui)
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
        self.SSI_groupBox = QtWidgets.QGroupBox(self.features_top_left_ui)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SSI_groupBox.setFont(font)
        self.SSI_groupBox.setObjectName("SSI_groupBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.SSI_groupBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.SSI_label = QtWidgets.QLabel(self.SSI_groupBox)
        self.SSI_label.setObjectName("SSI_label")
        self.gridLayout_14.addWidget(self.SSI_label, 0, 0, 1, 1)
        self.SSI_comboBox = QtWidgets.QComboBox(self.SSI_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SSI_comboBox.setFont(font)
        self.SSI_comboBox.setObjectName("SSI_comboBox")
        self.SSI_comboBox.addItem("")
        self.SSI_comboBox.setItemText(0, "")
        self.SSI_comboBox.addItem("")
        self.gridLayout_14.addWidget(self.SSI_comboBox, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.SSI_groupBox, 1, 0, 1, 1)
        self.motion_groupBox = QtWidgets.QGroupBox(self.features_top_left_ui)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.motion_groupBox.setFont(font)
        self.motion_groupBox.setObjectName("motion_groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.motion_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.motion_label_method = QtWidgets.QLabel(self.motion_groupBox)
        self.motion_label_method.setObjectName("motion_label_method")
        self.gridLayout_5.addWidget(self.motion_label_method, 0, 0, 1, 1)
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
        self.label_right = QtWidgets.QLabel(self.motion_groupBox)
        self.label_right.setObjectName("label_right")
        self.gridLayout_5.addWidget(self.label_right, 2, 2, 1, 1)
        self.label_left = QtWidgets.QLabel(self.motion_groupBox)
        self.label_left.setObjectName("label_left")
        self.gridLayout_5.addWidget(self.label_left, 2, 0, 1, 1)
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
            self.features_top_left_ui)
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
        self.gridLayout_16.addWidget(self.features_top_left_ui, 0, 0, 1, 1)
        self.features_top_right_ui = QtWidgets.QFrame(self.Feature_tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.features_top_right_ui.sizePolicy().hasHeightForWidth())
        self.features_top_right_ui.setSizePolicy(sizePolicy)
        self.features_top_right_ui.setMinimumSize(QtCore.QSize(550, 0))
        self.features_top_right_ui.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.features_top_right_ui.setFrameShadow(QtWidgets.QFrame.Raised)
        self.features_top_right_ui.setObjectName("features_top_right_ui")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.features_top_right_ui)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.saliency_groupBox = QtWidgets.QGroupBox(
            self.features_top_right_ui)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.saliency_groupBox.setFont(font)
        self.saliency_groupBox.setObjectName("saliency_groupBox")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.saliency_groupBox)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.saliency_checkBox1 = QtWidgets.QCheckBox(self.saliency_groupBox)
        self.saliency_checkBox1.setObjectName("saliency_checkBox1")
        self.gridLayout_18.addWidget(self.saliency_checkBox1, 0, 0, 1, 1)
        self.staticSaliencyApproch = QtWidgets.QComboBox(
            self.saliency_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.staticSaliencyApproch.setFont(font)
        self.staticSaliencyApproch.setObjectName("staticSaliencyApproch")
        self.staticSaliencyApproch.addItem("")
        self.staticSaliencyApproch.setItemText(0, "")
        self.staticSaliencyApproch.addItem("")
        self.staticSaliencyApproch.addItem("")
        self.gridLayout_18.addWidget(self.staticSaliencyApproch, 0, 1, 1, 1)
        self.saliency_checkBox1_2 = QtWidgets.QCheckBox(self.saliency_groupBox)
        self.saliency_checkBox1_2.setObjectName("saliency_checkBox1_2")
        self.gridLayout_18.addWidget(self.saliency_checkBox1_2, 1, 0, 1, 1)
        self.motionSaliencyApproch = QtWidgets.QComboBox(
            self.saliency_groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.motionSaliencyApproch.setFont(font)
        self.motionSaliencyApproch.setObjectName("motionSaliencyApproch")
        self.motionSaliencyApproch.addItem("")
        self.motionSaliencyApproch.setItemText(0, "")
        self.motionSaliencyApproch.addItem("")
        self.gridLayout_18.addWidget(self.motionSaliencyApproch, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(self.saliency_groupBox, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem1, 2, 2, 1, 1)
        self.outPut_result_formBox = QtWidgets.QGroupBox(
            self.features_top_right_ui)
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
        self.object_detection_groupBox = QtWidgets.QGroupBox(
            self.features_top_right_ui)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.object_detection_groupBox.setFont(font)
        self.object_detection_groupBox.setObjectName(
            "object_detection_groupBox")
        self.gridLayout_11 = QtWidgets.QGridLayout(
            self.object_detection_groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ObjDet_btn_right = QtWidgets.QRadioButton(
            self.object_detection_groupBox)
        self.ObjDet_btn_right.setObjectName("ObjDet_btn_right")
        self.gridLayout_11.addWidget(self.ObjDet_btn_right, 0, 2, 1, 1)
        self.ObjDet_btn_left = QtWidgets.QRadioButton(
            self.object_detection_groupBox)
        self.ObjDet_btn_left.setObjectName("ObjDet_btn_left")
        self.gridLayout_11.addWidget(self.ObjDet_btn_left, 0, 0, 1, 1)
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
        self.gridLayout_16.addWidget(self.features_top_right_ui, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem3, 1, 1, 1, 1)
        self.tabs.addTab(self.Feature_tab, "")
        self.visulaization_tab = QtWidgets.QWidget()
        self.visulaization_tab.setObjectName("visulaization_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.visulaization_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.visulaization_options_window = QtWidgets.QFrame(
            self.visulaization_tab)
        self.visulaization_options_window.setMaximumSize(
            QtCore.QSize(350, 16777215))
        self.visulaization_options_window.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.visulaization_options_window.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.visulaization_options_window.setObjectName(
            "visulaization_options_window")
        self.gridLayout_17 = QtWidgets.QGridLayout(
            self.visulaization_options_window)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.vis_label = QtWidgets.QLabel(self.visulaization_options_window)
        self.vis_label.setObjectName("vis_label")
        self.gridLayout_17.addWidget(self.vis_label, 0, 0, 1, 1)
        self.list_visulaization_optios = QtWidgets.QListWidget(
            self.visulaization_options_window)
        self.list_visulaization_optios.setObjectName(
            "list_visulaization_optios")
        item = QtWidgets.QListWidgetItem()
        self.list_visulaization_optios.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_visulaization_optios.addItem(item)
        self.gridLayout_17.addWidget(
            self.list_visulaization_optios, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(
            self.visulaization_options_window, 0, 0, 1, 1)
        self.visulaization_canvas = QtWidgets.QFrame(self.visulaization_tab)
        self.visulaization_canvas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.visulaization_canvas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.visulaization_canvas.setObjectName("visulaization_canvas")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.visulaization_canvas)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_7.addWidget(self.visulaization_canvas, 0, 1, 1, 1)
        self.tabs.addTab(self.visulaization_tab, "")
        self.gridLayout_3.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.gallery.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #### Functions ####

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
        self.gallery.clear()
        files = QDir().entryList(["*.jpg"], QDir.Files)
        for x in files:
            QDir().remove(x)

        if self.shot_bt.isChecked() == True:
            if self.key_frame_methods.currentIndex() == 0:
                method = 'ContentDetector'
                treshold = self.trashold_btn.value()
                self._freamExtraxtionThread = freamExtraxtionThread(
                    fileName, method, treshold, self.gallery)
                self._freamExtraxtionThread.frameExtraction(
                    fileName, method, treshold)
                self._freamExtraxtionThread.start()

            if self.key_frame_methods.currentIndex() == 1:
                method = 'threshold_detector'
                treshold = self.trashold_btn.value()
                self._freamExtraxtionThread = freamExtraxtionThread(
                    fileName, method, treshold, self.gallery)
                self._freamExtraxtionThread.frameExtraction(
                    fileName, method, treshold)
                self._freamExtraxtionThread.start()

        if self.frame_rate_bt.isChecked() == True:
            frameRate = self.frame_rate_option.value()
            vid = VideoAnalysis(fileName)
            vid.extractFrames(frameRate)

        #  QDir.Reverse\
        # dic = QDir()
        # files = dic.entryList(["*.jpg"], QDir.Files, QDir.Time)
        # for x in files[::-1]:
        #     item = QtWidgets.QListWidgetItem()
        #     icon = QtGui.QIcon()
        #     icon.addPixmap(QtGui.QPixmap(_fromUtf8(x)),
        #                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #     item.setIcon(icon)
        #     self.gallery.addItem(item)

        # def featureExtraxtion(self):
        #     if self.saveResult_btn.isChecked() == True:
        #         if self.color_comboBox.currentIndex() == 0:
        #             print(self.color_comboBox.currentIndex())
        #             method =

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
        self.gallery.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(
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
        self.SSI_groupBox.setTitle(_translate(
            "MainWindow", "Frame Structural Simiarity"))
        self.SSI_label.setText(_translate("MainWindow", "Method"))
        self.SSI_comboBox.setItemText(1, _translate(
            "MainWindow", "Structural Similarity Index"))
        self.motion_groupBox.setTitle(_translate("MainWindow", "Motion"))
        self.motion_label_method.setText(_translate("MainWindow", "Method"))
        self.label_right.setText(_translate("MainWindow", "Contour Size"))
        self.label_left.setText(_translate("MainWindow", "Kernal Size"))
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
        self.saliency_groupBox.setTitle(_translate("MainWindow", "Saliency"))
        self.saliency_checkBox1.setText(_translate(
            "MainWindow", "Static saliency (keyframes)"))
        self.staticSaliencyApproch.setItemText(
            1, _translate("MainWindow", "Spectral Residual"))
        self.staticSaliencyApproch.setItemText(
            2, _translate("MainWindow", "Fine Grained"))
        self.saliency_checkBox1_2.setText(
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
        self.ObjDet_btn_right.setText(_translate("MainWindow", "Video"))
        self.ObjDet_btn_left.setText(_translate("MainWindow", "KeyFrames"))
        self.detector_label.setText(_translate("MainWindow", "Detector"))
        self.object_detector_comboBox.setItemText(
            1, _translate("MainWindow", "YOLO v3"))
        self.tabs.setTabText(self.tabs.indexOf(
            self.Feature_tab), _translate("MainWindow", "Feature Options"))
        self.vis_label.setText(_translate(
            "MainWindow", "Choose result to visualize"))
        __sortingEnabled = self.list_visulaization_optios.isSortingEnabled()
        self.list_visulaization_optios.setSortingEnabled(False)
        item = self.list_visulaization_optios.item(0)
        item.setText(_translate("MainWindow", "Colorfulness"))
        item = self.list_visulaization_optios.item(1)
        item.setText(_translate("MainWindow", "Compression"))
        self.list_visulaization_optios.setSortingEnabled(__sortingEnabled)
        self.tabs.setTabText(self.tabs.indexOf(
            self.visulaization_tab), _translate("MainWindow", "Visualization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
