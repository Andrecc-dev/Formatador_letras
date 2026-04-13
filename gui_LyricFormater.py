import customtkinter as ctk
from Formatador import formatar_musica

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Padronizador Holyrics v1.0")
        self.geometry("800x600")
        
        # Grid Layout (Organizando em colunas)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- TÍTULO ---
        self.label_titulo = ctk.CTkLabel(self, text="FORMATADOR DE LETRAS PARA LIVE", font=("Arial", 20, "bold"))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # --- ÁREA DE ENTRADA (Esquerda) ---
        self.label_entrada = ctk.CTkLabel(self, text="Cole a letra original aqui:")
        self.label_entrada.grid(row=1, column=0, padx=20, sticky="nw")
        
        self.txt_entrada = ctk.CTkTextbox(self, width=350, height=350)
        self.txt_entrada.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # --- ÁREA DE SAÍDA (Direita) ---
        self.label_saida = ctk.CTkLabel(self, text="Resultado para o Holyrics:")
        self.label_saida.grid(row=1, column=1, padx=20, sticky="nw")
        
        self.txt_saida = ctk.CTkTextbox(self, width=350, height=350)
        self.txt_saida.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        # --- BOTÃO DE AÇÃO ---
        self.btn_processar = ctk.CTkButton(self, text="FORMATAR AGORA 🚀", command=self.clique_formatar)
        self.btn_processar.grid(row=3, column=0, columnspan=2, pady=20)

    def clique_formatar(self):
        # 1. Pega o texto da caixa de entrada
        texto_bruto = self.txt_entrada.get("1.0", "end")
        
        if texto_bruto.strip():
            # 2. Chama a sua função do formatador.py
            resultado = formatar_musica(texto_bruto)
            
            # 3. Limpa a saída e coloca o resultado novo
            self.txt_saida.delete("1.0", "end")
            self.txt_saida.insert("1.0", resultado)

# Se rodar o gui.py direto, ele abre a janela para testar
if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()