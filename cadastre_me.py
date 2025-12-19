from datetime import datetime
import random

# Lista de cartões
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']

# 1. Obter nome do usuário
nome = input('Digite seu nome: ')

# 2. Obter idade do usuário
idade = int(input('Digite sua idade: '))

# 3. Data automática de cadastro
data_cadastro = datetime.now().strftime('%d/%m/%Y')

# 4. Sortear cartão
cartao_sorteado = random.choice(cartoes)

# Exibir resultado
print('\n--- Registro do Funcionário ---')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Data de cadastro: {data_cadastro}')
print(f'Cartão recebido: {cartao_sorteado}')
