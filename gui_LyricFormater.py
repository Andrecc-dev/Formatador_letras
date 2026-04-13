import customtkinter as ctk
from Formatador import formatar_musica

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Padronizador Holyrics v2.0")
        self.geometry("1000x650") # Aumentei um pouco para caber a lateral
        
        # Grid Layout (Sidebar + Área de Conteúdo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- SIDEBAR DE CONFIGURAÇÕES ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        
        self.label_conf = ctk.CTkLabel(self.sidebar, text="CONFIGURAÇÕES", font=("Arial", 16, "bold"))
        self.label_conf.pack(pady=20, padx=10)

        # Dropdown de Presets
        self.label_preset = ctk.CTkLabel(self.sidebar, text="Presets:")
        self.label_preset.pack(pady=(10, 0))
        self.opt_preset = ctk.CTkOptionMenu(self.sidebar, 
                                            values=["Live (Padrão)", "Retorno Louvor", "Texto Limpo", "Personalizado"],
                                            command=self.aplicar_preset)
        self.opt_preset.pack(pady=10, padx=10)

        # Input: Limite de Caracteres
        self.label_caracteres = ctk.CTkLabel(self.sidebar, text="Caracteres por linha:")
        self.label_caracteres.pack(pady=(10, 0))
        self.ent_caracteres = ctk.CTkEntry(self.sidebar)
        self.ent_caracteres.insert(0, "40")
        self.ent_caracteres.pack(pady=5, padx=10)

        # Input: Linhas por Slide
        self.label_linhas = ctk.CTkLabel(self.sidebar, text="Linhas por slide:")
        self.label_linhas.pack(pady=(10, 0))
        self.ent_linhas = ctk.CTkEntry(self.sidebar)
        self.ent_linhas.insert(0, "2")
        self.ent_linhas.pack(pady=5, padx=10)

        # Switch: Mostrar Tags ([SLIDE], etc)
        self.switch_tags = ctk.CTkSwitch(self.sidebar, text="Mostrar Etiquetas")
        self.switch_tags.select() # Começa ligado
        self.switch_tags.pack(pady=20, padx=10)

        # --- ÁREA CENTRAL ---
        self.label_titulo = ctk.CTkLabel(self, text="FORMATADOR DE LETRAS", font=("Arial", 22, "bold"))
        self.label_titulo.grid(row=0, column=1, columnspan=2, pady=20)

        # Entrada
        self.label_entrada = ctk.CTkLabel(self, text="Letra Original:")
        self.label_entrada.grid(row=1, column=1, padx=20, sticky="nw")
        self.txt_entrada = ctk.CTkTextbox(self, width=300, height=400)
        self.txt_entrada.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        # Saída
        self.label_saida = ctk.CTkLabel(self, text="Para o Holyrics:")
        self.label_saida.grid(row=1, column=2, padx=20, sticky="nw")
        self.txt_saida = ctk.CTkTextbox(self, width=300, height=400)
        self.txt_saida.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        # Botão Processar
        self.btn_processar = ctk.CTkButton(self, text="FORMATAR AGORA 🚀", font=("Arial", 16, "bold"), height=45, command=self.clique_formatar)
        self.btn_processar.grid(row=3, column=1, columnspan=2, pady=20, padx=20, sticky="ew")

    def aplicar_preset(self, escolha):
        # Bloqueia ou libera os campos se for personalizado
        if escolha == "Live (Padrão)":
            self.ent_caracteres.delete(0, "end")
            self.ent_caracteres.insert(0, "40")
            self.ent_linhas.delete(0, "end")
            self.ent_linhas.insert(0, "2")
            self.switch_tags.select()
        elif escolha == "Retorno Louvor":
            self.ent_caracteres.delete(0, "end")
            self.ent_caracteres.insert(0, "60")
            self.ent_linhas.delete(0, "end")
            self.ent_linhas.insert(0, "4")
            self.switch_tags.select()
        elif escolha == "Texto Limpo":
            self.ent_caracteres.delete(0, "end")
            self.ent_caracteres.insert(0, "100")
            self.ent_linhas.delete(0, "end")
            self.ent_linhas.insert(0, "10")
            self.switch_tags.deselect()

    def clique_formatar(self):
        texto_bruto = self.txt_entrada.get("1.0", "end")
        
        if texto_bruto.strip():
            try:
                # Pegamos os valores dos inputs (convertendo para int)
                limite = int(self.ent_caracteres.get())
                linhas = int(self.ent_linhas.get())
                tags = self.switch_tags.get() # Retorna 1 ou 0 (True/False)

                resultado = formatar_musica(texto_bruto, limite, linhas, tags)
                
                self.txt_saida.delete("1.0", "end")
                self.txt_saida.insert("1.0", resultado)
            except ValueError:
                self.txt_saida.delete("1.0", "end")
                self.txt_saida.insert("1.0", "ERRO: Use apenas números nos campos de configuração!")

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()