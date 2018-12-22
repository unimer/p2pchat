#!/usr/bin/python

from PyQt4.QtNetwork import QUdpSocket, QHostAddress
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import gui
import sys

class MainWind(QtGui.QMainWindow, gui.Ui_MainWindow):

    def app_q(self):
       app.quit()

    def print_version(self):
        self.info_box("App Version", "p2pme-1.0(beta) ®")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        QObject.connect(self.startServer, QtCore.SIGNAL ('clicked()'), self.start_server)
        QtCore.QObject.connect(self.sendButton, QtCore.SIGNAL('clicked()'), self.send_message)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL('clicked()'), self.clear_logs)
        self.messageBox.textChanged.connect(self.check_for_return)
        self.clientIp.returnPressed.connect(self.startServer.click)
        self.nickName.returnPressed.connect(self.startServer.click)
        #timers
        self.progressBarTimer = QtCore.QTimer(self)
        self.timer_clientCheck = QtCore.QTimer(self)
        self.timer2 = QtCore.QTimer(self)
        self.timer = QtCore.QTimer(self)
        #timer-signals
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update_my_status_online)
        QtCore.QObject.connect(self.progressBarTimer, QtCore.SIGNAL("timeout()"), self.progressBarInc)
        QtCore.QObject.connect(self.timer2, QtCore.SIGNAL("timeout()"), self.check_client_status)
        QtCore.QObject.connect(self.timer_clientCheck, QtCore.SIGNAL("timeout()"), self.setLbl_text)
        self.progressBar.valueChanged.connect(self.checkProgressVal)
        self.actionVersion.triggered.connect(self.print_version)
        self.actionExit.triggered.connect(self.app_q)
        #progressBar-settings
        self.progressBar.setMaximum(10)
        self.progressBar.setMinimum(0)

        #parameters for testing
        #self.nickName.setText("nick")
        #self.clientIp.setText("192.168.0.13")
        #parameters for testing


    def setLbl_text(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkRed)
        self.label_3.setPalette(palette)
        self.label_3.setText("Client is offline")

    def info_box(self,ttl, info):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle(ttl)
        msgBox.setText(info)
        msgBox.exec_()


    def info_box_advanced(self,ttl, info):
        msgBox = QtGui.QMessageBox()
        stayButton = msgBox.addButton(self.tr("Stay connected"), QtGui.QMessageBox.ActionRole)
        disconnectButton = msgBox.addButton(self.tr("Disconect"), QtGui.QMessageBox.ActionRole)
        msgBox.setDefaultButton(stayButton)
        msgBox.setWindowTitle(ttl)
        msgBox.setText(info)
        msgBox.exec_()
        if msgBox.clickedButton() == disconnectButton:
            self.update_my_status_offline()
            self.server.close()
            self.set_box_enabled()
            self.startServer.setText("Connect")
            self.label_3.setText("")
            self.progressBarTimer.stop()
            self.timer2.stop()
            self.timer.stop()
            self.progressBar.setValue(0)
            self.progressLbl.setText("")
            self.progressBar.setVisible(False)
            self.progressLbl.setVisible(False)
            self.timer_clientCheck.stop()

    def clear_logs(self):
        self.listWidget.clear()
        self.messageBox.setText("")

    def update_list(self, data):
        self.listWidget.addItem(data)
        self.listWidget.scrollToBottom()

    def myItemOnList(self, data):
        item = QtGui.QListWidgetItem(data)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        self.listWidget.addItem(item)
        self.listWidget.scrollToBottom()

    def read_message(self):
        palette = QtGui.QPalette()

        #recieving-message
        (data, senderAddress, senderPort) = self.server.readDatagram(1024)
        senderAddress = senderAddress.toString()
        data = data.decode("utf-8")
        if senderAddress == self.clientIp.text():
            if data == '$#*--imonline--*#$':
                palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkGreen)
                self.timer_clientCheck.start(4000)
                self.label_3.setText("Client is online")
                self.label_3.setPalette(palette)
            elif data == '$#*--imoffline--*#$':
                palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkRed)
                self.label_3.setText("Client is offline")
                self.label_3.setPalette(palette)
                self.timer_clientCheck.stop()
            else:
                self.update_list(data)

    def send_datagram(self, message):
        send = QUdpSocket()
        send.writeDatagram(message, QHostAddress(self.clientIp.text()), self.clientPort.value())


    def update_my_status_online(self):
        testmsg = '$#*--imonline--*#$'
        self.send_datagram(testmsg)

    def update_my_status_offline(self):
        testmsg = '$#*--imoffline--*#$'
        self.send_datagram(testmsg)

    def set_box_disabled(self):
        self.nickName.setDisabled(True)
        #self.hostIp.setDisabled(True)
        self.hostPort.setDisabled(True)
        self.clientIp.setDisabled(True)
        self.clientPort.setDisabled(True)

    def set_box_enabled(self):
        self.nickName.setDisabled(False)
        #self.hostIp.setDisabled(False)
        self.hostPort.setDisabled(False)
        self.clientIp.setDisabled(False)
        self.clientPort.setDisabled(False)

    def check_client_status(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkRed)
        self.label_3.setPalette(palette)
        if self.label_3.text() == "":
            self.label_3.setText("Client is offline")

    def check_parameters(self):
        if self.nickName.text() == '':
            self.progressBar.setValue(10)
            self.progressLbl.setText("Connecting failed!")
            self.info_box("Connection Refused", "Nick not set.")
            return 1
        elif self.clientIp.text() == '...':
            self.progressBar.setValue(10)
            self.progressLbl.setText("Connecting failed!")
            self.info_box("Connection Refused", "Client ip not set.")
            return 1
        elif self.hostIp.text() == '...':
            self.progressBar.setValue(10)
            self.progressLbl.setText("Connecting failed!")
            self.info_box("Connection Refused", "Host ip not set.")
            return 1
        elif self.clientIp.text() != '...':
            IP = self.clientIp.text()
            IP = IP.split('.')
            for i in range(0, 4):
                if IP[i] == '':
                    self.info_box("Connection Refused", "Client ip incompletely.")
                    self.progressBar.setValue(10)
                    self.progressLbl.setText("Connecting failed!")
                    return 1
                    break
                elif self.hostIp.text() != '...':
                    IP = self.hostIp.text()
                    IP = IP.split('.')
            for i in range(0, 4):
                if IP[i] == '':
                    self.info_box("Connection Refused", "Host ip incompletely.")
                    self.progressBar.setValue(10)
                    self.progressLbl.setText("Connecting failed!")
                    return 1
                    break

    def start_server(self):
        self.progressBar.setVisible(True)
        self.progressLbl.setVisible(True)
        self.progressBar.setValue(2)
        if self.check_parameters() != 1:
            self.progressLbl.setText("Connecting...")
            self.progressBar.setValue(5)
            self.set_box_disabled()
            if (self.startServer.text() == "Connect"):
                self.server = QUdpSocket()
                error = self.server.bind(QHostAddress(self.hostIp.text()), self.hostPort.value())
                if (error == True):
                    self.update_my_status_online()
                    self.timer.start(3000)
                    self.timer_clientCheck.start(4000)
                    self.progressBarTimer.start(100)
                    self.timer2.setSingleShot(True)
                    self.timer2.start(300)
                    QtCore.QObject.connect(self.server, QtCore.SIGNAL('readyRead()'), self.read_message)
                    self.startServer.setText("Disconnect")
                elif (error == False):
                    self.info_box("Connection refused", "The Host Address or Host Port are currently unavailable.")
                    self.progressBar.setValue(10)
                    self.progressLbl.setText("Connecting failed!")
                    self.set_box_enabled()
            elif (self.startServer.text() == "Disconnect"):
                self.update_my_status_offline()
                self.server.close()
                self.set_box_enabled()
                self.startServer.setText("Connect")
                self.label_3.setText("")
                self.progressBarTimer.stop()
                self.timer2.stop()
                self.timer.stop()
                self.progressBar.setVisible(False)
                self.progressLbl.setVisible(False)
                self.timer_clientCheck.stop()

    def check_for_return(self):
        a = self.messageBox.toPlainText()
        a = str(a)
        x = len(a)
        if a != "":
            ascii = ord(a[x-1])
            if ascii == 10:
                self.sendButton.click()
        ##if x > 30:
          ##  self.message = a + 10

    def send_message(self):
        self.progressBar.setVisible(True)
        self.progressLbl.setText("Sending Message...")

        #preparing-for-sending
        message = self.messageBox.toPlainText()
        x = len(message)
        nick = self.nickName.text()
        msg = nick + ": \n"  + message
        self.progressBar.setValue(2)
        if self.startServer.text() == 'Connect':
            self.progressBar.setValue(10)
            self.progressLbl.setText("Sending Refused")
            self.info_box("Sending Refused", "Server not started.")


        elif message != '':

            self.progressBar.setValue(6)
            if self.label_3.text() == "" or self.label_3.text() == "Client is offline":
                self.info_box_advanced("Sending Unsuccessful","The message cannot be sent. \nWrong Client Ip or client not online.")
                self.progressBar.setValue(10)
                self.progressLbl.setText("Sending Failed!")
            else:
                self.messageBox.clear()
                self.myItemOnList(msg)
                self.send_datagram(msg)
                self.progressBar.setValue(10)
                self.progressLbl.setText("Message Sent!")
        elif message == '':
            self.progressBar.setValue(10)
            self.progressLbl.setText("Empty Message!")
#progressBar-work

    def progressBarInc(self):
        i = self.progressBar.value()
        i += 1
        self.progressBar.setValue(i)

    def checkProgressVal(self):
        if self.progressBar.value() == 10:
            self.update_my_status_online()
            self.progressBarTimer.stop()
            self.progressLbl.setText("Connected!")



def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWind()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()


