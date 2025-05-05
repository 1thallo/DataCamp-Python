# Trabalhando com Dicionários

# Enunciado:
# Você tem estado ocupado, adicionando mais artistas e músicas ao seu dicionário `playlist` em preparação para a festa!
# Como lembrete, ele contém nomes de artistas como chaves e nomes de músicas como valores.
# Neste exercício, você acessará partes do dicionário e adicionará um novo artista e uma nova música.

# ## Instruções:
# 1. Imprima o nome da música na `playlist` que é do artista "Coldplay".
# 2. Adicione um novo par chave-valor à `playlist`, em que a chave é "Usher" e o valor é "Yeah!".
# 3. Imprima somente as músicas na `playlist`.

# --- Código abaixo ---

# 1. Imprimir o nome da música do artista "Coldplay"
print(playlist["Coldplay"]) 

# 2. Adicionar um novo par chave-valor à playlist
playlist["Usher"] = "Yeah!" 

# 3. Imprimir somente as músicas na playlist
print(playlist.values()) 