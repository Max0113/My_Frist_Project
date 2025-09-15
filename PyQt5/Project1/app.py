from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame , QLabel , QLineEdit , QPushButton , QCheckBox
import sys

print(sys.argv)

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(500, 500)
win.move(200, 200)
win.setWindowTitle("APP-YounesAmzil")
win.setStyleSheet("background-color:#ffffff")

# Icon (تأكد أن الملف .ico)
win.setWindowIcon(QtGui.QIcon("C:\\Users\\Gk\\Desktop\\favpng_22eeecf99b8d92726b4f3735be5473c0.png"))


# إنشاء QFrame
frame = QFrame(win)
frame.setGeometry(100, 90, 300, 320)  # position x, y, width, height

# تحديد style
frame.setFrameShape(QFrame.Box)        # شكل الإطار (Box, Panel, HLine, VLine…)
frame.setFrameShadow(QFrame.Raised)    # الظل (Raised, Sunken, Plain)
frame.setLineWidth(0)                            # سماكة الخط
frame.setStyleSheet("""
background-color: #000000;
color: #ffffff;
font-family : tajawal;
border-radius: 10px; 
""")

# إضافة عنصر داخل الـ frame (مثلا label)
label1 = QLabel("Email : ", frame)
label1.move(20, 20+60)
Entr1 = QLineEdit(frame)
Entr1.move(20, 50+60)
Entr1.resize(200,30)
Entr1.setStyleSheet("""
   background-color: #ffffff;
   border-radius: 5px;
   color : black;
                    """)

label2 = QLabel("Passowrd : ", frame)
label2.move(20, 90+60)
Entr2 = QLineEdit(frame)
Entr2.move(20, 120+60)
Entr2.resize(200,30)
Entr2.setStyleSheet("""
   background-color: #ffffff;
   border-radius: 5px;
   color : black;
""")

check1 = QCheckBox("accept",frame)
check1.move(20,170+60)

button1 = QPushButton("Login",frame)
button1.move(20,200+60)
button1.resize(100,30)
button1.setStyleSheet("""
   background-color: #ffffff;
   color: black;
   border-radius: 5px; 
""")

button2 = QPushButton("Inscription",frame)
button2.move(140,200+60)
button2.resize(100,30)
button2.setStyleSheet("""
   background-color: #ffffff;
   color: black;
   border-radius: 5px; 
""")

# Image 
Lable = QLabel(frame)
photo = QPixmap("C:\\Users\\Gk\\Desktop\\user.png")
Lable.setPixmap(photo)
Lable.move(120,20)
Lable.setStyleSheet("")

win.show()
app.exec_()   # إذا كنت PyQt5
# app.exec()  # إذا كنت PyQt6


