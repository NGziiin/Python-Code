from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#editando as opções do treeview
def edit(treeview, combobox):

    #recebendo valores registrados
    registrados = [treeview.item(item, 'values')[0] for item in treeview.get_children()]

    #passando os valores para caixa de seleção
    combobox['values'] = registrados

    #colocando as informações na tela
    if registrados:
        combobox.set(registrados[0])

#verificando se o treeview não está vazio
def vazio(treeview):

    #verificando se tem informações no treeview
    if len(treeview.get_children()) == 0:

        #mensagem de erro caso esteja vazio e retornando a infomação que está vazio
        messagebox.showwarning("ERRO!", 'Não possui informações inseridas')
        return False
    else:
        return True

#janela de seleção
def janela_editar(treeview, produtodados, lojadados, parceladados, precodados, produto, preco, loja, parcelas):

    #verificando se a treeview possui infomações (se não houver cancela a abertura da janela)
    if vazio(treeview):
        #configurações da janela
        janela2 = Toplevel()
        janela2.configure(bg='#ffffc1')
        janela2.resizable(False, False)
        janela2.geometry('360x640')
        janela2.title('editar informações')

        #frame para colocar as informações
        frame = Frame(janela2, bg='white')
        frame.place(relheight=1, relwidth=1)

        #configurações do combobox
        select = ttk.Combobox(janela2, state='readonly')
        select.place(relx=0.5, rely=0.5)

        #passando as informações para a caixa de seleção (não pode remover daqui)
        edit(treeview, select)

        janela2.mainloop()