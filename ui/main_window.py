# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 20))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 60))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1001, 60))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_worker = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_worker.sizePolicy().hasHeightForWidth())
        self.add_worker.setSizePolicy(sizePolicy)
        self.add_worker.setMinimumSize(QtCore.QSize(0, 0))
        self.add_worker.setMaximumSize(QtCore.QSize(60, 16777215))
        self.add_worker.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/icons/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_worker.setIcon(icon1)
        self.add_worker.setIconSize(QtCore.QSize(45, 45))
        self.add_worker.setCheckable(False)
        self.add_worker.setFlat(True)
        self.add_worker.setObjectName("add_worker")
        self.horizontalLayout.addWidget(self.add_worker)
        self.del_worker = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_worker.sizePolicy().hasHeightForWidth())
        self.del_worker.setSizePolicy(sizePolicy)
        self.del_worker.setMinimumSize(QtCore.QSize(0, 0))
        self.del_worker.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.del_worker.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/icons/delete_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_worker.setIcon(icon2)
        self.del_worker.setIconSize(QtCore.QSize(45, 45))
        self.del_worker.setFlat(True)
        self.del_worker.setObjectName("del_worker")
        self.horizontalLayout.addWidget(self.del_worker)
        self.save_workers = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_workers.sizePolicy().hasHeightForWidth())
        self.save_workers.setSizePolicy(sizePolicy)
        self.save_workers.setMinimumSize(QtCore.QSize(0, 0))
        self.save_workers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.save_workers.setSizeIncrement(QtCore.QSize(0, 0))
        self.save_workers.setBaseSize(QtCore.QSize(0, 0))
        self.save_workers.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/icons/save_users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_workers.setIcon(icon3)
        self.save_workers.setIconSize(QtCore.QSize(45, 45))
        self.save_workers.setFlat(True)
        self.save_workers.setObjectName("save_workers")
        self.horizontalLayout.addWidget(self.save_workers)
        self.search_user = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_user.sizePolicy().hasHeightForWidth())
        self.search_user.setSizePolicy(sizePolicy)
        self.search_user.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/icons/search_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_user.setIcon(icon4)
        self.search_user.setIconSize(QtCore.QSize(45, 45))
        self.search_user.setFlat(True)
        self.search_user.setObjectName("search_user")
        self.horizontalLayout.addWidget(self.search_user)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 45))
        self.line.setMaximumSize(QtCore.QSize(16777215, 45))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.new_inproject = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_inproject.sizePolicy().hasHeightForWidth())
        self.new_inproject.setSizePolicy(sizePolicy)
        self.new_inproject.setMinimumSize(QtCore.QSize(0, 0))
        self.new_inproject.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.new_inproject.setBaseSize(QtCore.QSize(0, 0))
        self.new_inproject.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/icons/add_user_inproject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_inproject.setIcon(icon5)
        self.new_inproject.setIconSize(QtCore.QSize(45, 45))
        self.new_inproject.setFlat(True)
        self.new_inproject.setObjectName("new_inproject")
        self.horizontalLayout.addWidget(self.new_inproject)
        self.del_inproject = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_inproject.sizePolicy().hasHeightForWidth())
        self.del_inproject.setSizePolicy(sizePolicy)
        self.del_inproject.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui/icons/delete_user_inproject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_inproject.setIcon(icon6)
        self.del_inproject.setIconSize(QtCore.QSize(45, 45))
        self.del_inproject.setFlat(True)
        self.del_inproject.setObjectName("del_inproject")
        self.horizontalLayout.addWidget(self.del_inproject)
        self.save_inprojects = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_inprojects.sizePolicy().hasHeightForWidth())
        self.save_inprojects.setSizePolicy(sizePolicy)
        self.save_inprojects.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui/icons/save_user_inproject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_inprojects.setIcon(icon7)
        self.save_inprojects.setIconSize(QtCore.QSize(45, 45))
        self.save_inprojects.setFlat(True)
        self.save_inprojects.setObjectName("save_inprojects")
        self.horizontalLayout.addWidget(self.save_inprojects)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.undo_changes_workers = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_changes_workers.sizePolicy().hasHeightForWidth())
        self.undo_changes_workers.setSizePolicy(sizePolicy)
        self.undo_changes_workers.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui/icons/undo_changes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_changes_workers.setIcon(icon8)
        self.undo_changes_workers.setIconSize(QtCore.QSize(45, 45))
        self.undo_changes_workers.setFlat(True)
        self.undo_changes_workers.setObjectName("undo_changes_workers")
        self.horizontalLayout.addWidget(self.undo_changes_workers)
        self.update_data = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_data.sizePolicy().hasHeightForWidth())
        self.update_data.setSizePolicy(sizePolicy)
        self.update_data.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui/icons/update_data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_data.setIcon(icon9)
        self.update_data.setIconSize(QtCore.QSize(45, 45))
        self.update_data.setFlat(True)
        self.update_data.setObjectName("update_data")
        self.horizontalLayout.addWidget(self.update_data)
        self.settings = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ui/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon10)
        self.settings.setIconSize(QtCore.QSize(45, 45))
        self.settings.setFlat(True)
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.logout = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout.sizePolicy().hasHeightForWidth())
        self.logout.setSizePolicy(sizePolicy)
        self.logout.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ui/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon11)
        self.logout.setIconSize(QtCore.QSize(45, 45))
        self.logout.setFlat(True)
        self.logout.setObjectName("logout")
        self.horizontalLayout.addWidget(self.logout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 6)
        self.workers_table = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workers_table.sizePolicy().hasHeightForWidth())
        self.workers_table.setSizePolicy(sizePolicy)
        self.workers_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.workers_table.setGridStyle(QtCore.Qt.SolidLine)
        self.workers_table.setObjectName("workers_table")
        self.workers_table.setColumnCount(5)
        self.workers_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.workers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.workers_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.workers_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.workers_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.workers_table.setHorizontalHeaderItem(4, item)
        self.workers_table.horizontalHeader().setDefaultSectionSize(135)
        self.gridLayout_2.addWidget(self.workers_table, 2, 0, 1, 5)
        self.current_projects_table = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_projects_table.sizePolicy().hasHeightForWidth())
        self.current_projects_table.setSizePolicy(sizePolicy)
        self.current_projects_table.setMinimumSize(QtCore.QSize(300, 0))
        self.current_projects_table.setMaximumSize(QtCore.QSize(300, 16777215))
        self.current_projects_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.current_projects_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.current_projects_table.setGridStyle(QtCore.Qt.SolidLine)
        self.current_projects_table.setObjectName("current_projects_table")
        self.current_projects_table.setColumnCount(2)
        self.current_projects_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.current_projects_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.current_projects_table.setHorizontalHeaderItem(1, item)
        self.current_projects_table.horizontalHeader().setCascadingSectionResizes(False)
        self.current_projects_table.horizontalHeader().setDefaultSectionSize(140)
        self.current_projects_table.horizontalHeader().setMinimumSectionSize(39)
        self.current_projects_table.horizontalHeader().setSortIndicatorShown(False)
        self.current_projects_table.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.current_projects_table, 2, 5, 2, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.output_size = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_size.sizePolicy().hasHeightForWidth())
        self.output_size.setSizePolicy(sizePolicy)
        self.output_size.setMinimumSize(QtCore.QSize(50, 0))
        self.output_size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.output_size.setMaxLength(10000)
        self.output_size.setFrame(True)
        self.output_size.setAlignment(QtCore.Qt.AlignCenter)
        self.output_size.setObjectName("output_size")
        self.gridLayout_4.addWidget(self.output_size, 1, 2, 1, 1)
        self.page_left = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_left.sizePolicy().hasHeightForWidth())
        self.page_left.setSizePolicy(sizePolicy)
        self.page_left.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("ui/icons/left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page_left.setIcon(icon12)
        self.page_left.setObjectName("page_left")
        self.gridLayout_4.addWidget(self.page_left, 1, 1, 1, 1)
        self.page_right = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_right.sizePolicy().hasHeightForWidth())
        self.page_right.setSizePolicy(sizePolicy)
        self.page_right.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("ui/icons/right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page_right.setIcon(icon13)
        self.page_right.setIconSize(QtCore.QSize(16, 16))
        self.page_right.setObjectName("page_right")
        self.gridLayout_4.addWidget(self.page_right, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 0, 1, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 20))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.scrollArea_2.setAutoFillBackground(True)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setMidLineWidth(1)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1001, 60))
        self.scrollAreaWidgetContents_2.setAutoFillBackground(True)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_project = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_project.sizePolicy().hasHeightForWidth())
        self.add_project.setSizePolicy(sizePolicy)
        self.add_project.setMinimumSize(QtCore.QSize(0, 0))
        self.add_project.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_project.setBaseSize(QtCore.QSize(0, 0))
        self.add_project.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("ui/icons/add_project.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_project.setIcon(icon14)
        self.add_project.setIconSize(QtCore.QSize(45, 45))
        self.add_project.setFlat(True)
        self.add_project.setObjectName("add_project")
        self.horizontalLayout_2.addWidget(self.add_project)
        self.del_project = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_project.sizePolicy().hasHeightForWidth())
        self.del_project.setSizePolicy(sizePolicy)
        self.del_project.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("ui/icons/del_project.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_project.setIcon(icon15)
        self.del_project.setIconSize(QtCore.QSize(45, 45))
        self.del_project.setFlat(True)
        self.del_project.setObjectName("del_project")
        self.horizontalLayout_2.addWidget(self.del_project)
        self.save_projects = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_projects.sizePolicy().hasHeightForWidth())
        self.save_projects.setSizePolicy(sizePolicy)
        self.save_projects.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("ui/icons/save_project.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_projects.setIcon(icon16)
        self.save_projects.setIconSize(QtCore.QSize(45, 45))
        self.save_projects.setFlat(True)
        self.save_projects.setObjectName("save_projects")
        self.horizontalLayout_2.addWidget(self.save_projects)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.undo_changes_projects = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_changes_projects.sizePolicy().hasHeightForWidth())
        self.undo_changes_projects.setSizePolicy(sizePolicy)
        self.undo_changes_projects.setText("")
        self.undo_changes_projects.setIcon(icon8)
        self.undo_changes_projects.setIconSize(QtCore.QSize(45, 45))
        self.undo_changes_projects.setFlat(True)
        self.undo_changes_projects.setObjectName("undo_changes_projects")
        self.horizontalLayout_2.addWidget(self.undo_changes_projects)
        self.update_data_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_data_2.sizePolicy().hasHeightForWidth())
        self.update_data_2.setSizePolicy(sizePolicy)
        self.update_data_2.setText("")
        self.update_data_2.setIcon(icon9)
        self.update_data_2.setIconSize(QtCore.QSize(45, 45))
        self.update_data_2.setFlat(True)
        self.update_data_2.setObjectName("update_data_2")
        self.horizontalLayout_2.addWidget(self.update_data_2)
        self.settings_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_2.sizePolicy().hasHeightForWidth())
        self.settings_2.setSizePolicy(sizePolicy)
        self.settings_2.setText("")
        self.settings_2.setIcon(icon10)
        self.settings_2.setIconSize(QtCore.QSize(45, 45))
        self.settings_2.setFlat(True)
        self.settings_2.setObjectName("settings_2")
        self.horizontalLayout_2.addWidget(self.settings_2)
        self.logout_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_2.sizePolicy().hasHeightForWidth())
        self.logout_2.setSizePolicy(sizePolicy)
        self.logout_2.setText("")
        self.logout_2.setIcon(icon11)
        self.logout_2.setIconSize(QtCore.QSize(45, 45))
        self.logout_2.setFlat(True)
        self.logout_2.setObjectName("logout_2")
        self.horizontalLayout_2.addWidget(self.logout_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 3)
        self.projects_table = QtWidgets.QTableWidget(self.tab_2)
        self.projects_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.projects_table.setObjectName("projects_table")
        self.projects_table.setColumnCount(2)
        self.projects_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.projects_table.setHorizontalHeaderItem(1, item)
        self.projects_table.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout_3.addWidget(self.projects_table, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.label_log_main = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_log_main.sizePolicy().hasHeightForWidth())
        self.label_log_main.setSizePolicy(sizePolicy)
        self.label_log_main.setMinimumSize(QtCore.QSize(0, 0))
        self.label_log_main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_log_main.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_log_main.setText("")
        self.label_log_main.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_log_main.setObjectName("label_log_main")
        self.gridLayout.addWidget(self.label_log_main, 2, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.add_worker)
        MainWindow.setTabOrder(self.add_worker, self.del_worker)
        MainWindow.setTabOrder(self.del_worker, self.save_workers)
        MainWindow.setTabOrder(self.save_workers, self.search_user)
        MainWindow.setTabOrder(self.search_user, self.new_inproject)
        MainWindow.setTabOrder(self.new_inproject, self.del_inproject)
        MainWindow.setTabOrder(self.del_inproject, self.save_inprojects)
        MainWindow.setTabOrder(self.save_inprojects, self.undo_changes_workers)
        MainWindow.setTabOrder(self.undo_changes_workers, self.update_data)
        MainWindow.setTabOrder(self.update_data, self.settings)
        MainWindow.setTabOrder(self.settings, self.logout)
        MainWindow.setTabOrder(self.logout, self.workers_table)
        MainWindow.setTabOrder(self.workers_table, self.current_projects_table)
        MainWindow.setTabOrder(self.current_projects_table, self.page_left)
        MainWindow.setTabOrder(self.page_left, self.output_size)
        MainWindow.setTabOrder(self.output_size, self.page_right)
        MainWindow.setTabOrder(self.page_right, self.scrollArea_2)
        MainWindow.setTabOrder(self.scrollArea_2, self.add_project)
        MainWindow.setTabOrder(self.add_project, self.del_project)
        MainWindow.setTabOrder(self.del_project, self.save_projects)
        MainWindow.setTabOrder(self.save_projects, self.undo_changes_projects)
        MainWindow.setTabOrder(self.undo_changes_projects, self.update_data_2)
        MainWindow.setTabOrder(self.update_data_2, self.settings_2)
        MainWindow.setTabOrder(self.settings_2, self.logout_2)
        MainWindow.setTabOrder(self.logout_2, self.projects_table)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "peMI"))
        item = self.workers_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.workers_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.workers_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.workers_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.workers_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.current_projects_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название продукта"))
        item = self.current_projects_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Срок сдачи"))
        self.output_size.setText(_translate("MainWindow", "50"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Работники"))
        item = self.projects_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название продукта"))
        item = self.projects_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Срок сдачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Проекты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

