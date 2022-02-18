from cgitb import text
from curses import window
from tkinter import *


def convert_F_to_C(input_f_tmp, lbl_c_temp):
    temp_f = round(5/9 * float(input_f_tmp.get()) - 32, 2)
    lbl_c_temp["text"] = f"{temp_f} \N{DEGREE CELSIUS}"


def convert_C_to_F(input_c_temp, lbl_f_temp):
    temp_c = round(9/5 * float(lbl_f_temp.get()) + 32, 2)
    lbl_f_temp["text"] = f"{temp_c} \N{DEGREE FAHRENHEIT}"


if __name__ == "__main__":
    window = Tk()
    window.title("Convert Temperature")
    window.resizable(width=False, height=False)

    form_convert = Frame(master=window)  # define form
    # Convert F to C form
    input_f_tmp = Entry(master=form_convert, width=30)  # input F temperature
    lbl_c_temp = Label(master=form_convert, text="\N{DEGREE CELSIUS}")

    input_f_tmp.grid(row=0, column=0, sticky="e")
    lbl_c_temp.grid(row=0, column=1, sticky='w')
    