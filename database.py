import mysql.connector

def conectar():
    try:
        # Aqui você coloca os dados que usou no Workbench
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="usbw",  # Se tiver senha, coloque aqui
            database="db_louvor"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None

def salvar_musica(titulo, artista, letra_original, letra_formatada):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO musicas (titulo, artista, letra_original, letra_formatada) VALUES (%s, %s, %s, %s)"
        valores = (titulo, artista, letra_original, letra_formatada)
        
        cursor.execute(sql, valores)
        conexao.commit() # Importante: Salva as mudanças no banco
        
        cursor.close()
        conexao.close()
        return True
    return False

def buscar_musicas():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT titulo FROM musicas")
        resultados = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        return resultados
    return []