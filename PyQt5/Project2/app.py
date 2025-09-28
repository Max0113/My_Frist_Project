from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import sys
import yt_dlp

From_Class, _ = loadUiType(path.join(path.dirname(__file__), "untitled.ui"))

class mainloop(QWidget, From_Class):
    def __init__(self, parent=None):
        super(mainloop, self).__init__(parent)
        self.setupUi(self) 
        self.Window() 
        self.Button()

    def Window(self):
        self.setFixedSize(793, 499)

    def Button(self):
        self.pushButton.clicked.connect(self.But_Download_DV)
        self.pushButton_2.clicked.connect(self.Browse_DV)

        self.pushButton_4.clicked.connect(self.But_Download_DP)
        self.pushButton_3.clicked.connect(self.Browse_DP)



    # ________Downlode Youtube Video Methode________

    def Browse_DV(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Save Location")
        if folder:
            self.lineEdit_2.setText(folder)

    def progress_hook_DV(self, d):
        if d['status'] == 'downloading':
            if d.get('total_bytes'):
                percent = d['downloaded_bytes'] * 100 / d['total_bytes']
                QApplication.processEvents()
            else:
                percent = 0
                QApplication.processEvents()

            self.progressBar.setValue(int(percent))
            QApplication.processEvents()

        elif d['status'] == 'finished':
            self.progressBar.setValue(100)

    def But_Download_DV(self):
        Text_URL = self.lineEdit.text()
        Text_Location = self.lineEdit_2.text()

        if not Text_URL or not Text_Location :
            QMessageBox.warning(self, "Error", "Please provide both URL and Save Location")
            return

        ydl_opts = {
            'format': 'best',
            'progress_hooks': [self.progress_hook_DV],
            'outtmpl': f'{Text_Location}/%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([Text_URL])

        except Exception as e :
            QMessageBox.critical(self, "Download Error", str(e))

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.progressBar.setValue(0)
    
    # ________Downlode Youtube Plyalist Methode________

    def Browse_DP(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Save Location")
        if folder :
            self.lineEdit_4.setText(folder)

    def progress_hook_DP(self, d):
        if d['status'] == 'downloading':
            if d.get('total_bytes'):
                percent = d['downloaded_bytes'] * 100 / d['total_bytes']
                QApplication.processEvents()
            else:
                percent = 0
                QApplication.processEvents()

            self.progressBar_2.setValue(int(percent))
            QApplication.processEvents()

        elif d['status'] == 'finished':
            self.progressBar_2.setValue(100)

    def But_Download_DP(self):
        Text_URL = self.lineEdit_3.text()
        Text_Location = self.lineEdit_4.text()

        if not Text_URL or not Text_Location :
            QMessageBox.warning(self, "Error", "Please provide both URL and Save Location")
            return

        ydl_opts = {
            'format': 'best',
            'progress_hooks': [self.progress_hook_DP],
            'outtmpl': f'{Text_Location}/%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([Text_URL])

        except Exception as e :
            QMessageBox.critical(self, "Download Error", str(e))

        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.progressBar_2.setValue(0)

def main():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)  
    app.setStyle("Fusion")                         
    w = mainloop()  
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
