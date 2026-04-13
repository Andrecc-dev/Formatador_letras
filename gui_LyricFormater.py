import customtkinter as ctk
from formatador import formatar_musica
from database import salvar_musica # Importando a nova função

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Padronizador Holyrics v3.0 - Database Edition")
        self.geometry("1100x700")
        
        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # --- SIDEBAR DE CONFIGURAÇÕES ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=5, sticky="nsew")
        
        self.label_conf = ctk.CTkLabel(self.sidebar, text="CONFIGURAÇÕES", font=("Arial", 16, "bold"))
        self.label_conf.pack(pady=20, padx=10)

        # Dropdown de Presets
        self.label_preset = ctk.CTkLabel(self.sidebar, text="Presets:")
        self.label_preset.pack(pady=(10, 0))
        self.opt_preset = ctk.CTkOptionMenu(self.sidebar, 
                                            values=["Live (Padrão)", "Retorno Louvor", "Texto Limpo", "Personalizado"],
                                            command=self.aplicar_preset)
        self.opt_preset.pack(pady=10, padx=10)

        # Inputs de Configuração
        self.label_caracteres = ctk.CTkLabel(self.sidebar, text="Caracteres por linha:")
        self.label_caracteres.pack(pady=(10, 0))
        self.ent_caracteres = ctk.CTkEntry(self.sidebar)
        self.ent_caracteres.insert(0, "40")
        self.ent_caracteres.pack(pady=5, padx=10)

        self.label_linhas = ctk.CTkLabel(self.sidebar, text="Linhas por slide:")
        self.label_linhas.pack(pady=(10, 0))
        self.ent_linhas = ctk.CTkEntry(self.sidebar)
        self.ent_linhas.insert(0, "2")
        self.ent_linhas.pack(pady=5, padx=10)

        self.switch_tags = ctk.CTkSwitch(self.sidebar, text="Mostrar Etiquetas")
        self.switch_tags.select()
        self.switch_tags.pack(pady=20, padx=10)

        # --- BOTÃO SALVAR (SIDEBAR) ---
        self.btn_salvar = ctk.CTkButton(self.sidebar, text="SALVAR NO BANCO 💾", 
                                        fg_color="green", hover_color="darkgreen",
                                        command=self.clique_salvar)
        self.btn_salvar.pack(pady=20, padx=10)

        # --- ÁREA CENTRAL ---
        self.label_titulo_app = ctk.CTkLabel(self, text="FORMATADOR & REPERTÓRIO", font=("Arial", 22, "bold"))
        self.label_titulo_app.grid(row=0, column=1, columnspan=2, pady=20)

        # Campos de Identificação (Título e Artista)
        self.frame_info = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_info.grid(row=1, column=1, columnspan=2, padx=20, sticky="ew")
        
        self.ent_n_musica = ctk.CTkEntry(self.frame_info, placeholder_text="Título da Música", width=300)
        self.ent_n_musica.pack(side="left", padx=(0, 10))
        
        self.ent_n_artista = ctk.CTkEntry(self.frame_info, placeholder_text="Artista/Ministério", width=250)
        self.ent_n_artista.pack(side="left")

        # Entrada e Saída
        self.txt_entrada = ctk.CTkTextbox(self, width=350, height=350)
        self.txt_entrada.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        self.txt_saida = ctk.CTkTextbox(self, width=350, height=350)
        self.txt_saida.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        # Botão Processar
        self.btn_processar = ctk.CTkButton(self, text="FORMATAR AGORA 🚀", font=("Arial", 16, "bold"), height=45, command=self.clique_formatar)
        self.btn_processar.grid(row=3, column=1, columnspan=2, pady=20, padx=20, sticky="ew")

    def aplicar_preset(self, escolha):
        if escolha == "Live (Padrão)":
            self.ent_caracteres.delete(0, "end")
            self.ent_caracteres.insert(0, "40")
            self.ent_linhas.delete(0, "end")
            self.ent_linhas.insert(0, "2")
            self.switch_tags.select()
        # ... (os outros elifs continuam iguais ao seu código anterior)

    def clique_formatar(self):
        texto_bruto = self.txt_entrada.get("1.0", "end")
        if texto_bruto.strip():
            try:
                limite = int(self.ent_caracteres.get())
                linhas = int(self.ent_linhas.get())
                tags = self.switch_tags.get()
                resultado = formatar_musica(texto_bruto, limite, linhas, tags)
                self.txt_saida.delete("1.0", "end")
                self.txt_saida.insert("1.0", resultado)
            except ValueError:
                self.txt_saida.delete("1.0", "end")
                self.txt_saida.insert("1.0", "ERRO: Use números válidos!")

    def clique_salvar(self):
        # 1. Pega os dados da tela
        titulo = self.ent_n_musica.get()
        artista = self.ent_n_artista.get()
        original = self.txt_entrada.get("1.0", "end")
        formatada = self.txt_saida.get("1.0", "end")

        # 2. Validação simples
        if not titulo.strip() or not original.strip():
            self.txt_saida.delete("1.0", "end")
            self.txt_saida.insert("1.0", "ERRO: Título e Letra Original são obrigatórios para salvar!")
            return

        # 3. Chama o database.py
        sucesso = salvar_musica(titulo, artista, original, formatada)

        if sucesso:
            self.txt_saida.delete("1.0", "end")
            self.txt_saida.insert("1.0", f"Música '{titulo}' salva com sucesso no banco de dados! ✅")
        else:
            self.txt_saida.delete("1.0", "end")
            self.txt_saida.insert("1.0", "Erro ao conectar ao MySQL para salvar. ❌")

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()