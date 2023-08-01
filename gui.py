from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *


"""ВАЛИДАЦИЯ"""
def validating():
    try:
        sum = float(entrySum.get())
    except:
        messagebox.showwarning("Ошибка", "Некорректные данные: sum")
        return 0
    try:
        months = int(entryMonths.get())
    except:
        messagebox.showwarning("Ошибка", "Некорректные данные: months")
        return 0
    try:
        rate = float(entryRate.get())
    except:
        messagebox.showwarning("Ошибка", "Некорректные данные: rate")
        return 0

    if sum < 0:
        messagebox.showwarning("Ошибка", "Некорректные данные: sum")
        return 0
    if months < 0:
        messagebox.showwarning("Ошибка", "Некорректные данные: months")
        return 0
    if rate < 0 or rate > 100:
        messagebox.showwarning("Ошибка", "Некорректные данные: rate")
        return 0
    return 1


"""КРЕДИТНЫЙ КАЛЬКУЛЯТОР"""
def change_credit():
    for i in tree.get_children():
        tree.delete(i)

    if validating():
        sum, months, rate = float(entrySum.get()), int(entryMonths.get()), float(entryRate.get())

        ob = Bank(sum, months, rate)
        if button_type.get() == "diff":
            answer = ob.diff_int()
            overpayment = 0
            for a in answer:
                overpayment += a[-1]
                for i in range(len(a)):
                    if i != 0:
                        a[i] = "{:.2f}".format(a[i])
                tree.insert("", END, values=a)
            label3['text'] = f"Общая переплата: {round(overpayment - sum, 2)}"
        elif button_type.get() == "ann":
            answer = ob.ann_int()
            overpayment = 0
            for a in answer:
                overpayment += a[-1]
                for i in range(len(a)):
                    if i != 0:
                        a[i] = "{:.2f}".format(a[i])
                tree.insert("", END, values=a)
            label3['text'] = f"Общая переплата: {round(overpayment - sum, 2)}"


"""ДЕПОЗИТНЫЙ КАЛЬКУЛЯТОР"""
def change_deposit():
    for i in tree2.get_children():
        tree2.delete(i)

    if validating():
        sum, months, rate = float(entrySum.get()), int(entryMonths.get()), float(entryRate.get())

        ob = Bank(sum, months, rate)
        answer = ob.deposit()

        last = answer[-1][-1]
        for a in answer:
            for i in range(len(a)):
                if i != 0:
                    a[i] = "{:.2f}".format(a[i])
            tree2.insert("", END, values=a)

        label4['text'] = f"Итоговая сумма процентов: {round(last - sum, 2)}"
        label5['text'] = f"Общая сумма к выдаче: {last}"


"""GUI"""
root = Tk()
root.title("Калькуляторы")
root.geometry("1350x350")

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Кредитный калькулятор")

frame2 = Frame(notebook)
frame2.pack(fill=BOTH, expand=True)
notebook.add(frame2, text="Депозитный калькулятор")

label1 = Label()
label1['text'] = "Сумма в рублях:"
label1.place(x=20, y=50)

entrySum = Entry()
entrySum.insert(0, "350000")
entrySum.place(x=150, y=50)

label2 = Label()
label2['text'] = "Срок в месяцах:"
label2.place(x=20, y=100)

entryMonths = Entry()
entryMonths.insert(0, "9")
entryMonths.place(x=150, y=100)

label3 = Label()
label3['text'] = "Процентная ставка:"
label3.place(x=20, y=150)

entryRate = Entry()
entryRate.insert(0, "4.7")
entryRate.place(x=150, y=150)

# frame1
btn = ttk.Button(frame1, text="Посчитать", command=change_credit)
btn.place(x=20, y=170)

label3 = Label(frame1)
label3['text'] = "Общая переплата:"
label3.place(x=20, y=210)

button_type = StringVar()
button_type.set("diff")
button_diff = Radiobutton(frame1, text="Дифференцированный", value="diff", variable=button_type)
button_diff.place(x=20, y=250)
button_ann = Radiobutton(frame1, text="Аннуитетный", value="ann", variable=button_type)
button_ann.place(x=20, y=270)

columns = ("month", "sum", "first", "second", "full")
tree = ttk.Treeview(frame1, columns=columns, show="headings")
tree.place(x=300, y=30)

tree.column("month", anchor="e")
tree.column("sum", anchor="e")
tree.column("first", anchor="e")
tree.column("second", anchor="e")
tree.column("full", anchor="e")

tree.heading("month", text="Месяц")
tree.heading("sum", text="Остаток займа")
tree.heading("first", text="Основной платеж")
tree.heading("second", text="Проценты")
tree.heading("full", text="Итоговый платеж")

# frame2
btn = ttk.Button(frame2, text="Посчитать", command=change_deposit)
btn.place(x=20, y=170)

label4 = Label(frame2)
label4['text'] = "Итоговая сумма процентов:"
label4.place(x=20, y=210)

label5 = Label(frame2)
label5['text'] = "Общая сумма к выдаче:"
label5.place(x=20, y=230)

columns = ("month", "percent", "sum")
tree2 = ttk.Treeview(frame2, columns=columns, show="headings")
tree2.place(x=300, y=30)

tree2.column("month", anchor="e")
tree2.column("percent", anchor="e")
tree2.column("sum", anchor="e")

tree2.heading("month", text="Месяц")
tree2.heading("percent", text="Сумма начисленных %")
tree2.heading("sum", text="Остаток вклада после начисления %")

root.mainloop()
