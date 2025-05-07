from tkinter import *
from unittest import result

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

main = Tk()
main.title("Pocket Calculator")



operator = ""
input_value = StringVar()
display_text = Entry(main, font =("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4, 
                bg="navajo white",justify=RIGHT)
display_text.grid(columnspan = 4)

#Row 1 789+

btn_7 = Button(main, padx = 16 , bd = 8 , fg="black" , font = ("arial" , 20 , "bold"),text = "7",bg="sky blue",command=lambda: buttonClick(7))
btn_7.grid (row=1 , column=0)

btn_8 = Button(main, padx = 16 , bd = 8 , fg="black" , font = ("arial" , 20 , "bold"),text = "8",bg="sky blue",command=lambda: buttonClick(8))
btn_8.grid (row=1 , column=1)

btn_9 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "9",bg="sky blue",command=lambda: buttonClick(9))
btn_9.grid (row=1 , column=2)

btn_add = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "+",bg="lemon chiffon",command=lambda: buttonClick("+"))
btn_add.grid (row=1,column=3)

# ROW 2 456-

btn_4 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "4",bg="sky blue",command=lambda: buttonClick(4))
btn_4.grid (row=2, column=0)

btn_5 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "5",bg="sky blue",command=lambda: buttonClick(5))
btn_5.grid (row=2, column=1)

btn_6 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "6",bg="sky blue",command=lambda: buttonClick(6))
btn_6.grid (row=2, column=2)

btn_sub = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "-",bg="lemon chiffon",command=lambda: buttonClick("-"))
btn_sub.grid (row=2 , column=3)

# Row 3 123*

btn_1 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "1",bg="sky blue",command=lambda: buttonClick(1))
btn_1.grid (row=3, column=0)

btn_2 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "2",bg="sky blue",command=lambda: buttonClick(2))
btn_2.grid (row=3 , column=1)

btn_3 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "3",bg="sky blue",command=lambda: buttonClick(3))
btn_3.grid (row=3, column=2)

btn_mul = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "*",bg="lemon chiffon",command=lambda: buttonClick("*"))
btn_mul.grid (row=3, column=3)

#Row 4 0C=/

btn_0 = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "0",bg="sky blue",command=lambda: buttonClick(0))
btn_0.grid (row=4, column=0)

btn_clear = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "C",bg="coral",command=buttonClear)
btn_clear.grid (row=4, column=1)

btn_equal = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "=",bg="light coral",command=buttonEqual)
btn_equal.grid (row=4, column=2)

btn_div = Button(main, padx = 16 , bd = 8 , fg = "black" , font = ("arial" , 20 , "bold"),text = "/",bg="lemon chiffon",command=lambda: buttonClick("/"))
btn_div.grid (row=4, column=3)


main.mainloop()