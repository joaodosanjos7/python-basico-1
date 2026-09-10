# Interface Avançada — versão orientada a objetos
# Formulário com Entry, RadioButtons, Checkboxes e ComboBox,
# que monta uma mensagem personalizada a partir das escolhas do usuário.

import tkinter as tk
from tkinter import ttk

class InterfaceAvancada:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Interface Avançada")
        self.janela.geometry("400x400")
        self.criar_widgets()

    def criar_widgets(self):
        # Caixa de entrada para nome
        tk.label(self.janela, text="Digite seu nome:").pack(pady=5)
        # Input da caixa
        self.caixa_texto = tk.Entry(self.janela, width=40)
        self.caixa_texto.pack(pady=5)

        # Botões de radio (Escolha)
        tk.label(self.janela, text="Escolha sua preferencia: ").pack(pady=5)
        # Opção padrão  ""Café""
        self.preferencia = tk.StringVar(value="Café")
        # Laço for para as outras opções
        for opcao in ["Café", "Chá", "Suco", "Água"]:
            tk.Radiobutton(
                self.janela, text=opcao, variable=self.var_radio, 
                value=opcao
            ).pack()


