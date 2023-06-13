# Operadores Aritméticos

a = 10  # atribuição
b = 3

soma = a + b  # Realiza a soma de 'a' e 'b' (resultado: 13)
subtracao = a - b  # Realiza a subtração de 'b' de 'a' (resultado: 7)
multiplicacao = a * b  # Realiza a multiplicação de 'a' e 'b' (resultado: 30)
divisao = a / b  # Realiza a divisão de 'a' por 'b' (resultado: 3.3333333333333335)
divisao_inteira = a // b  # Realiza a divisão inteira de 'a' por 'b' (resultado: 3)
resto = a % b  # Calcula o resto da divisão de 'a' por 'b' (resultado: 1)
exponencial = a**b  # Calcula 'a' elevado à potência 'b' (resultado: 1000)

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto, exponencial)
# Imprime os resultados das operações aritméticas

print('A soma de {} com {} é: {}'.format(a, b, soma))
# Imprime a mensagem "A soma de 10 com 3 é: 13" usando formatação de string

print(f'A soma de {a} com {b} é: {soma}')
# Outra forma de imprimir a mensagem usando f-strings

# Operadores de Atribuição

c = 5
d = 2

c += d  # Equivalente a c = c + d (resultado: 7)
c -= d  # Equivalente a c = c - d (resultado: 5)
c *= d  # Equivalente a c = c * d (resultado: 10)
c /= d  # Equivalente a c = c / d (resultado: 5.0)
c //= d  # Equivalente a c = c // d (resultado: 2)
c %= d  # Equivalente a c = c % d (resultado: 0)
c **= d  # Equivalente a c = c ** d (resultado: 0)

# Operadores de Comparação

e = 5
f = 3

igual = e == f  # Verifica se 'e' é igual a 'f' (resultado: False)
diferente = e != f  # Verifica se 'e' é diferente de 'f' (resultado: True)
maior_que = e > f  # Verifica se 'e' é maior que 'f' (resultado: True)
maior_ou_igual = e >= f  # Verifica se 'e' é maior ou igual a 'f' (resultado: True)
menor_que = e < f  # Verifica se 'e' é menor que 'f' (resultado: False)
menor_ou_igual = e <= f  # Verifica se 'e' é menor ou igual a 'f' (resultado: False)

# Operadores Lógicos

g = True
h = False

e_logico = g and h  # Verifica se 'g' e 'h' são ambos verdadeiros (resultado: False)
ou_logico = g or h  # Verifica se 'g' ou 'h' é verdadeiro (resultado: True)
nao_logico = not g  # Inverte o valor de 'g' (resultado: False)
