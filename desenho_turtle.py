from turtle import Turtle, Screen

# Cria a tela
tela = Screen()
tela.title("Mini Game Turtle")

# Cria a turtle
t = Turtle()
t.speed(3)

# Loop principal
continuar = 's'

while continuar == 's':

    # Movimento
    direcao = input('Mover para frente ou para trás? (f/t): ').lower()
    distancia = int(input('Quantos pixels deseja mover? '))

    if direcao == 'f':
        t.forward(distancia)
    elif direcao == 't':
        t.backward(distancia)

    # Rotação
    rotacao = input('Rotacionar para esquerda ou direita? (e/d): ').lower()
    angulo = int(input('Quantos graus deseja rotacionar? '))

    if rotacao == 'e':
        t.left(angulo)
    elif rotacao == 'd':
        t.right(angulo)

    # Continuar?
    continuar = input('Continuar andando? (s/n): ').lower()

# Mantém a tela aberta
tela.exitonclick()
