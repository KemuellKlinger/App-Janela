from tkinter import *
from tkinter import ttk

def valBarra():
    cont = 0
    etapas = 10000/100
    while cont < etapas:
        cont += 1
        i=0
        while i<100000:
            i=i+1
        varBarra.set(cont)
        janela.update()
    concluido = Label(janela, text="Concluido").grid()

janela = Tk()
janela.geometry("300x300")

botao = Button(janela, text="Comecar", command=lambda:valBarra())
botao.grid(row=0, column=0)

varBarra = DoubleVar()
varBarra.set(0)

progresso = ttk.Progressbar(janela, variable=varBarra, maximum=100)
progresso.grid(row=2, column=0, ipadx=50, ipady=5)

janela.mainloop()