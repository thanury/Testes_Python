# Calculadora de Preço de Corte de Cabelo

# Variável que representa o tamanho do cabelo em centímetros
tamanho_cabelo_cm = 45

# Condicional para definir o preço do corte
if tamanho_cabelo_cm <= 20:
    print('O valor do corte é R$50,00')

elif tamanho_cabelo_cm <= 30:
    print('O valor do corte é R$70,00')

elif tamanho_cabelo_cm <= 50:
    print('O valor do corte é R$100,00')

else:
    print('Acima de 50cm, favor consultar na recepção')