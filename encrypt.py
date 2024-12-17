from gerar_subchaves import gerar_subchaves
from gerar_subchaves import permutacao

def permutacao_inicial(bloco_8bits):
    tabela_ip = [2, 6, 3, 1, 4, 8, 5, 7]  # Tabela de permutação inicial
    return permutacao(bloco_8bits, tabela_ip)

# Teste Gerar Sub Chaves
chave_principal = "1010000010"  # Chave de 10 bits fornecida no problema
k1, k2 = gerar_subchaves(chave_principal)
print(f"Subchave K1: {k1}")
print(f"Subchave K2: {k2}")

# Permutação Inicial
bloco_dados = "11010111"  # Bloco de dados de 8 bits fornecido
bloco_permutado = permutacao_inicial(bloco_dados)
print(f"Bloco após Permutação Inicial: {bloco_permutado}")