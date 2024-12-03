import tkinter as tk
from tkinter import ttk

# Criação da janela principal
root = tk.Tk()
root.title("Seleção de Produto")
root.geometry("400x200")

# Lista de produtos
produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4"]

# Função para exibir o produto selecionado
def exibir_selecionado(event):
    selecionado = combobox.get()
    print(f"Produto selecionado: {selecionado}")

# Criação do Combobox
combobox = ttk.Combobox(root, values=produtos)
combobox.set("Selecione um produto")
combobox.pack(pady=20)

# Adicionar evento de seleção
combobox.bind("<<ComboboxSelected>>", exibir_selecionado)

root.mainloop()
