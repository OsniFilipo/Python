## Exemplos de Funções Disponíveis

# Função para Calcular a Média de uma Lista de Números

def calcular_media(lista):
    """Calcula a média dos valores em uma lista."""
    total = sum(lista)  # Calcula a soma dos valores na lista
    media = total / len(lista)  # Calcula a média dividindo a soma pelo número de elementos
    return media

# Exemplo de uso da função calcular_media
numeros = [2, 4, 6, 8, 10]
media = calcular_media(numeros)
print("A média dos números é:", media)

# Função para Verificar se uma Palavra é Palíndromo

def verificar_palindromo(palavra):
    """Verifica se uma palavra é um palíndromo."""
    palavra_invertida = palavra[::-1]  # Inverte a palavra usando slicing
    return palavra == palavra_invertida

# Exemplo de uso da função verificar_palindromo
palavra = "radar"
if verificar_palindromo(palavra):
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")

# Função para Converter Graus Celsius para Fahrenheit

def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura em graus Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32  # Fórmula de conversão de Celsius para Fahrenheit
    return fahrenheit

# Exemplo de uso da função celsius_para_fahrenheit
temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)