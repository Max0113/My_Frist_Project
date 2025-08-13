from tkinter import *
from tkinter import ttk

class student :
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x700")
        self.win.config(bg="#e6e6e6")
        self.win.title("student app")
        self.win.resizable(False,False)
        title = Label(self.win , text="نظام تسجيل الطلاب" ,bg="#0096b8" ,fg="#ffffff")
        title.pack(fill=X)
        # ----------- أدوات تحكم بالبرنامج --------------
        fram = Frame(self.win , bg="#ffffff")
        fram.place(x=1096,y=25,width=250,height=420)
        
        lbl_ID = Label(fram, text="الرقم التسلسلي" ,bg="#ffffff")
        lbl_ID.pack()
        ID_Entry = Entry(fram, bd=2 , justify="center")
        ID_Entry.pack()

        lbl_Name = Label(fram, text="اسم الطالب" ,bg="#ffffff")
        lbl_Name.pack()
        Name_Entry = Entry(fram, bd=2 , justify="center")
        Name_Entry.pack()

        lbl_Email = Label(fram, text="ايميل الطالب" ,bg="#ffffff")
        lbl_Email.pack()
        Email_Entry = Entry(fram, bd=2 , justify="center")
        Email_Entry.pack()

        lbl_Phone = Label(fram, text="هاتف الطالب" ,bg="#ffffff")
        lbl_Phone.pack()
        Phone_Entry = Entry(fram, bd=2 , justify="center")
        Phone_Entry.pack()

        lbl_Phone = Label(fram, text="هاتف الطالب" ,bg="#ffffff")
        lbl_Phone.pack()
        Phone_Entry = Entry(fram, bd=2 , justify="center")
        Phone_Entry.pack()

        lbl_qualifications = Label(fram, text="مؤهلات الطالب" ,bg="#ffffff")
        lbl_qualifications.pack()
        qualifications_Entry = Entry(fram, bd=2 , justify="center")
        qualifications_Entry.pack()

        lbl_Sex = Label(fram, text="جنس الطالب" ,bg="#ffffff")
        lbl_Sex.pack()
        array = ("male","famille")
        choasie = ttk.Combobox(fram,values=(array))
        choasie.pack()

        lbl_Addresse = Label(fram, text="عنوان الطالب" ,bg="#ffffff")
        lbl_Addresse.pack()
        Addresse_Entry = Entry(fram, bd=2 , justify="center")
        Addresse_Entry.pack()

        lbl_delete = Label(fram, text="حدف الطالب" ,bg="#ffffff" , fg="red")
        lbl_delete.pack()
        delete_Entry = Entry(fram, bd=2 , justify="center")
        delete_Entry.pack()

        # -------- Button ---------

        fram1 = Frame(self.win, bg="#ffffff")
        fram1.place(x=1096,y=450,width=250,height=243)

        title1 = Label(fram1,text="لوحة التحكم",bg="#2877ff" ,fg="#ffffff",font=("29LT Azer",15))
        title1.pack(fill=X)
        
        lbl_Button1 = Button(fram1,text="اضافة الطالب",width=20,bg="#949191" ,fg="#ffffff")
        lbl_Button1.pack(pady=5)

        lbl_Button2 = Button(fram1,text="حدف الطالب",width=20,bg="#949191",fg="#ffffff")
        lbl_Button2.pack(pady=5)

        lbl_Button3 = Button(fram1,text="تعديل بيانات الطالب",width=20,bg="#949191",fg="#ffffff")
        lbl_Button3.pack(pady=5)

        lbl_Button4 = Button(fram1,text="افراغ الحقول",width=20,bg="#949191",fg="#ffffff")
        lbl_Button4.pack(pady=5)

        lbl_Button5 = Button(fram1,text="من نحن",width=20,bg="#949191",fg="#ffffff")
        lbl_Button5.pack(pady=5)

        lbl_Button6 = Button(fram1,text="اغلاق البرنامج",width=20,bg="#949191",fg="#ffffff")
        lbl_Button6.pack(pady=5)


        # ---------- search bar -------------

        search_farm = Label(self.win,bg="#ffffff")
        search_farm.place(x=4,y=25,width=1087,height=52)

        text = Label(search_farm,text="البحث عن طالب",bg="#ffffff")
        text.place(x=980,y=12)
 
        array1 = ("id","name","email","phone")
        choasie = ttk.Combobox(search_farm,values=(array1))
        choasie.place(x=820,y=12)

        Search_Entry = Entry(search_farm, bd=2 , justify="left")
        Search_Entry.place(x=670,y=13)

        Search_Button = Button(search_farm, text="البحث",width=15,bg="#6bbaff")
        Search_Button.place(x=530,y=10)


win = Tk()
student1 = student(win)
win.mainloop()
        