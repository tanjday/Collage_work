# Student Management System - simple Tkinter GUI
# Run: python app.py   (students are saved in students.json)

import json
import os
from tkinter import *
from tkinter import messagebox  

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


def load():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def save(students):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


students = load()   # every student, in a list


# ---------- buttons ----------

def show():
    listbox.delete(0, END)
    for s in students:
        listbox.insert(END, s["roll"] + " | " + s["name"] + " | " + s["department"] + " | " + s["email"])


def add():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    dept = dept_entry.get().strip()
    email = email_entry.get().strip()

    if name == "" or roll == "" or dept == "" or email == "":
        messagebox.showerror(title="Error", message="Please fill in all four fields: name, roll number, department, email.")
        return
    if "@" not in email:
        messagebox.showerror(title="Error", message="Email does not look valid.")
        return
    for s in students:
        if s["roll"] == roll:
            messagebox.showerror(title="Error", message="Roll number " + roll + " already exists.")
            return

    students.append({"name": name, "roll": roll, "department": dept, "email": email})
    save(students)
    show()
    clear()


def delete():
    for index in reversed(listbox.curselection()):
        students.pop(index)
    save(students)
    show()


def clear():
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    dept_entry.delete(0, END)
    email_entry.delete(0, END)


# ---------- window ----------

window = Tk()
window.title("Student Management System")
window.config(bg="#121212")

title = Label(window, text="Student Management System", font=("Consolas", 20, "bold"))
title.config(bg="#121212", fg="#e8e8e8")
title.pack(pady=10)

name_label = Label(window, text="name")
name_label.config(bg="#121212", fg="#e8e8e8")
name_label.pack()

name_entry = Entry(window, width=45)
name_entry.config(bg="#1e1e1e", fg="#e8e8e8", insertbackground="#e8e8e8")
name_entry.pack(pady=2)

roll_label = Label(window, text="roll number")
roll_label.config(bg="#121212", fg="#e8e8e8")
roll_label.pack()

roll_entry = Entry(window, width=45)
roll_entry.config(bg="#1e1e1e", fg="#e8e8e8", insertbackground="#e8e8e8")
roll_entry.pack(pady=2)

dept_label = Label(window, text="department")
dept_label.config(bg="#121212", fg="#e8e8e8")
dept_label.pack()

dept_entry = Entry(window, width=45)
dept_entry.config(bg="#1e1e1e", fg="#e8e8e8", insertbackground="#e8e8e8")
dept_entry.pack(pady=2)

email_label = Label(window, text="email")
email_label.config(bg="#121212", fg="#e8e8e8")
email_label.pack()

email_entry = Entry(window, width=45)
email_entry.config(bg="#1e1e1e", fg="#e8e8e8", insertbackground="#e8e8e8")
email_entry.pack(pady=2)

frame = Frame(window)
frame.config(bg="#121212")
frame.pack(pady=8)

add_button = Button(frame, text="add", command=add)
add_button.config(bg="#2563eb", fg="white")
add_button.pack(side=LEFT, padx=4)

delete_button = Button(frame, text="delete", command=delete)
delete_button.config(bg="#b91c1c", fg="white")
delete_button.pack(side=LEFT, padx=4)

clear_button = Button(frame, text="clear", command=clear)
clear_button.config(bg="#333333", fg="#e8e8e8")
clear_button.pack(side=LEFT, padx=4)

listbox = Listbox(window, width=70, height=12, selectmode=MULTIPLE)
listbox.config(bg="#1e1e1e", fg="#e8e8e8", font=("Consolas", 12))
listbox.pack(pady=6)

show()

if __name__ == "__main__":
    window.mainloop()
