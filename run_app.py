import os
import subprocess
import sys
from encrypt import encrypt, decrypt

def instalar_flask():
    """Instala o Flask caso não esteja instalado."""
    try:
        import flask
        print("Flask já está instalado!")
    except ImportError:
        print("Flask não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
        print("Flask instalado com sucesso!")

def testar_codigo():
    chave_principal = "1010000010"
    dados = "11010111"
    print("Teste da Logica de Criptografia...")
    print(f"Chave Principal: {chave_principal}")
    print(f"Bloco de Dados: {chave_principal}")
    dados_cripogradado = encrypt(chave_principal,dados)
    print(f"Dado cripografado: {dados_cripogradado}")
    dados_descripogrado = decrypt(chave_principal,dados_cripogradado)
    print(f"Dado descripografado: {dados_descripogrado}")
    if dados_descripogrado == dados:
        print("Dados são iguais: Teste concluido com sucesso!")
    else:
        print("Falha")

def executar_app():
    """Executa o arquivo app.py."""
    if os.path.exists("app.py"):
        print("Executando o arquivo app.py...")
        subprocess.run([sys.executable, "app.py"])
    else:
        print("Erro: O arquivo app.py não foi encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    instalar_flask()
    testar_codigo()
    executar_app()
