from tkinter import *
from tkinter import ttk
import sys
import os

#parte da janela
janela = Tk()

janela = janela
#--------------------------------------------------------------------

#aba de funções
sys.path.append(os.path.join(os.path.dirname(__file__), 'functions')) 
import save
#--------------------------------------------------------------------

#icone do software
icone = PhotoImage(file="../software (em desenvolvimento)/galery/icone.png")
#--------------------------------------------------------------------

#seleções de divisão
divisao = ['nenhum', '1x', '2x', '3x', '4x', '5x', '6x', '7x', '8x', '9x', '10x', '11x', '12x']
#--------------------------------------------------------------------

#configurações da tela
janela.title("Controle Financeiro")
janela.resizable(False, False)
janela.geometry('980x720')
janela.configure(bg='gray')
janela.iconphoto(False, icone)
#--------------------------------------------------------------------

#janelas para as funções
#parte das informações
frame_1 = Frame(janela, bg='gray')
frame_1.place(relwidth=0.988, relheight=0.40, rely=0.01, relx=0.006)
#parte da lista
frame_2 = Frame(janela, bg='gray')
frame_2.place(relwidth=0.988, relheight=0.65, rely=0.34, relx=0.006)
#-------------------------------------------------------------------

#lista de informações
treeview = ttk.Treeview(frame_2, columns=("Nome", "Valor", "Dividido", "Loja"), show="headings")
treeview.heading("Nome", text="Produto")
treeview.heading("Valor", text="Valor")
treeview.heading("Dividido", text="Parcelas")
treeview.heading("Loja", text="Loja")
treeview.pack(expand=True, fill=BOTH)
#--------------------------------------------------------------------

#botão criar
criar = Button(frame_1, text='SALVAR', font=('arial', 15, 'bold'), border=0)
criar.place(rely=0.64, relx=0.60, relheight=0.16, relwidth=0.10)
#--------------------------------------------------------------------

#nomes das opções
preco_nome = Label(frame_1, text='VALOR:', bg='gray', font=('arial', 17, 'bold'))
preco_nome.place(rely=0.69, relx=0.275)
produto_nome = Label(frame_1, text='PRODUTO:', bg='gray', font=('arial', 17, 'bold'))
produto_nome.place(rely=0.09, relx=0.02)
parcelas_nome = Label(frame_1, text='PARCELAS:', bg='gray', font=('arial', 17, 'bold'))
parcelas_nome.place(relx=0.02, rely=0.25)

#--------------------------------------------------------------------

#informações das variáveis
preco = Entry(frame_1, font=('arial', 15, 'italic'))
preco.place(rely=0.7, relx=0.37, relwidth=0.2)
produto = Entry(frame_1, font=('arial', 15))
produto.place(rely=0.1, relx=0.17)
#caixa de seleção das parcelas
parcelas = ttk.Combobox(frame_1, values=divisao, state='readonly', font=('arial', 15,'bold'))
parcelas.set("selecione as parcelas")
parcelas.place(rely=0.25, relx=0.17, relwidth=0.233)
#--------------------------------------------------------------------

janela.mainloop()