def permutacao(bits, tabela):
    return ''.join(bits[i - 1] for i in tabela)

def deslocamento_circular(bits, deslocamento):
    return bits[deslocamento:] + bits[:deslocamento]

def gerar_subchaves(chave_10bits):
    
    tabela_p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    chave_permutada = permutacao(chave_10bits, tabela_p10)

    metade_esquerda = chave_permutada[:5]
    metade_direita = chave_permutada[5:]

    metade_esquerda = deslocamento_circular(metade_esquerda, 1)
    metade_direita = deslocamento_circular(metade_direita, 1)

    tabela_p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    k1 = permutacao(metade_esquerda + metade_direita, tabela_p8)

    metade_esquerda = deslocamento_circular(metade_esquerda, 2)
    metade_direita = deslocamento_circular(metade_direita, 2)

    k2 = permutacao(metade_esquerda + metade_direita, tabela_p8)

    return k1, k2
