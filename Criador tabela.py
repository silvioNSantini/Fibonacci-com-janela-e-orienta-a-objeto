from tkinter import *
from calcFib import fib
tabela=Tk()
tabela.geometry("700x350")

def calcularFib():
   n1=int(a.get())
   #print (fib(n1))
   ff=fib(n1)
   label.config(text=ff)
   

Label(tabela, text="Digite o nume do Fibonacci desejado", font=('Calibri 10')).pack()
a=Entry(tabela, width=35)
a.pack()


label=Label(tabela, text="Resultado : ", font=('Calibri 15'))
label.pack(pady=20)

Button(tabela, text="Calculat Fibonacci", command=calcularFib).pack()
tabela.mainloop()
