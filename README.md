1. 📌 Nome do Projeto
LyricFormatter — Padronizador de Letras para Projeção

2. 🎯 Objetivo Geral
Desenvolver um sistema em Python capaz de padronizar automaticamente letras de músicas para exibição no Holyrics, garantindo consistência visual, redução de erros humanos e otimização do tempo de preparação.

3. 🎯 Objetivos Específicos
Automatizar a formatação de letras
Reduzir o tempo gasto com ajustes manuais
Garantir padronização entre diferentes usuários
Melhorar a legibilidade no telão

4. 🧩 Problema
A inserção manual de letras apresenta os seguintes problemas:
Falta de padronização entre usuários
Slides visualmente inconsistentes
Retrabalho frequente
Risco de erros durante apresentações

5. 💡 Solução Proposta
Desenvolver um sistema que:
Receba texto bruto de músicas
Aplique regras fixas de formatação
Retorne texto estruturado pronto para uso

6. ⚙️ Requisitos Funcionais
O sistema deve:
Permitir entrada de texto livre
Processar automaticamente o texto
Aplicar limite de caracteres por linha
Dividir o conteúdo em slides
Exibir o resultado formatado
Permitir cópia do resultado final
Permitir limpeza rápida dos campos

7. ⚙️ Requisitos Não Funcionais
Interface simples e intuitiva
Baixo tempo de resposta
Facilidade de uso por usuários não técnicos
Código organizado e modular
Facilidade de manutenção e expansão

8. 📏 Regras de Negócio
8.1 Estrutura de Exibição
Máximo de 2 linhas por slide

8.2 Limite de Linha
Máximo de 40 caracteres por linha (incluindo espaços)

8.3 Quebra de Linha
Não dividir palavras
Quebra deve ocorrer preferencialmente em espaços

8.4 Tratamento de Texto
O sistema deve:
Remover espaços duplicados
Ignorar quebras de linha do texto original
Padronizar o conteúdo antes da formatação

8.5 Separação de Slides
Slides devem ser separados por linha em branco

8.6 Regra para Palavras Longas
Palavras com mais de 40 caracteres:
Devem ser mantidas completas em uma única linha
Mesmo que ultrapassem o limite definido

9. 🔄 Fluxo do Sistema
Usuário insere o texto
Sistema realiza limpeza do conteúdo
Texto é dividido em palavras
Palavras são organizadas em linhas respeitando limites
Linhas são agrupadas em slides (2 linhas)
Resultado final é exibido

10. 🧠 Regras de Processamento
A verificação do limite de caracteres ocorre antes da adição da palavra
A ordem original das palavras deve ser preservada
Nenhuma palavra deve ser truncada
O sistema deve garantir consistência na saída

11. ⚠️ Tratamento de Exceções
O sistema deve tratar:
Entrada vazia
Texto com múltiplos espaços
Quebras de linha irregulares
Palavras extremamente longas
Caracteres especiais

12. 🧱 Arquitetura do Sistema
O sistema será dividido em módulos:
Entrada de dados
Processamento (formatação)
Saída de dados

13. 🧩 Estrutura Funcional do Sistema
O sistema será organizado em funções com responsabilidades específicas:
🔹 limpar_texto(texto)
Responsável por remover espaços desnecessários e padronizar o texto.

🔹 quebrar_em_palavras(texto)
Responsável por transformar o texto em uma lista de palavras.

🔹 montar_linhas(palavras)
Responsável por construir linhas respeitando o limite de 40 caracteres sem quebrar palavras.

🔹 montar_slides(linhas)
Responsável por agrupar as linhas em blocos de 2 linhas (slides).

🔹 gerar_saida(slides)
Responsável por converter os slides em texto final formatado com separação por linha em branco.

🔹 formatar_letra(texto)
Função principal que orquestra todo o processo.

14. 🎨 Interface do Sistema (Layout Proposto)
A interface deverá conter:
📥 Área de Entrada
Campo de texto grande para inserção da letra

⚙️ Botão de Ação
Botão “Formatar” para processar o texto

📤 Área de Saída
Campo de texto com o resultado formatado

📋 Botões Auxiliares
Botão “Copiar” → copia o resultado
Botão “Limpar” → limpa os campos

15. 📈 Expansões Futuras
🔹 Prioridade Alta
Configuração de:
Número máximo de caracteres por linha
Número de linhas por slide

🔹 Prioridade Média
Identificação automática de:
Versos
Refrões

🔹 Prioridade Baixa
Interface avançada
Integração direta com o Holyrics
Armazenamento de músicas

16. 📅 Cronograma de Desenvolvimento
Fase
Descrição
Planejamento
Definição completa das regras
Estruturação
Organização do sistema
Desenvolvimento
Implementação da lógica
Testes
Validação com músicas reais
Interface
Criação da interface
Ajustes
Correções e melhorias

17. 🧠 Considerações Finais
O projeto LyricFormatter propõe uma solução prática e eficiente para um problema real, com foco em simplicidade, padronização e escalabilidade. A abordagem modular permite evolução contínua sem comprometer a base do sistema.
