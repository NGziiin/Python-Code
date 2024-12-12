from tkinter import END
from tkinter import messagebox
import os
import sys
import editar

#salvando os arquivos.
def salvando(treeview, produto_var, loja_var, parcela_var, preco_var, produto_entry, preco_entry, loja_entry, parcela_combobox):
    
    # Recebendo dados das variáveis
    produto_save = produto_var.get()
    loja_save = loja_var.get()
    parcelas_save = parcela_var.get()
    preco_save = preco_var.get()
     
    # Vendo se está tudo preenchido
    if produto_save and loja_save and parcelas_save != "selecione as parcelas" and preco_save:
        
        # Lendo os produtos já inseridos no Treeview (apenas o nome do produto)
        produtos_existentes = [treeview.item(item, 'values')[0] for item in treeview.get_children() if treeview.item(item, 'values')]

        # Olhando se o produto já está registrado
        if produto_save not in produtos_existentes:
            treeview.insert('', 'end', values=(produto_save, preco_save, parcelas_save, loja_save))
            
            # Limpar os campos após salvar
            produto_entry.delete(0, END)
            preco_entry.delete(0, END)
            loja_entry.delete(0, END)
            parcela_combobox.set("selecione as parcelas")
        else:
            messagebox.showwarning("Erro!", "Esse produto já está registrado")
                   
    elif not produto_save:
        messagebox.showwarning('Error!', 'Insira o nome do Produto!')
    elif not loja_save:
        messagebox.showwarning('Error!', 'Insira o nome da loja!')
    elif parcelas_save == "selecione as parcelas":
        messagebox.showwarning('Error!', 'Insira uma parcela!')
    elif not preco_save:
        messagebox.showwarning('Error!', 'Insira o valor do produto!')

#bloqueio de letras na parte do preço  
def bloqueio(P):
  if P == '' or all(c.isdigit() or c == '.' or c == ',' for c in P):
      return True
  else:
      return False