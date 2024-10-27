from Janela.Janela import *
from extras.Barra import *

#-----------Instaciando a classe-----------
novaJanela = Janela("Teste", 300, 350, "gray")


#----------------Entrada-------------------

txt = novaJanela.addEntrada("Teste 1")

def imprimir():
    if txt.get():
        novaJanela.msgAviso(txt.get())
    else:
        barrinha = Barra(novaJanela.root)
        novaJanela.msgAviso("Digite algo no campo")
        
botaoAlerta = Buttones()
botaoAlerta.addBotao("validar", imprimir)
novaJanela.addTexto("-" *55)

#----------------check-------------------
checing1 = novaJanela.addCheck("Op 1")
checing2 = novaJanela.addCheck("Op 2")
checing3 = novaJanela.addCheck("Op 3")

def verificarOP():
    novaJanela.msgAviso(f"checing 1: {checing1.get()} \nchecing 2: {checing2.get()} \nchecing 3: {checing3.get()}")

botaoCheck = Buttones()
botaoCheck.addBotao("Verificar Op", verificarOP)

novaJanela.addTexto("-" *55)

#--------------Selecao(Radio)--------------
select1 = novaJanela.addSelecao("opcao 1", 1)
select2 = novaJanela.addSelecao("opcao 2", 2)
select3 = novaJanela.addSelecao("opcao 3", 3)

def verificarSelecao():
    valor_selecionado = novaJanela.var.get()
    if valor_selecionado == "1":
        novaJanela.msgAviso("Selecionado: opção 1")
    elif valor_selecionado == "2":
        novaJanela.msgAviso("Selecionado: opção 2")
    elif valor_selecionado == "3":
        novaJanela.msgAviso("Selecionado: opção 3")

botaoSelect = Buttones()

botaoSelect.addBotao("verificar Selecao", verificarSelecao)

novaJanela.root.mainloop()


