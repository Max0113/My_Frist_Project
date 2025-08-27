from tkinter import *
from tkinter import messagebox
import tkinter as tk
 
class super :
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700+30+10")
        self.root.title('Super-Market')
        self.root.resizable(False,False)

        title = Label(self.root,text="Welcome to Super-Market" ,fg="#ffffff",bg="#0B2F3A",font=("tajawal",12))
        title.pack(fill=X)

        # ______ données d'inscription _______

        Frame_Inscription = Frame(self.root, bg="#004D64" )
        Frame_Inscription.place(x=961,y=29,width=338,height=180)

        Title_Frame_IN = Label(Frame_Inscription,text=": بيانات المشتري",bg="#004D64" ,fg="#D4B100",font=("tajawal",12,"bold"))
        Title_Frame_IN.place(x=200,y=10)

        Title_Entry1_IN = Label(Frame_Inscription,text=": اسم المشترك",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry1_IN.place(x=200+20,y=50)
        Entry1_IN = Entry(Frame_Inscription,justify="center")
        Entry1_IN.place(x=70+25,y=50+5)


        Title_Entry2_IN = Label(Frame_Inscription,text=": رقم المشترك",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry2_IN.place(x=206+20,y=80)
        Entry2_IN = Entry(Frame_Inscription,justify="center")
        Entry2_IN.place(x=70+25,y=80+5)

        Title_Entry3_IN = Label(Frame_Inscription,text=": رقم الفاتورة",bg="#004D64" ,fg="#FFFFFF",font=("tajawal",12))
        Title_Entry3_IN.place(x=217+20,y=110)
        Entry3_IN = Entry(Frame_Inscription,justify="center")
        Entry3_IN.place(x=70+25,y=110+5)

        Button_IN = Button(Frame_Inscription,text="بحت",bg="#ffffff",fg="#000000",width=10,height=4)
        Button_IN.place(x=5+5,y=55+5)

        # ____________ BoxText _______________

        Title_TextBox = Label(Frame_Inscription,text="[الفواتير]" ,font=("tajawal",15,"bold") ,bg="#004D64",fg="#d4ff00")
        Title_TextBox.place(x=130,y=145)

        Frame_BoxText = Frame(self.root, bg="#FFFFFF" )
        Frame_BoxText.place(x=961,y=210,width=338,height=330)

        BoxText = tk.Text(Frame_BoxText , width=39 , height=20)
        BoxText.place(x=21,y=1)

        Scrollbar_BoxText = Scrollbar(Frame_BoxText,orient=VERTICAL, command=BoxText.yview)
        Scrollbar_BoxText.place(x=1,y=1,height=327)

        BoxText.config(yscrollcommand=Scrollbar_BoxText.set)

        BoxText.insert(END , """====================================
Name :
Phone :
num_bill :
====================================
Fatora :
rice : """)
        
        # __________ Price ______________

        Frame_Price = Frame(self.root,bg="#004D64")
        Frame_Price.place(x=619,y=543,height=156,width=680)

        Button1_Price = Button(Frame_Price,text="الحساب",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12))
        Button1_Price.place(x=470+80,y=30+6)

        Button2_Price = Button(Frame_Price,text="افراغ الحقول",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12))
        Button2_Price.place(x=400-50+80,y=30+6)

        Button3_Price = Button(Frame_Price,text="تصدير الفاتورة",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12))
        Button3_Price.place(x=470+80,y=80+6)

        Button4_Price = Button(Frame_Price,text="اغلاق البرنامج",bg="#D4B100",fg="#000000",height=1,width=13,font=("tajawal",12))
        Button4_Price.place(x=400-50+80,y=80+6)
        
        Title1_Price = Label(Frame_Price,text="حساب الكلي للبقوليات",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=180+40,y=36)

        Title1_Price = Label(Frame_Price,text="حساب اللوازم المنزلية",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=183+40,y=36+30)

        Title1_Price = Label(Frame_Price,text="حساب ادوات الكهرباء",bg="#004D64",fg="#D4B100",font=("tajawal",11,"bold") )
        Title1_Price.place(x=185+40,y=36+60)

        Entry1_Price = Entry(Frame_Price, justify="center")
        Entry1_Price.place(x=40,y=40,width=150)

        Entry1_Price = Entry(Frame_Price, justify="center")
        Entry1_Price.place(x=40,y=73,width=150)

        Entry1_Price = Entry(Frame_Price, justify="center")
        Entry1_Price.place(x=40,y=106,width=150)

        # _________ Legumes ________

        Frame_Legumes = Frame(self.root,bg="#004D64")
        Frame_Legumes.place(x=5,y=29,height=670,width=300)

        Title_Legumes = Label(Frame_Legumes,text="البقوليات",bg="#004D64",fg="#C7D503",font=("tajawal",15,"bold"))
        Title_Legumes.pack()

        Text1_Legumes = Label(Frame_Legumes,text=" : الرز",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text1_Legumes.place(x=210+30,y=50)
        Entry1_Legumes = Entry(Frame_Legumes,justify="center")
        Entry1_Legumes.place(x=40,y=54,width=100)

        Text2_Legumes = Label(Frame_Legumes,text=" : برغل",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text2_Legumes.place(x=196+30,y=50+30)
        Entry2_Legumes = Entry(Frame_Legumes,justify="center")
        Entry2_Legumes.place(x=40,y=54+30,width=100)

        Text3_Legumes = Label(Frame_Legumes,text=" : الفاصولياء",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text3_Legumes.place(x=191,y=50+60)
        Entry3_Legumes = Entry(Frame_Legumes,justify="center")
        Entry3_Legumes.place(x=40,y=54+60,width=100)

        Text4_Legumes = Label(Frame_Legumes,text=" : عدس",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text4_Legumes.place(x=220,y=50+90)
        Entry4_Legumes = Entry(Frame_Legumes,justify="center")
        Entry4_Legumes.place(x=40,y=54+90,width=100)

        Text5_Legumes = Label(Frame_Legumes,text=" : معكرونة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text5_Legumes.place(x=200,y=50+120)
        Entry5_Legumes = Entry(Frame_Legumes,justify="center")
        Entry5_Legumes.place(x=40,y=54+120,width=100)

        Text6_Legumes = Label(Frame_Legumes,text=" : فريكة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text6_Legumes.place(x=220,y=50+150)
        Entry6_Legumes = Entry(Frame_Legumes,justify="center")
        Entry6_Legumes.place(x=40,y=54+150,width=100)

        Text7_Legumes = Label(Frame_Legumes,text=" : حمض",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text7_Legumes.place(x=215,y=50+180)
        Entry7_Legumes = Entry(Frame_Legumes,justify="center")
        Entry7_Legumes.place(x=40,y=54+180,width=100)


        Text8_Legumes = Label(Frame_Legumes,text=" : فول",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text8_Legumes.place(x=225,y=50+230)
        Entry8_Legumes = Entry(Frame_Legumes,justify="center")
        Entry8_Legumes.place(x=40,y=54+230,width=100)

        Text9_Legumes = Label(Frame_Legumes,text=" : الملح",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text9_Legumes.place(x=217,y=50+260)
        Entry9_Legumes = Entry(Frame_Legumes,justify="center")
        Entry9_Legumes.place(x=40,y=54+260,width=100)

        Text10_Legumes = Label(Frame_Legumes,text=" : سكر",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text10_Legumes.place(x=220,y=50+290)
        Entry10_Legumes = Entry(Frame_Legumes,justify="center")
        Entry10_Legumes.place(x=40,y=54+290,width=100)

        Text11_Legumes = Label(Frame_Legumes,text=" : فلفل اسود",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text11_Legumes.place(x=176,y=50+340)
        Entry11_Legumes = Entry(Frame_Legumes,justify="center")
        Entry11_Legumes.place(x=40,y=54+340,width=100)

        Text12_Legumes = Label(Frame_Legumes,text=" : فلفل احمر",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text12_Legumes.place(x=180,y=50+370)
        Entry12_Legumes = Entry(Frame_Legumes,justify="center")
        Entry12_Legumes.place(x=40,y=54+370,width=100)

        Text13_Legumes = Label(Frame_Legumes,text=" : اللوبيا",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text13_Legumes.place(x=210,y=50+400)
        Entry13_Legumes = Entry(Frame_Legumes,justify="center")
        Entry13_Legumes.place(x=40,y=54+400,width=100)

        Text14_Legumes = Label(Frame_Legumes,text=" : الادمامي",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text14_Legumes.place(x=190,y=50+460)
        Entry14_Legumes = Entry(Frame_Legumes,justify="center")
        Entry14_Legumes.place(x=40,y=54+460,width=100)

        Text15_Legumes = Label(Frame_Legumes,text=" : القمح",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text15_Legumes.place(x=205,y=50+490)
        Entry15_Legumes = Entry(Frame_Legumes,justify="center")
        Entry15_Legumes.place(x=40,y=54+490,width=100)

        Text16_Legumes = Label(Frame_Legumes,text=" : الشعير",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text16_Legumes.place(x=195,y=50+520)
        Entry16_Legumes = Entry(Frame_Legumes,justify="center")
        Entry16_Legumes.place(x=40,y=54+520,width=100)

        Text17_Legumes = Label(Frame_Legumes,text=" : الشوفان",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text17_Legumes.place(x=182,y=50+570)
        Entry17_Legumes = Entry(Frame_Legumes,justify="center")
        Entry17_Legumes.place(x=40,y=54+570,width=100)

        # _________ Supplies ________

        Frame_Supplies = Frame(self.root,bg="#004D64")
        Frame_Supplies.place(x=312,y=29,height=670,width=300)

        Title_Supplies = Label(Frame_Supplies,text="اللوازم المنزلي",bg="#004D64",fg="#C7D503",font=("tajawal",15,"bold"))
        Title_Supplies.pack()

        Text1_Supplies = Label(Frame_Supplies,text=" : مصفاة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text1_Supplies.place(x=212,y=50)
        Entry1_Supplies = Entry(Frame_Supplies,justify="center")
        Entry1_Supplies.place(x=40,y=54,width=100)

        Text2_Supplies = Label(Frame_Supplies,text=" : صحن",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text2_Supplies.place(x=196+26,y=50+30)
        Entry2_Supplies = Entry(Frame_Supplies,justify="center")
        Entry2_Supplies.place(x=40,y=54+30,width=100)

        Text3_Supplies = Label(Frame_Supplies,text=" : كآس",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text3_Supplies.place(x=196+26,y=50+60)
        Entry3_Supplies = Entry(Frame_Supplies,justify="center")
        Entry3_Supplies.place(x=40,y=54+60,width=100)

        Text4_Supplies = Label(Frame_Supplies,text=" : ابريق",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text4_Supplies.place(x=222,y=50+90)
        Entry4_Supplies = Entry(Frame_Supplies,justify="center")
        Entry4_Supplies.place(x=40,y=54+90,width=100)

        Text5_Supplies = Label(Frame_Supplies,text=" : سكين",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text5_Supplies.place(x=212,y=50+120)
        Entry5_Supplies = Entry(Frame_Supplies,justify="center")
        Entry5_Supplies.place(x=40,y=54+120,width=100)

        Text6_Supplies = Label(Frame_Supplies,text=" : شوك",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text6_Supplies.place(x=215,y=50+150)
        Entry6_Supplies = Entry(Frame_Supplies,justify="center")
        Entry6_Supplies.place(x=40,y=54+150,width=100)

        Text7_Supplies = Label(Frame_Supplies,text=" : طنجرة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text7_Supplies.place(x=210,y=50+180)
        Entry7_Supplies = Entry(Frame_Supplies,justify="center")
        Entry7_Supplies.place(x=40,y=54+180,width=100)


        Text8_Supplies = Label(Frame_Supplies,text=" : سلة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text8_Supplies.place(x=225,y=50+230)
        Entry8_Supplies = Entry(Frame_Supplies,justify="center")
        Entry8_Supplies.place(x=40,y=54+230,width=100)

        Text9_Supplies = Label(Frame_Supplies,text=" : ملاعق",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text9_Supplies.place(x=212,y=50+260)
        Entry9_Supplies = Entry(Frame_Supplies,justify="center")
        Entry9_Supplies.place(x=40,y=54+260,width=100)

        Text10_Supplies = Label(Frame_Supplies,text=" : صينية",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text10_Supplies.place(x=214,y=50+290)
        Entry10_Supplies = Entry(Frame_Supplies,justify="center")
        Entry10_Supplies.place(x=40,y=54+290,width=100)

        Text11_Supplies = Label(Frame_Supplies,text=" : وعاء الخلط",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text11_Supplies.place(x=176,y=50+340)
        Entry11_Supplies = Entry(Frame_Supplies,justify="center")
        Entry11_Supplies.place(x=40,y=54+340,width=100)

        Text12_Supplies = Label(Frame_Supplies,text=" : فتاحة العلب",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text12_Supplies.place(x=170,y=50+370)
        Entry12_Supplies = Entry(Frame_Supplies,justify="center")
        Entry12_Supplies.place(x=40,y=54+370,width=100)

        Text13_Supplies = Label(Frame_Supplies,text=" : مقشرة",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text13_Supplies.place(x=200,y=50+400)
        Entry13_Supplies = Entry(Frame_Supplies,justify="center")
        Entry13_Supplies.place(x=40,y=54+400,width=100)

        Text14_Supplies = Label(Frame_Supplies,text=" : الادمامي",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text14_Supplies.place(x=190,y=50+460)
        Entry14_Supplies = Entry(Frame_Supplies,justify="center")
        Entry14_Supplies.place(x=40,y=54+460,width=100)

        Text15_Supplies = Label(Frame_Supplies,text=" : القمح",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text15_Supplies.place(x=205,y=50+490)
        Entry15_Supplies = Entry(Frame_Supplies,justify="center")
        Entry15_Supplies.place(x=40,y=54+490,width=100)

        Text16_Supplies = Label(Frame_Supplies,text=" : الشعير",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text16_Supplies.place(x=195,y=50+520)
        Entry16_Supplies = Entry(Frame_Supplies,justify="center")
        Entry16_Supplies.place(x=40,y=54+520,width=100)

        Text17_Supplies = Label(Frame_Supplies,text=" : الشوفان",bg="#004D64",fg="#ffffff",font=("tajawal",12))
        Text17_Supplies.place(x=182,y=50+570)
        Entry17_Supplies = Entry(Frame_Supplies,justify="center")
        Entry17_Supplies.place(x=40,y=54+570,width=100)



        


        self.root.mainloop()


        

ob = super()

        
        