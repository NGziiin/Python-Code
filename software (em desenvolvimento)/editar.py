from tkinter import END
from tkinter import messagebox
import os
import sys

def edit(treeview, produto_var, loja_var, parcela_var, preco_var, produto_entry, preco_entry, loja_entry, parcela_combobox):

    #abrindo a lista de seleção
    lista = treeview.selection()

    #erro caso não tenha selecionado
    if not lista:
        messagebox.showwarning('Error!', 'Selecione algo para editar')
        return
    
    produto_save = treeview.item(lista, 'values')[0]
    loja_save = treeview.item(lista, 'values')[1]
    parcela_save = treeview.item(lista, 'values')[2]
    preco_save = treeview.item(lista, 'values')[3]

    produto_var.set(produto_save)
    loja_var.set(loja_save)
    parcela_var.set(parcela_save)
    preco_var.set(preco_save)