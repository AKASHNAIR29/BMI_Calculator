import datetime
from tkinter import *
from tkinter.messagebox import *
from datetime import datetime
from tkinter.ttk import Label
from sqlite3 import *
from tkinter.scrolledtext import *
import pandas as pd



def f1():
    bmi.deiconify()
    main_window.withdraw()


def f2():
    main_window.deiconify()
    bmi.withdraw()


def f3():
    convert_window.deiconify()
    main_window.withdraw()


def convert_bmi():
    convert_lbl_feet = int(convert_ent_feet.get())
    convert_lbl_inches = int(convert_ent_inches.get())
    in_m = convert_lbl_feet/3.28084 + convert_lbl_inches/39.3701
    x = round(in_m, 2)
    showinfo('Meters', f'meters = {x}')


def calculate_bmi():
    kg = float(bmi_ent_weight.get())
    m = float(bmi_ent_height.get())
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    con = None
    try:
        con = connect("bmi.db")
        cursor = con.cursor()
        sql = "insert into bmi values('%s','%d','%d','%s','%f','%d','%d')"
        name = bmi_ent_name.get()
        age = int(bmi_ent_age.get())
        phone = int(bmi_ent_phone.get())
        if a.get() == 1:
            gender = "Male"
        else:
            gender = "Female"
        height = float(bmi_ent_height.get())
        weight = int(bmi_ent_weight.get())
        cursor.execute(sql % (name, age, phone, gender, height, weight, bmi))
        con.commit()
    except Exception as e:
        print("Failure", e)
    finally:
        if con is not None:
            con.close()
        if bmi < 18.5:
            showinfo(
                'BMI', f'Name = {name}\nAge = {age}\nPhone = {phone}\nGender = {gender}\nBMI = {bmi} is Underweight')
        elif (bmi > 18.5) and (bmi < 24.9):
            showinfo(
                'BMI', f'Name = {name}\nAge = {age}\nPhone = {phone}\nGender = {gender}\nBMI = {bmi} is Normal')
        elif (bmi > 24.9) and (bmi < 29.9):
            showinfo(
                'BMI', f'Name = {name}\nAge = {age}\nPhone = {phone}\nGender = {gender}\nBMI = {bmi} is Overweight')
        elif (bmi > 29.9):
            showinfo(
                'BMI', f'Name = {name}\nAge = {age}\nPhone = {phone}\nGender = {gender}\nBMI = {bmi} is Obesity')
        else:
            showerror('BMI', 'something went wrong!')

    bmi_ent_name.delete(0, END)
    bmi_ent_age.delete(0, END)
    bmi_ent_phone.delete(0, END)
    bmi_ent_height.delete(0, END)
    bmi_ent_weight.delete(0, END)


def f4():
    main_window.deiconify()
    view.withdraw()


def f5():
    view.deiconify()
    main_window.withdraw()
    view_bmi_data.delete(1.0, END)
    info = ""
    con = None
    try:
        con = connect('bmi.db')
        cursor = con.cursor()
        sql = "select * from bmi"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            info = info + "Name = " + str(d[0])+"\n" + "Age = " + str(d[1])+"\n"+"Phone = " + str(
                d[2])+"\n"+"Gender = " + str(d[3])+"\n" + "BMI = " + str(float(d[6])) + "\n" + ("*" * 50)+"\n"
        view_bmi_data.insert(INSERT, info)
    except Exception as e:
        showerror('Failure', e)
        con.rollback()
    finally:
        if con is not None:
            con.close()


con = None
try:
    con = connect('bmi.db')
    cursor = con.cursor()
    sql = "select * from bmi"
    data = (len(cursor.execute(sql).fetchall()))
except Exception as e:
    print('Failure', e)
    con.rollback()
finally:
    if con is not None:
        con.close()


def f6():
    main_window.deiconify()
    convert_window.withdraw()


def f7():
    if askokcancel("Quit", "Click OK to Quit"):
        main_window.destroy()


def f8():
    pid = []
    name = []
    age = []
    phone = []
    gender = []
    bmi = []
    con = None
    try:
        con = connect('bmi.db')
        cursor = con.cursor()
        sql = "select * from bmi"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            pid
            name.append(d[0])
            age.append(d[1])
            phone.append(d[2])
            gender.append(d[3])
            bmi.append(d[6])
    except Exception as e:
        showerror('Failure', e)
        con.rollback()
    finally:
        if con is not None:
            con.close()
    d = {'Name': (name), 'Age': (age), 'Phone': (
        phone), 'Gender': (gender), 'Bmi': (bmi)}
    df = pd.DataFrame(d, columns=["Name", "Age", "Phone", "Gender", "Bmi"])
    df.index += 1
    df.to_csv(r'E:\KAMAL CLASSES\MYSQL\PROJECT\BMI_Calculator\export_dataframe.csv',
              index_label='Pid')


con = None
try:
    con = connect('bmi.db')
    cursor = con.cursor()
    sql = "select * from bmi"
    data = (len(cursor.execute(sql).fetchall()))
except Exception as e:
    print('Failure', e)
    con.rollback()
finally:
    if con is not None:
        con.close()


now = datetime.datetime.now()
p = str(now)

hour = datetime.datetime.now().hour
greeting = "Good morning" if 5 <= hour < 12 else "Good afternoon" if hour < 17 else "Good evening"

splash = Tk()
splash.after(4000, splash.destroy)
splash.wm_attributes('-fullscreen', 'true')
splash.title("Welcome")
splash.resizable(True, False)
msg = Label(splash, text="\nBMI Calculator \n           By \n    Akash Nair",font=('Calibri', 90, 'italic'))
msg.pack()
splash.mainloop()

# ----------------------------------- main window ------------------------------------------
main_window = Tk()
main_window.title("BMI Calculator")
main_window.geometry("800x500+500+150")
#main_window.resizable(True, False)
main_window.configure(background="yellow")

lbl_date = Label(main_window, text=p + "\n " +
                 "{}".format(greeting), font=('arial', 20, 'bold'))
lbl_date.pack(pady=20)

b1 = Button(main_window, text="Calculate BMI",
            command=f1, font=('arial', 20, 'bold'))
b1.pack(pady=20)
b2 = Button(main_window, text="View History",
            command=f5, font=('arial', 20, 'bold'))
b2.pack(pady=20)
b3 = Button(main_window, text="Export Data",
            command=f8, font=('arial', 20, 'bold'))
b3.pack(pady=20)

lbl_count = Label(main_window, text="Count =  " +
                  "{}".format(data), font=('arial', 20, 'bold'))
lbl_count.pack(pady=20)

# ----------------------------------- bmi window ------------------------------------------
bmi = Toplevel(main_window)
bmi.title("BMI")
bmi.geometry("800x500+400+100")
bmi.configure(background="light blue")
bmi.withdraw()

bmi_lbl_name = Label(bmi, text="enter name", font=('arial', 20, 'bold'))
bmi_ent_name = Entry(bmi, bd=3, font=('arial', 20, 'bold'))
bmi_lbl_age = Label(bmi, text="enter age", font=('arial', 20, 'bold'))
bmi_ent_age = Entry(bmi, bd=3, font=('arial', 20, 'bold'))
bmi_lbl_phone = Label(bmi, text="enter phone", font=('arial', 20, 'bold'))
bmi_ent_phone = Entry(bmi, bd=3, font=('arial', 20, 'bold'))

a = IntVar()

bmi_lbl_gender = Label(bmi, text="Gender", font=('arial', 20, 'bold'))
rb_male = Radiobutton(bmi, text="Male", font=(
    'arial', 18, 'bold'), variable=a, value=1)
rb_female = Radiobutton(bmi, text="Female", font=(
    'arial', 18, 'bold'), variable=a, value=2)
bmi_lbl_height = Label(bmi, text="enter height in mtr",
                       font=('arial', 20, 'bold'))
bmi_ent_height = Entry(bmi, bd=3, font=('arial', 20, 'bold'))
bmi_lbl_weight = Label(bmi, text="enter weight in kg",
                       font=('arial', 20, 'bold'))
bmi_ent_weight = Entry(bmi, bd=3, font=('arial', 20, 'bold'))

bmi_btn_convert = Button(bmi, text="Convert", font=(
    'arial', 20, 'bold'), command=f3)
bmi_btn_cal = Button(bmi, text="Calculate", font=(
    'arial', 20, 'bold'), command=calculate_bmi)
bmi_btn_back = Button(bmi, text="Back", font=('arial', 20, 'bold'), command=f2)

bmi_lbl_name.place(x=10, y=10)
bmi_ent_name.place(x=300, y=10)
bmi_lbl_age.place(x=10, y=70)
bmi_ent_age.place(x=300, y=70)
bmi_lbl_phone.place(x=10, y=130)
bmi_ent_phone.place(x=300, y=130)
bmi_lbl_gender.place(x=10, y=190)
rb_male.place(x=300, y=190)
rb_female.place(x=500, y=190)
bmi_lbl_height.place(x=10, y=250)
bmi_ent_height.place(x=300, y=250)
bmi_btn_convert.place(x=650, y=250)
bmi_lbl_weight.place(x=10, y=330)
bmi_ent_weight.place(x=300, y=330)
bmi_btn_cal.place(x=40, y=400)
bmi_btn_back.place(x=200, y=400)

# ----------------------------------- convert window ------------------------------------------
convert_window = Toplevel(bmi)
convert_window.title("Convert")
convert_window.geometry("800x500+400+100")
convert_window.configure(background="light green")
convert_window.withdraw()

convert_lbl_height = Label(
    convert_window, text="Enter your height:", font=('arial', 22, 'bold'))
convert_lbl_feet = Label(convert_window, text="Feet:",
                         font=('arial', 22, 'bold'))
convert_ent_feet = Entry(convert_window, bd=3, width=30,
                         font=('arial', 22, 'bold'))
convert_lbl_inches = Label(
    convert_window, text="Inches:", font=('arial', 22, 'bold'))
convert_ent_inches = Entry(
    convert_window, bd=3, width=30, font=('arial', 22, 'bold'))
convert_btn_convert = Button(convert_window, text="Convert", font=(
    'arial', 22, 'bold'), command=convert_bmi)
convert_window_btn_back = Button(convert_window, text="Back", font=(
    'Cambria', 20, 'bold'), width=10, command=f6)

convert_lbl_height.pack(pady=20)
convert_lbl_feet.pack(pady=20)
convert_ent_feet.pack(pady=20)
convert_lbl_inches.pack(pady=20)
convert_ent_inches.pack(pady=20)
convert_btn_convert.pack(pady=20)
convert_window_btn_back.pack(pady=10)
convert_window.withdraw()

# ----------------------------------- view window ------------------------------------------
view = Toplevel(main_window)
view.title("View")
view.geometry("800x500+400+100")
view.configure(background="light blue")

view_bmi_data = ScrolledText(
    view, width=40, height=10, font=('arial', 20, 'bold'))
view_btn_back = Button(view, text="Back", font=(
    'arial', 20, 'bold'), width=10, command=f4)
view_bmi_data.pack(pady=10)
view_btn_back.pack(pady=10)
view.withdraw()

# ----------------------------------- export data ------------------------------------------
export = Toplevel(main_window)
export.title("csv.")
export.geometry("700x500+400+100")

export_bmi_data = ScrolledText(
    export, width=40, height=10, font=('Cambria', 20, 'bold'))
export_btn_back = Button(export, text="Back", font=(
    'Cambria', 20, 'bold'), width=10, command=f8)
export_bmi_data.pack(pady=10)
export_btn_back.pack(pady=10)
export.withdraw()

main_window.protocol("WM_DELETE_WINDOW", f7)
main_window.mainloop()
