from gerar_subchaves import gerar_subchaves

# Teste Gerar Sub Chaves
chave_principal = "1010000010" 
k1, k2 = gerar_subchaves(chave_principal)
print(f"Subchave K1: {k1}")
print(f"Subchave K2: {k2}")