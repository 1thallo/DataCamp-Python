# Subdivisão de Listas

# Enunciado:
# Você expandiu sua playlist. Ela ainda contém a ordem e os nomes das músicas, mas agora você também adicionou
# o nome do artista para cada música, bem como algumas músicas adicionais!
# A playlist segue o padrão:
# 1) número da música, 2) nome da música, 3) nome do artista, e repete.
# Essa é uma ótima oportunidade para praticar a extração de informações específicas da sua lista.

# ## Instruções:
# 1. Localize o nome da segunda música, que é o quinto elemento, em `playlist`, e imprima o valor.
# 2. Imprima o nome do artista da última música da playlist.
# 3. Imprima cada nome de música da playlist.

# --- Código abaixo ---

# Playlist expandida
playlist = [
    1, 'Blinding Lights', 'The Weeknd',
    2, 'One Dance', 'Drake',
    3, 'Uptown Funk', 'Mark Ronson',
    4, 'Closer', 'The Chainsmokers',
    5, 'One Kiss', 'Calvin Harris',
    6, 'Mr. Brightside', 'The Killers'
]

# 1. Localizar o nome da segunda música (quinto elemento da lista)
# O índice 4 corresponde ao nome da segunda música.
print(playlist[4])  # Saída esperada: "One Dance"

# 2. Imprimir o nome do artista da última música
# O índice -1 corresponde ao último elemento da lista.
print(playlist[-1])  # Saída esperada: "The Killers"

# 3. Imprimir cada nome de música da playlist
# Usando slicing para pegar todos os nomes das músicas (começando no índice 1 e pulando de 3 em 3).
print(playlist[1::3])  # Saída esperada: ['Blinding Lights', 'One Dance', 'Uptown Funk', 'Closer', 'One Kiss', 'Mr. Brightside']