from tkinter import *
from tkinter import ttk
from tkinter import Tk
import webbrowser

janela = Tk()

janela = janela

#configurações da janela
janela.title("Calculadora IMC")
janela.resizable(False, False)
janela.configure(background='#1E90FF')
janela.geometry('322x500')
janela.iconbitmap('C:\\Users\\71325245186\\Documents\\estudo\\R.ico')

#widgets da tela
frame1 = Frame(janela, bg='#1E90FF')
frame1.place(relx= 0.02, rely=0.01, relheight=0.4, relwidth=0.96)
frame2 = Frame(janela, bg='#1E90FF')
frame2.place(relx= 0.02, rely=0.42, relheight=0.58, relwidth=0.96)

#direcionando GitHub
def github():
    webbrowser.open_new("https://github.com/NGziiin")
    
#abrindo calculadora
def calculadora():
    janela.destroy()
    import calculadora_com_interface

#strings
texto_tela = StringVar()
texto_aviso = StringVar()
texto_imc = StringVar()
erro1 = StringVar()
erro2 = StringVar()

#calculando
def calculando():
    #pegando dados
    global peso
    global altura
    peso = dadospeso.get()
    altura = dadosaltura.get()
    
    #erro de caixa vazia
    if not altura:
      texto_imc.set("digite sua altura")
    elif not peso:
      texto_imc.set("digite seu peso")
      
    #trocando , por .
    peso = peso.replace("," , ".")
    altura = altura.replace("," , ".")
    #convertendo String em Float
    altura = float(altura)
    
    #fazendo comparação da altura
    if altura <= 2.30 and altura >= 1.30:
      
      #convertendo peso em float
      peso = float(peso)
      
      #fazendo comparação nos dados peso
      if peso <= 596 and peso >= 30:
        
        #realizando calculo após tudo está correto
        resu = float(peso/(altura * altura))
        resu = round(resu ,1)
        if resu <= 18.5:
          texto_aviso.set('ABAIXO DO PESO')
        elif resu <= 24.9 and resu >= 18.6:
          texto_aviso.set('Parabéns!! Peso ideal')
        elif resu <= 29.9 and resu >= 25:
          texto_aviso.set('ACIMA DO PESO')
        elif resu <= 34.9 and resu >= 30:
          texto_aviso.set('Obesidade grau 1')
        elif resu <= 39.9 and resu>= 30.1:
          texto_aviso.set('Obesidade grau 2')
        elif resu >= 40:
          texto_aviso.set('Obesidade grau 3')
        #convertendo o resultado em string
        resu = str(resu)
        #trocando o . pela ,
        resu = resu.replace(".", ",")
        #aparecendo os resultados na tela
        texto_imc.set('SEU IMC:')
        texto_tela.set(resu)
        erro1.set("")
        erro2.set("")
        #fim#
      else:
        texto_tela.set("digite novamente")
        texto_imc.set("Não reconhecido!")
        erro2.set("")
      #fim#
    else:
      texto_tela.set('digite novamente')
      texto_imc.set('Não reconhecido!')
      erro1.set("")
      erro2.set("")
    #fim#
        
#label de resposta
res = Label(frame2, textvariable=texto_tela, bg='#1E90FF', foreground='white', font=('arial', 18, 'bold'))
res.place(relx=0.02, rely=0.38, relheight=0.2, relwidth=0.96)
aviso = Label(frame2, textvariable=texto_aviso, bg='#1E90FF', foreground='white', font=('arial', 18, 'bold'))
aviso.place(relx=0.02, rely=0.6, relheight=0.10, relwidth=0.96)
imc = Label(frame2, textvariable=texto_imc, bg='#1E90FF', foreground='white', font=('arial', 18, 'bold'))
imc.place(relx=0.02, rely=0.33, relheight=0.1, relwidth=0.96)

#texto na tela
nome1 = Label(frame1, text="CALCULADORA IMC", bg="#1E90FF", font=('arial', 20, 'bold'), foreground='white')
nome1.place(relx=0.02, rely=0.01, relheight=0.3, relwidth=0.96)
nome2 = Label(frame1, text='(Indice de Massa Corporal)', bg="#1E90FF", font=('arial', 15, 'bold'), foreground='white')
nome2.place(relx=0.02, rely=0.22, relheight=0.1, relwidth=0.96)
nome3 = Label(frame1, text="PESO", bg='#1E90FF', foreground='white', font=('arial', 15, 'bold'))
nome3.place(relx=0.36, rely=0.73, relheight=0.10, relwidth=0.3)
nome4 = Label(frame1, text="ALTURA", bg='#1E90FF', foreground='white', font=('arial', 15, 'bold'))
nome4.place(relx=0.36, rely=0.43, relheight=0.10, relwidth=0.3)

#botões da calculadora
btreturn = Button(frame2, command=calculadora, text="Voltar para Calculadora", bd=1, bg='white', font=('arial', 10, 'bold'), relief=RAISED)
btreturn.place(relx=0.02, rely=0.80, relwidth=0.96, relheight=0.10)
btrespo = Button(frame2,command=calculando, text="RESULTADO", bg='green', bd=1, font=('arial', 20, 'bold'), fg='white', activebackground='#00FF7F', activeforeground='white', relief=RAISED)
btrespo.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.2)
nome3 = Button(frame2, command=github, text="https://github.com/NGziiin", bg='#1E90FF', activebackground='#1E90FF', bd=0, font=('arial', 10, 'italic'), fg='white')
nome3.place(relx=0.25, rely=0.90, relwidth=0.5, relheight=0.1)

#caixa de digito
dadosaltura = Entry(frame1, textvariable=erro1, font=('arial', 10), justify='center')
dadosaltura.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.1)
dadospeso = Entry(frame1, textvariable=erro2, font=('arial', 10), justify='center')
dadospeso.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)

janela.mainloop()