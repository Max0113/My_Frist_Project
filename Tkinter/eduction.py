from tkinter import *

class MyApp:
    def __init__(self, root):
        self.ID_var = StringVar()  # متغير نصوص

        Label(root, text="أدخل الـ ID:").pack()
        Entry(root, textvariable=self.ID_var).pack()

        Button(root, text="عرض القيمة", command=self.show_value).pack()

    def show_value(self):
        print("القيمة المدخلة:", self.ID_var.get())  # الحصول على النص

root = Tk()
app = MyApp(root)
root.mainloop()



