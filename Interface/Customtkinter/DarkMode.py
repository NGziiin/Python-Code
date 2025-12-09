import customtkinter as ctk

class Interface:
    def __init__(self):
        self.janela = ctk.CTk()
        self.config()
        self.main()
        self.janela.mainloop()

    def config(self):
        self.janela.resizable(width=False, height=False)
        self.janela.title("Dark Mode")
        self.janela.geometry("400x300")

    def aplicar_tema(self):
        if self.button.get():  # se switch está ligado
            self.frame.configure(bg_color="black")
            self.label.configure(text="olá! estamos com \no fundo escuro",
                                 text_color="white",
                                 bg_color="black")
            self.button.configure(text="Ativar Modo Claro", text_color="white", bg_color=self.frame.cget("bg_color"))
        else:  # se switch está desligado
            self.frame.configure(bg_color="white")
            self.label.configure(text="olá! estamos com \no fundo claro",
                                 text_color="black",
                                 bg_color=self.frame.cget("bg_color"))
            self.button.configure(text="Ativar Modo Escuro", text_color="black", bg_color=self.frame.cget("bg_color"))

    def main(self):
        self.frame = ctk.CTkFrame(self.janela, bg_color="white", fg_color="transparent")
        self.frame.pack(expand=True, fill="both")

        self.label = ctk.CTkLabel(self.frame,
                                  text="olá! estamos com \no fundo claro",
                                  text_color="black",
                                  bg_color="white",
                                  font=("Arial", 16, "bold"))
        self.label.pack(expand=True, fill="both")

        self.button = ctk.CTkSwitch(self.frame,
                                    text="Ativar Modo Escuro",
                                    bg_color=self.frame.cget("bg_color"),
                                    command=self.aplicar_tema)
        self.button.pack(pady=10, padx=10)

if __name__ == "__main__":
    Interface()
