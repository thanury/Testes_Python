# Pode ter 'ou ""
# print('Codar todos os dias')

# # Quando a frase ocupar mais de uma linha
# print("""Estamos codando todos os dias
# E estou aprendendo muito""")   

# #Caracteres de escape
# print('Olá meu nom é \nThanury')

# # \ ignorar o caractere de error e aparece assim mesmo
# print('Codar todos \'os dias')

# nome = 'carol'
# print(len(nome))

# como colocar comentário em 1 ou varias linhas selecionadas: ⌘ + /

# print('vamos codar!')
# print('vamos \'codar!')
# print("""vamos 
# \'codar!""")

# nome = 'Thanury'
# email = 'thanurytanisue@gmail.com'
# print(f'Olá {nome}, você cadastrou o email {email}, essa informação está correta?')

# Métodos de string
# nome_curso = 'edição de vídeo'
# print(nome_curso.upper())
# print(nome_curso.lower())
# print(nome_curso.strip())
# print(nome_curso.lstrip())
# print(nome_curso.rsplit())
# print(nome_curso.find('ção'))
# print(nome_curso.replace('vídeo', 'música'))

# teclado = 'teclado'
# print(teclado[4])
# print(teclado[-1])
# print(teclado.index('l'))
# print(teclado[teclado.index('l')])
# print(teclado[0:])
# print(teclado[0:5])

# frase = 'Olá, bem-vindo a este treinamento!'
# print(frase.split())
# print(frase.split(','))
# print(frase.split('-'))


# hashtags = 'music #guitar #gamer #coder #python'
# print(hashtags.split())
# print(hashtags.split('#'))
# print(hashtags.split('#',3))

# # Como concatenar (combinar) strings
# hashtag_separadas_por_espaco = hashtags.split(' ')
# print(hashtag_separadas_por_espaco)
# print(','.join(hashtag_separadas_por_espaco))
# print('.'.join(hashtag_separadas_por_espaco))
# print(' '.join(hashtag_separadas_por_espaco))

# #Recebendo dados do usuário
# senha = input('Digite sua senha: ')
# print(senha)
# print(type(senha))

# qunat_filmes = int(input('Quantos filmes você viu esse mês? '))
# print(type(qunat_filmes))

# a = 20
# b = 20.5
# print(type(a))
# print(type(b))

# from datetime import datetime
# # print(datetime.now())
# # print(datetime.now().day)
# # print(datetime.now().month)

# # Criar data
# lacamento = datetime(2021,5,28)
# print(lacamento)

#Valores aleatórios com random
# import random
# print(random.randint(4,10))