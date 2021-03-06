#/usr/bin/python

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):

        self.defaultHostIp = '0.0.0.0'
        self.defaultHostPort = 1024


        #gui-initializing
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(781, 478)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.hostIp = QtGui.QLineEdit(self.widget)
        self.hostIp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.hostIp.setObjectName(_fromUtf8("hostIp"))
        self.hostIp.setText(self.defaultHostIp)
        self.hostIp.setDisabled(True)
        self.hostIp.setInputMask('000.000.000.000;_')
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.hostIp)
        self.hostPort = QtGui.QSpinBox(self.widget)
        self.hostPort.setMinimum(1024)
        self.hostPort.setMaximum(49151)
        self.hostPort.setObjectName(_fromUtf8("hostPort"))
        self.hostPort.setValue(self.defaultHostPort)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.hostPort)
        self.clientIp = QtGui.QLineEdit(self.widget)
        self.clientIp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.clientIp.setObjectName(_fromUtf8("clientIp"))
        self.clientIp.setInputMask('000.000.000.000;_')
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.clientIp)
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.formLayout.setWidget(11, QtGui.QFormLayout.SpanningRole, self.widget_3)
        self.clientPort = QtGui.QSpinBox(self.widget)
        self.clientPort.setMinimum(1024)
        self.clientPort.setMaximum(49151)
        self.clientPort.setObjectName(_fromUtf8("clientPort"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.clientPort)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_2)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.label_8)
        self.nickName = QtGui.QLineEdit(self.widget)
        self.nickName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.nickName.setObjectName(_fromUtf8("nickName"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.nickName)
        self.horizontalLayout.addWidget(self.widget)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget = QtGui.QListWidget(self.frame)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.messageBox = QtGui.QTextEdit(self.frame)
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.verticalLayout_2.addWidget(self.messageBox)
        self.widget_2 = QtGui.QWidget(self.frame)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clearButton = QtGui.QPushButton(self.widget_2)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.sendButton = QtGui.QPushButton(self.widget_2)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout_2.addWidget(self.sendButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu.addAction(self.actionVersion)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.nickName)
        self.startServer = QtGui.QPushButton(self.widget)
        self.startServer.setObjectName(_fromUtf8("startServer"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.startServer)
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 3))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setVisible(False)
        self.formLayout.setWidget(15, QtGui.QFormLayout.SpanningRole, self.progressBar)
        self.progressLbl = QtGui.QLabel(self.widget)
        self.progressLbl.setObjectName(_fromUtf8("progressLbl"))
        newfont = QtGui.QFont("Arial", 10, QtGui.QFont.Bold)
        self.progressLbl.setFont(newfont)
        self.formLayout.setWidget(14, QtGui.QFormLayout.LabelRole, self.progressLbl)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "p2pme", None))
        self.label_5.setText(_translate("MainWindow", "Nick:", None))
        self.startServer.setText(_translate("MainWindow", "Connect", None))
        self.label.setText(_translate("MainWindow", "Host Ip:", None))
        self.label_2.setText(_translate("MainWindow", "Host Port:", None))
        self.label_7.setText(_translate("MainWindow", "Client Ip:", None))
        self.label_8.setText(_translate("MainWindow", "Client Port:", None))
        self.clearButton.setText(_translate("MainWindow", "Clear Logs", None))
        self.sendButton.setText(_translate("MainWindow", "Send", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.label_3.setText(_translate("MainWindow", "", None))
        self.actionVersion.setText(_translate("MainWindow", "Version", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.progressLbl.setText(_translate("MainWindow", "", None))

