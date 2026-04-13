# formatador.py

def quebrar_linha_longa(linha, limite=40):
    """Fatia uma linha que ultrapassa o limite sem cortar palavras ao meio."""
    palavras = linha.split()
    novas_linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= limite:
            linha_atual = palavra if linha_atual == "" else linha_atual + " " + palavra
        else:
            novas_linhas.append(linha_atual)
            linha_atual = palavra
            
    if linha_atual:
        novas_linhas.append(linha_atual)
    return novas_linhas

def formatar_musica(texto_bruto, limite_caracteres=40, linhas_por_slide=2, mostrar_tags=True):
    """
    Processa o texto da música com parâmetros flexíveis.
    - limite_caracteres: Máximo de letras por linha.
    - linhas_por_slide: Quantas linhas aparecem antes do próximo [SLIDE].
    - mostrar_tags: Se False, remove [SLIDE], o tracejado e o FIM DA ESTROFE.
    """
    # Separa o texto por blocos (estrofes)
    estrofes = texto_bruto.split("\n\n")
    texto_final = ""

    for estrofe in estrofes:
        if not estrofe.strip():
            continue
            
        linhas_originais = estrofe.strip().split("\n")
        linhas_finais = []

        # Etapa 1: Quebra as linhas respeitando o novo limite de caracteres
        for linha in linhas_originais:
            if len(linha) <= limite_caracteres:
                linhas_finais.append(linha.strip())
            else:
                linhas_finais.extend(quebrar_linha_longa(linha, limite_caracteres))

        # Etapa 2: Agrupa as linhas conforme a quantidade definida (linhas_por_slide)
        for i in range(0, len(linhas_finais), linhas_por_slide):
            if mostrar_tags:
                texto_final += "[SLIDE]\n"
            
            # Adiciona a quantidade de linhas solicitada para este slide
            for j in range(linhas_por_slide):
                if i + j < len(linhas_finais):
                    texto_final += linhas_finais[i+j] + "\n"
            
            if mostrar_tags:
                texto_final += "-" * 20 + "\n\n"
            else:
                texto_final += "\n" # Apenas um espaço entre slides se estiver sem tags

        if mostrar_tags:
            texto_final += ">>> FIM DA ESTROFE <<<\n\n"
        else:
            texto_final += "\n" # Espaço extra entre estrofes mesmo sem tags
    
    return texto_final.strip()