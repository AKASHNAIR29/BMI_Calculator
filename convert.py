from tkinter import*
from tkinter.messagebox import*

def f3():
	convert_window.deiconify()
	convert.withdraw()

def convert():
	bmi_inch=float(bmi_ent_inch.get())
	bmi_feet=float(bmi_ent_feet.get())															
	bmi_ent_height=bmi_inch/0.0254
	bmi_ent_height=bmi_feet/0.305

	x = round(bmi_ent_height,2)
	messagebox.showinfo('Meters', f'meters = {x}')

bmi_lbl_feet = Label(convert_window, text="enter feet", font=('arial',20,'bold'))
bmi_ent_feet = Entry(convert_window, bd=3, font=('arial',20,'bold'))
bmi_lbl_inch = Label(convert_window, text="enter inch", font=('arial',20,'bold'))
bmi_ent_inch = Entry(convert_window, bd=3, font=('arial',20,'bold'))

bmi_btn_back = Button(convert_window, text="Back", font=('arial',20,'bold'),command = f3)