from tkinter import *
from tkinter import ttk
from tkinter import Tk

janela = Tk()

#abrindo janela
janela = janela

#configurações da tela
    
janela.title("Calculadora")
janela.configure(background = '#E8E8E8')
janela.geometry('322x467')
janela.resizable(False, False)
janela.iconbitmap('C:\\Users\\71325245186\\Documents\\estudo\\R.ico')

#configurações das informações    
frame_1 = Frame(janela, bg='#E8E8E8')
frame_1.place(relx=0, rely=0, relwidth=1, relheight=0.29)
frame_2 = Frame(janela, bg='#E8E8E8')
frame_2.place(relx=0, rely=0.3, relwidth=1, relheight=0.70)

#abrindo imc
def imc():
    janela.destroy()
    import IMC_com_interface

#variável global
texto_tela = StringVar()

#variável
todos_valores = ''

def valores(event):
    
    #aparece as respostas
    global todos_valores
    todos_valores = todos_valores + str(event)
    todos_valores = todos_valores.replace('*','×')
    todos_valores = todos_valores.replace('/','÷')
    todos_valores = todos_valores.replace('.',',')
    
    #passado para a tela
    texto_tela.set(todos_valores)
    
#calculando conta
def calculo():
    try:
        global todos_valores
        global resultado
        todos_valores = todos_valores.replace('×', '*')
        todos_valores = todos_valores.replace('÷', '/')
        todos_valores = todos_valores.replace(',', '.')
        if '**' in todos_valores:
            texto_tela.set('Equação Inválida.')
        if '*-+' in todos_valores:
            texto_tela.set('Equação Inválida.')
        if '*+-' in todos_valores:
            texto_tela.set('Equação Inválida.')
        else:
            resultado = eval(todos_valores)
            texto_tela.set(resultado)
    except SyntaxError:
        texto_tela.set('Equação Inválida')
    except ZeroDivisionError:
        texto_tela.set('#Erro#')
    
#função clear
def clear():
    global todos_valores
    todos_valores = ""
    texto_tela.set(todos_valores)

res = Label(frame_1, bg='#E8E8E8', bd=0, textvariable=texto_tela, font=('verdana', 20), padx=7, relief=FLAT, anchor="s""e")
res.place(relx=0.02, rely=0.03, relheight=0.96, relwidth=0.96)
        
#botões do teclado
bt_0 = Button(frame_2, command=lambda:valores("0"),  text="0", bd=0, bg='white', font=('verdana',20,), borderwidth=0)
bt_0.place(relx=0.35, rely=0.84, relheight=0.15, relwidth=0.3)
bt_1 = Button(frame_2, command=lambda:valores("1"), text="1", bd=0, bg='white', font=('verdana',20,))
bt_1.place(relx=0.02, rely=0.67, relheight=0.15, relwidth=0.3)
bt_2 = Button(frame_2, command=lambda:valores("2"), text="2", bd=0, bg='white', font=('verdana',20,))
bt_2.place(relx=0.35, rely=0.67, relheight=0.15, relwidth=0.3)
bt_3 = Button(frame_2, command=lambda:valores("3"), text="3", bd=0, bg='white', font=('verdana',20,))
bt_3.place(relx=0.68, rely=0.67, relheight=0.15, relwidth=0.3)
bt_4 = Button(frame_2, command=lambda:valores("4"), text="4", bd=0, bg='white', font=('verdana',20,))
bt_4.place(relx=0.02, rely=0.5, relheight=0.15, relwidth=0.3)
bt_5 = Button(frame_2, command=lambda:valores("5"), text="5", bd=0, bg='white', font=('verdana',20,))
bt_5.place(relx=0.35, rely=0.5, relheight=0.15, relwidth=0.3)
bt_6 = Button(frame_2, command=lambda:valores("6"), text="6", bd=0, bg='white', font=('verdana',20,))
bt_6.place(relx=0.68, rely=0.5, relheight=0.15, relwidth=0.3)
bt_7 = Button(frame_2, command=lambda:valores("7"), text="7", bd=0, bg='white', font=('verdana',20,))
bt_7.place(relx=0.02, rely=0.33, relheight=0.15, relwidth=0.3)
bt_8 = Button(frame_2, command=lambda:valores("8"), text="8", bd=0, bg='white', font=('verdana',20,))
bt_8.place(relx=0.35, rely=0.33, relheight=0.15, relwidth=0.3)
bt_9 = Button(frame_2, command=lambda:valores("9"), text="9", bd=0, bg='white', font=('verdana',20,))
bt_9.place(relx=0.68, rely=0.33, relheight=0.15, relwidth=0.3)

#botões clean e virgula
btclean = Button(frame_2,command=clear, text="C", bd=0, bg='white', font=('verdana',20,))
btclean.place(relx=0.02, rely=0.84, relheight=0.15, relwidth=0.3)
btvirgula = Button(frame_2,command=lambda:valores("."), text=",", bd=0, bg='white', font=('verdana',20,))
btvirgula.place(relx=0.68, rely=0.84, relheight=0.15, relwidth=0.3)

#botões de calculo
btsoma = Button(frame_2,command=lambda:valores("+"), text="+", bd=0, bg='white', font=('verdana',20,))
btsoma.place(relx=0.02, rely=0.19, relheight=0.12, relwidth=0.23)
btsub = Button(frame_2,command=lambda:valores("-"), text="-", bd=0, bg='white', font=('verdana',20,))
btsub.place(relx=0.27, rely=0.19, relheight=0.12, relwidth=0.23)
btmult = Button(frame_2,command=lambda:valores("*"), text="×", bd=0, bg='white', font=('verdana',20,))
btmult.place(relx=0.52, rely=0.19, relheight=0.12, relwidth=0.22)
btdiv = Button(frame_2,command=lambda:valores("/"), text="÷", bd=0, bg='white', font=('verdana',20,))
btdiv.place(relx=0.76, rely=0.19, relheight=0.12, relwidth=0.22)
btresul = Button (frame_2,command=calculo, text="=", bd=0, bg='white', font=('verdana', 20))
btresul.place(relx=0.76, rely=0.02, relheight=0.15, relwidth=0.22)

#botão calculadora IMC
btimc = Button(frame_2,command=imc, text="Calculadora IMC", bd=0, bg='white', font=('verdana',15,))
btimc.place(relx=0.02, rely=0.02, relheight=0.15, relwidth=0.72)
       
janela.mainloop()