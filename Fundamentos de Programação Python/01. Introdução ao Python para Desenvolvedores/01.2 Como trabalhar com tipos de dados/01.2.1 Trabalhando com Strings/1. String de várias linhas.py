# String de Várias Linhas

# Enunciado:
# Você tem um amigo que trabalha em uma empresa de e-learning chamada LLM Camp, onde eles ensinam as pessoas
# a trabalhar com grandes modelos de linguagem (LLMs).
# Eles querem usar o Python para armazenar as avaliações dos usuários e você se ofereceu para ajudar a configurar isso!

# ## Cenário:
# Eles forneceram duas de suas avaliações mais recentes:
# 1. review_one:
#    I really enjoy the courses,
#    and they are easy to fit into my busy schedule. 
#    I wish I had started using your platform sooner.
#    I'll be recommending you to my friends!!
# 2. review_two:
#    One year ago, I was unsure of how to make progress in my career. 
#    Now, I work as a Prompt Engineer, and I can't thank you enough! 
#    Keep up the great work.

# ## Instruções:
# 1. Armazene a primeira avaliação como uma variável de string de várias linhas chamada `review_one`.
# 2. Armazene a segunda avaliação como uma variável de string de várias linhas chamada `review_two`.
# 3. Imprima `review_one` e, em seguida, imprima `review_two`.

# --- Código abaixo ---

# Criação da variável review_one como uma string de várias linhas
review_one = """I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""

# Criação da variável review_two como uma string de várias linhas
review_two = """One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Exibição da primeira avaliação no console
print(review_one)

# Exibição da segunda avaliação no console
print(review_two)