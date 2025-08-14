import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("جدول بـ Treeview")
win.geometry("600x300")

# 1) إنشاء الـ Treeview مع الأعمدة
cols = ("ID", "الاسم", "العمر")
table = ttk.Treeview(win, columns=cols, show="headings", height=8)

# 2) عناوين الأعمدة + المقاسات
for c in cols:
    table.heading(c, text=c)
table.column("ID", width=60, anchor="center")
table.column("الاسم", width=200)
table.column("العمر", width=80, anchor="center")

# 3) إدخال بيانات
data = [
    (1, "أمين", 22),
    (2, "سارة", 19),
    (3, "ياسين", 25),
    (4, "خديجة", 21),
]
for row in data:
    table.insert("", "end", values=row)

table.pack(fill="both", expand=True)
win.mainloop()


