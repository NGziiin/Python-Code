from tkinter import *
from tkinter import ttk

# Criando a janela principal
janela = Tk()

# Definindo o tamanho da janela
janela.geometry('360x640')  # Tamanho inicial
janela.title("Controle Financeiro")
janela.configure(bg='gray')

# Função para redimensionar os widgets
def ajustar_tamanho(event):
    largura = event.width
    altura = event.height
    
    # Ajustar tamanho dos widgets em relação à largura e altura da janela
    botao_salvar.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1, anchor='center')
    entrada.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.1, anchor='center')
    combobox.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.1, anchor='center')

# Bind para ajustar a posição ao redimensionar
janela.bind('<Configure>', ajustar_tamanho)

# Exemplo de um botão
botao_salvar = Button(janela, text="Salvar", font=("Arial", 15))
botao_salvar.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1, anchor='center')

# Exemplo de um campo de entrada
entrada = Entry(janela, font=("Arial", 15))
entrada.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.1, anchor='center')

# Exemplo de uma combobox
combobox = ttk.Combobox(janela, values=["1x", "2x", "3x"], state="readonly", font=("Arial", 15))
combobox.set("Selecione as parcelas")
combobox.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.1, anchor='center')

# Iniciar a janela
janela.mainloop()