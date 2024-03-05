from tkinter import *

class Janela:
    def __init__(self, titulo, largura, altura):
        self.root = Tk()
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - (altura + 70) / 2
        self.root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        self.root.title(titulo)
        self.button_func = None
        
    def destruir(self):
        return self.root.destroy()
    
    def addTexto(self, info, x=None, y=None):
        self.label = Label(text=info)
        if x is not None and y is not None:
           self.label.place(x=x, y=y)
        else:
            self.label.pack()
    
    def corFundo(self, corDeFundo=None):
        self.root.config(bg=corDeFundo)
        self.label.config(bg=corDeFundo)

    def addEntrada(self, tt=None, x=None, y=None):
        if tt:
            self.texto(tt)
        self.valorEntrada = Entry()
        if x is not None and y is not None:
            self.valorEntrada.place(x=x, y=y)
        else:
            self.valorEntrada.pack()   
        return self.valorEntrada 
    
    def addBotao(self, info, func=None):
            self.button_func = func
            self.bb = Button(text=info, command=self.clickBotao)
            self.bb.pack()
            return self.bb
    
    def clickBotao(self):
        if self.button_func:
            self.button_func()
   
            