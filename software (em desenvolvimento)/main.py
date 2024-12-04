from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import Tk
import sys
import os

#parte da janela
janela = Tk()

janela = janela
#--------------------------------------------------------------------

#importando as funções 
import save
#--------------------------------------------------------------------

#icone do software
# -> icone = PhotoImage(file="../Nova pasta/Python-Code/software (em desenvolvimento)/galery/icone.png")
#--------------------------------------------------------------------

#variavel global
produtodados = StringVar()
lojadados = StringVar()
parceladados = StringVar()
precodados = StringVar()

#configurações da tela
janela.title("Controle Financeiro")
janela.resizable(False, False)
janela.geometry('980x720')
janela.configure(bg='gray')
# -> janela.iconphoto(False, icone)
#--------------------------------------------------------------------

#janelas para as funções
#parte das informações
frame_1 = Frame(janela, bg='gray')
frame_1.place(relwidth=0.988, relheight=0.40, rely=0.01, relx=0.006)
#parte da lista
frame_2 = Frame(janela, bg='gray')
frame_2.place(relwidth=0.988, relheight=0.65, rely=0.34, relx=0.006)
#-------------------------------------------------------------------

#nomes das opções
preco_nome = Label(frame_1, text='VALOR:', bg='gray', font=('arial', 17, 'bold'))
preco_nome.place(rely=0.54, relx=0.067)
produto_nome = Label(frame_1, text='PRODUTO:', bg='gray', font=('arial', 17, 'bold'))
produto_nome.place(rely=0.09, relx=0.03)
parcelas_nome = Label(frame_1, text='PARCELAS:', bg='gray', font=('arial', 17, 'bold'))
parcelas_nome.place(rely=0.246, relx=0.02)
empresa_nome = Label(frame_1, text='LOJA:', bg='gray', font=('arial', 17, 'bold'))
empresa_nome.place(rely=0.39, relx=0.087)
#--------------------------------------------------------------------

#lista de informações
#seleções de divisão
divisao = ['nenhum', '1x', '2x', '3x', '4x', '5x', '6x', '7x', '8x', '9x', '10x', '11x', '12x']
#--------------------------------------------------------------------
treeview = ttk.Treeview(frame_2, columns=("Nome", "Valor", "Dividido", "Loja"), show="headings")
treeview.heading("Nome", text="Produto")
treeview.heading("Valor", text="Valor")
treeview.heading("Dividido", text="Parcelas")
treeview.heading("Loja", text="Loja")
treeview.pack(expand=True, fill=BOTH)

treeview.column("Nome", width=200, anchor=CENTER)
treeview.column("Valor", width=50, anchor=CENTER)
treeview.column("Dividido", width=50, anchor=CENTER)
treeview.column("Loja", width=200, anchor=CENTER)
#--------------------------------------------------------------------

#informações das variáveis
preco = Entry(frame_1, font=('arial', 15), textvariable=precodados)
preco.place(rely=0.55, relx=0.17)
produto = Entry(frame_1, font=('arial', 15), textvariable=produtodados)
produto.place(rely=0.1, relx=0.17)
#caixa de seleção das parcelas
parcelas = ttk.Combobox(frame_1, values=divisao, state='readonly', font=('arial', 15,'bold'), textvariable=parceladados)
parcelas.set("selecione as parcelas")
parcelas.place(rely=0.25, relx=0.17, relwidth=0.233)
loja = Entry(frame_1, font=('arial', 15), textvariable=lojadados)
loja.place(rely=0.4, relx=0.17)
#--------------------------------------------------------------------

#botões
#botão salvar
criar = Button(frame_1, text='SALVAR', font=('arial', 15, 'bold'), border=0, command=partial(save.salvando, treeview, produtodados, lojadados, parceladados, precodados, produto, preco, loja, parcelas))
criar.place(rely=0.48, relx=0.45, relheight=0.16, relwidth=0.10)
#botão editar
editar = Button(frame_1, text='EDITAR', font=('arial', 15, 'bold'), border=0)
editar.place(rely=0.295, relx=0.45, relheight=0.16, relwidth=0.10)
#botão excluir
excluir = Button(frame_1, text='EXCLUIR', font=('arial', 15, 'bold'), border=0)
excluir.place(rely=0.11, relx=0.45, relheight=0.16, relwidth=0.10)
#--------------------------------------------------------------------

janela.mainloop()