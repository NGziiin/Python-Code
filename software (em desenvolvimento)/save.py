from tkinter import END
import os
import sys

def salvando(treeview, produto_var, loja_var, parcela_var, preco_var, produto_entry, preco_entry, loja_entry, parcela_combobox):
    produto_save = produto_var.get()
    loja_save = loja_var.get()
    parcelas_save = parcela_var.get()
    preco_save = preco_var.get()

    if produto_save and loja_save and parcelas_save != "selecione as parcelas" and preco_save:
        treeview.insert('', 'end', values=(produto_save, preco_save, parcelas_save, loja_save))
        
        # Limpar os campos após salvar
        produto_entry.delete(0, END)
        preco_entry.delete(0, END)
        loja_entry.delete(0, END)
        parcela_combobox.set("selecione as parcelas")
        
def bloqueio(P):
  if P == '' or P.isdigit():
      return False
  else:
      return True