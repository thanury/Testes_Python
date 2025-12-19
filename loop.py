# for numero in range(1,6,2):
#     print('carregando', numero)

# Loop Aninhados
# País + Estação

# paises = ['brasil', 'india', 'estados unidos']
# estacoes_do_ano = ['primavera', 'verão', 'outono', 'inverno']

# for pais in paises:
#     for estacao in estacoes_do_ano:
#         print(f'{pais} {estacao}')

# contador = 1

# while contador <= 120:
#     print(contador)
#     contador += 1

# senha = ''

# while senha != 'secreto':
#     senha = input('Digite a senha: ')

# print('Acesso liberado')

# contador = 100

# while contador >= 1:
#     print(contador)
#     contador -= 1

# estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

# for estilo in estilos:
#     if estilo == 'Rap':
#         continue
#     print(estilo)

estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)
