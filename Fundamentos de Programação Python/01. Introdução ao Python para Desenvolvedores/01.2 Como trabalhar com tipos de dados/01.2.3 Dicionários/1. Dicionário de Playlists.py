# Dicionário de Playlists

# Enunciado:
# Com seu novo conhecimento sobre dicionários, você decide traduzir sua playlist de uma lista para um dicionário!
# Como lembrete, este é o conteúdo da playlist:
# [1, "Blinding Lights", "The Weeknd", 2, "One Dance", "Drake",
#  3, "Uptown Funk", "Mark Ronson", 4, "Closer", "The Chainsmokers",
#  5, "One Kiss", "Calvin Harris", 6, "Mr. Brightside", "The Killers"]
#
# Os nomes das músicas começam no segundo índice "Blinding Lights" e compõem cada terceiro valor a partir daí.
# Os nomes dos artistas começam no terceiro índice "The Weeknd" e também compõem cada terceiro valor posterior.

# ## Instruções:
# 1. Crie um dicionário chamado `playlist` contendo as duas primeiras músicas, nessa ordem,
#    com os nomes dos artistas como chaves e suas respectivas músicas como valores.
# 2. Imprima o dicionário.

# --- Código abaixo ---

# Criação do dicionário playlist com as duas primeiras músicas
playlist = {
    "The Weeknd": "Blinding Lights",  # Artista: Música
    "Drake": "One Dance"
}

# Exibição do dicionário playlist no console
print(playlist)