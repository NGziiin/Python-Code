#### NÃO TENHO ACESSO A API ENTÃO PRECISO CRIAR UM SISTEMA DRAG & DROP DE CSV PARA FAZER ESSE SISTEMA
import customtkinter as ctk
import pandas as pd

class Interface:
    def __init__(self):
        self.janela = ctk.CTk()
        self.config_interface()
        self.janela.mainloop()

    def config_interface(self):
        self.janela.resizable(False, False)
        self.janela.geometry("430x390")
        self.janela.title('Contador de chromebook')

class Geral:
    def __init__(self):
        self.link_planilha = f"C:/Users/heric/Downloads/controle de chromebook para garantia(CHROMEBOOK - SEDUC).csv"
        self.load_planilha()
        pass

    def load_planilha(self):
        self.planilha = pd.read_csv(self.link_planilha, encoding='latin1')
        print(self.planilha.head())

if __name__ == "__main__":
    Interface()