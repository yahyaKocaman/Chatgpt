
from PyQt5 import QtCore, QtGui, QtWidgets
from concurrent.futures import thread
import sys
from threading import Thread
from datetime import datetime
import openai

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1211, 601))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1040, 610, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDefault(True)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 610, 1031, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 21))
        self.menubar.setObjectName("menubar")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOturumu_Ba_lat = QtWidgets.QAction(MainWindow)
        self.actionOturumu_Ba_lat.setObjectName("actionOturumu_Ba_lat")
        self.actionEkran_Temizle = QtWidgets.QAction(MainWindow)
        self.actionEkran_Temizle.setObjectName("actionEkran_Temizle")
        self.actionYaz_lanlar_Kaydet = QtWidgets.QAction(MainWindow)
        self.actionYaz_lanlar_Kaydet.setObjectName("actionYaz_lanlar_Kaydet")
        self.actionYaz_lanlar_Kaydet.setShortcut("Ctrl+S")
        self.actionYaz_lanlar_Kaydet.setStatusTip('Save File')

        self.menuAyarlar.addAction(self.actionOturumu_Ba_lat)
        self.menuAyarlar.addAction(self.actionEkran_Temizle)
        self.menuAyarlar.addAction(self.actionYaz_lanlar_Kaydet)

        self.menubar.addAction(self.menuAyarlar.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatGpt"))
        self.pushButton.setText(_translate("MainWindow", "Gönder"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.actionOturumu_Ba_lat.setText(_translate("MainWindow", "Oturumu Başlat"))
        self.actionEkran_Temizle.setText(_translate("MainWindow", "Ekranı Temizle"))
        self.actionYaz_lanlar_Kaydet.setText(_translate("MainWindow", "Yazılanları Kaydet"))

        

class mainjob(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainjob,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.msgsender)
        self.ui.actionEkran_Temizle.triggered.connect(self.ekrantemizle)    
        self.ui.actionYaz_lanlar_Kaydet.triggered.connect(self.konusmakaydet)
        self.ui.lineEdit.returnPressed.connect(self.msgsender)
        openai.api_key = "apikey"
        self.komut = "First command"
        self.konusmagecmisi = [{"role": "system", "content": self.komut}]




    def msgsender(self):
        
        def baslat():
            alinanicerek=self.ui.lineEdit.text()
            self.ui.textEdit.append("Siz: "+alinanicerek)

            self.ui.lineEdit.clear()


            ekle={"role": "user", "content": alinanicerek}

            self.konusmagecmisi.append(ekle)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.konusmagecmisi
            )
 
            answer = response.choices[0]['message']['content']
            self.ui.textEdit.append("ChatGPT: "+str(answer))
            self.konusmagecmisi.append({"role": "assistant", "content": answer})

        islem=Thread(target=baslat)
        islem.start()

       


    def ekrantemizle(self):
        self.ui.textEdit.clear()


    def konusmakaydet(self):
        

        file , check = QtWidgets.QFileDialog.getSaveFileName(None, "QFileDialog getSaveFileName() Demo",
                                               "", "Text Files (*.txt)")
        with open(file,"w",encoding="utf-8") as file:
            file.write(self.ui.textEdit.toPlainText())
        print("Konuşma Kaydedildi") 

    def durdur(self):
        pass

    def konusmabaslat(self): 
        pass       

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = mainjob()
    win.show()
    sys.exit(app.exec_())

app()
