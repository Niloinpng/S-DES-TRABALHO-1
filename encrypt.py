from gerar_subchaves import gerar_subchaves
from gerar_subchaves import permutacao

def permutacao_inicial(bloco_8bits):
    tabela_ip = [2, 6, 3, 1, 4, 8, 5, 7] 
    return permutacao(bloco_8bits, tabela_ip)

def permutacao_final(bloco_8bits):
    tabela_ip_inversa = [4, 1, 3, 5, 7, 2, 8, 6]  # Tabela de permutação final
    return permutacao(bloco_8bits, tabela_ip_inversa)


def dividir_em_metades(bloco_8bits):
    metade_esquerda = bloco_8bits[:4]
    metade_direita = bloco_8bits[4:]
    return metade_esquerda, metade_direita

def funcao_f(metade_direita, subchave):
    tabela_ep = [4, 1, 2, 3, 2, 3, 4, 1]
    expandido = permutacao(metade_direita, tabela_ep)

    xor_resultado = ''.join(str(int(expandido[i]) ^ int(subchave[i])) for i in range(8))

    sbox0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    sbox1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    def sbox_lookup(sbox, entrada):
        linha = int(entrada[0] + entrada[3], 2)
        coluna = int(entrada[1] + entrada[2], 2)
        return format(sbox[linha][coluna], '02b')

    metade_esquerda, metade_direita = xor_resultado[:4], xor_resultado[4:]
    sbox_saida = sbox_lookup(sbox0, metade_esquerda) + sbox_lookup(sbox1, metade_direita)

    tabela_p4 = [2, 4, 3, 1]
    return permutacao(sbox_saida, tabela_p4)

def rodada_feistel(l, r, subchave):
    resultado_f = funcao_f(r, subchave)
    nova_metade_esquerda = ''.join(str(int(l[i]) ^ int(resultado_f[i])) for i in range(4))
    return r, nova_metade_esquerda 

# 1. Gerar Sub Chaves
chave_principal = "1010000010" 
k1, k2 = gerar_subchaves(chave_principal)
print(f"Subchave K1: {k1}")
print(f"Subchave K2: {k2}")

# 2. Permutação Inicial
bloco_dados = "11010111"  
bloco_permutado = permutacao_inicial(bloco_dados)
print(f"Bloco após Permutação Inicial: {bloco_permutado}")

# 3. Dividir em Metades 
l, r = dividir_em_metades(bloco_permutado)
print(f"Metade Esquerda (L): {l}")
print(f"Metade Direita (R): {r}")

# 4. Rodadas de Feistel 
# 4.1. Primeira rodada com K1
l, r = rodada_feistel(l, r, k1)
print(f"Após primeira rodada - L: {l}, R: {r}")

# 4.2. Segunda rodada com K2 (sem troca de metades no final)
l, r = rodada_feistel(l, r, k2)
print(f"Após segunda rodada - L: {l}, R: {r}")

# 5. Permutação Final (IP-^1)
bloco_final = permutacao_final(r + l)  # R + L pois não trocamos no final
print(f"Bloco após Permutação Final (IP-^1): {bloco_final}")