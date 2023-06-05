<img src="https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg" width="1028">

# Primeiros passos para estudar Python

Apresentar os conceitos fundamentais do "Olá, Mundo!", variáveis e operações aritméticas. Aqui, você encontrará exemplos práticos e explicações detalhadas para auxiliar no seu aprendizado da linguagem de programação Python.

# <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"> Olá, Mundo !

O famoso "Olá Mundo!" é o ponto de partida para muitos programadores iniciantes. É uma tradição que marca o início da jornada de aprendizado em várias linguagens de programação, incluindo Python.

Em Python, para exibir a frase "Olá Mundo!" na tela, utilizamos a função print(). A função print() é uma função embutida do Python que nos permite exibir mensagens e resultados no console.

```

  print()
  
```

Quando escrevemos o código print("Olá Mundo!") e o executamos, o Python interpreta essa instrução e exibe a mensagem "Olá Mundo!" no console ou terminal.

O "Olá Mundo!" em Python é mais do que apenas uma frase simples. É a prova de que você entrou no mundo da programação e que está pronto para explorar e criar coisas incríveis. É o primeiro passo em direção a uma compreensão mais profunda dos conceitos de programação e ao desenvolvimento de habilidades de resolução de problemas.

À medida que você avança em sua jornada em Python, o "Olá Mundo!" se torna apenas o começo. Você começará a escrever programas mais complexos, criar aplicações interativas, desenvolver projetos de Data Science e muito mais. Mas, independentemente do quão longe você chegue, o "Olá Mundo!" sempre será uma lembrança especial e um marco de suas primeiras conquistas na programação.

Então, da próxima vez que você escrever print("Olá Mundo!") em Python, lembre-se de apreciar o significado simbólico por trás dessa simples linha de código. Celebre seu progresso, mantenha-se motivado e continue explorando as infinitas possibilidades que a programação em Python oferece.

```

  print("Olá Mundo!")
  
```

Parabéns por dar o primeiro passo em direção ao incrível mundo da programação!

# Variáveis

As variáveis são elementos fundamentais em qualquer linguagem de programação. Neste repositório, você aprenderá como declarar variáveis em Python, atribuir valores a elas e usar diferentes tipos de dados, como números, strings e booleanos. Além disso, abordaremos conceitos como escopo de variáveis e boas práticas de nomenclatura.

As variáveis em Python são usadas para armazenar e manipular dados. Elas são essenciais para o desenvolvimento de programas, permitindo que você atribua valores a nomes e os utilize posteriormente no código. Aqui estão algumas informações importantes sobre variáveis em Python, juntamente com exemplos:

1.  Declaração de variáveis: Em Python, você pode declarar uma variável atribuindo um valor a ela usando o sinal de igual (=). O nome da variável pode conter letras, números e [underscores](https://www.significados.com.br/underline/#:~:text=Underline%20(%20_%20)%2C%20tamb%C3%A9m%20conhecido,interpretado%20como%20uma%20informa%C3%A7%C3%A3o%20v%C3%A1lida.), mas deve começar com uma letra ou underscore. Python diferencia maiúsculas de minúsculas nos nomes das variáveis.

Exemplo:

```

  x = 5                        # Atribui o valor 5 à variável x
  nome = "João"                # Atribui o valor "João" à variável nome
  saldo_conta = 1000.50        # Atribui o valor 1000.50 à variável saldo_conta

  
```

2. Tipos de dados das variáveis: Em Python, as variáveis são dinamicamente tipadas, o que significa que você não precisa declarar explicitamente o tipo de dados que elas irão armazenar. O tipo de dados é inferido automaticamente com base no valor atribuído à variável.

Exemplo:

```

  x = 5                         # x é do tipo int (inteiro)
  nome = "João"                 # nome é do tipo str (string)
  saldo_conta = 1000.50         # saldo_conta é do tipo float (número de ponto flutuante)

```

3. Acesso e manipulação de variáveis: Você pode acessar o valor de uma variável usando seu nome. Também é possível modificar o valor de uma variável atribuindo um novo valor a ela.

Exemplo:

```

x = 5                        # Atribui o valor 5 à variável x
print(x)                     # Imprime o valor de x (5)

x = x + 1                    # Aumenta o valor de x em 1
print(x)                     # Imprime o novo valor de x (6)

```

4. Convenções de nomenclatura: É uma prática comum usar nomes descritivos para as variáveis, para que outros programadores (e você mesmo) possam entender facilmente o propósito e o conteúdo da variável. Por convenção, em Python, recomenda-se usar letras minúsculas e underscores para separar palavras em nomes de variáveis.

Exemplo:

```

saldo_conta = 1000.50       # Nome descritivo para a variável
idade_usuario = 25          # Outro exemplo de nome descritivo


```

5. Tipagem dinâmica: Em Python, você pode atribuir um novo valor a uma variável, mesmo que o tipo de dados seja diferente do valor anterior. Python permite a reatribuição dinâmica de tipos de dados.

Exemplo:

```

x = 5                   # x é do tipo int
print(x)                # Imprime o valor de x (5)

x = "Olá"               # x agora é do tipo str
print(x)                # Imprime o novo valor de x ("Olá")


```
Outro exemplo pode ser visto no [variaveis.py](https://github.com/OsniFilipo/Python/blob/main/01%20-%20Projeto%20inicial/variaveis.py)

As variáveis em Python são uma maneira flexível e poderosa de armazenar e manipular dados em seu programa. Elas permitem que você trabalhe com diferentes tipos de dados e realizem operações com eles. Use nomes descritivos para suas variáveis e lembre-se de atualizá-las conforme necessário durante a execução do seu programa.
# Operações Aritméticas
Python oferece uma ampla variedade de operações aritméticas para trabalhar com números. Neste repositório, você encontrará explicações e exemplos práticos sobre adição, subtração, multiplicação, divisão e exponenciação. Além disso, exploraremos o uso de operadores especiais, como módulo e divisão inteira.

# Exemplo de Código
Para facilitar o seu aprendizado, forneceremos exemplos de código práticos em cada seção. Esses exemplos demonstrarão como aplicar os conceitos discutidos, permitindo que você veja o Python em ação. Sinta-se à vontade para experimentar, modificar e expandir esses exemplos para aprimorar sua compreensão e habilidades em Python.

# Os comentários

Os comentários são uma parte importante da programação em Python. Eles são trechos de texto que não são executados pelo interpretador Python, servindo apenas como notas ou explicações para facilitar o entendimento do código pelos programadores. Os comentários fornecem informações adicionais sobre o que o código faz, sua lógica ou outras considerações importantes. Aqui estão alguns pontos-chave sobre os comentários em Python:

1. Propósito dos comentários: Os comentários são usados para adicionar informações úteis ao código, tornando-o mais compreensível e facilitando sua manutenção. Eles ajudam outros programadores (ou até mesmo você mesmo, no futuro) a entender o que o código faz e como ele funciona.

2. Sintaxe dos comentários: Em Python, os comentários são precedidos pelo caractere cerquilha (#). Qualquer texto após o # em uma linha é considerado um comentário e será ignorado pelo interpretador. Os comentários podem aparecer em uma linha separada ou após o código em uma mesma linha.

Exemplo:

```

  # Este é um comentário em Python

  print("Olá Mundo!")  # Este é outro comentário


```

3. Comentários de uma linha: Os comentários de uma linha são usados para adicionar breves explicações ou notas ao código. Eles são ideais para fornecer contexto sobre o que está acontecendo em uma linha específica.

Exemplo:

```

  x = 10  # Atribuindo o valor 10 à variável x

```
4. Comentários de várias linhas: Os comentários de várias linhas são usados quando você precisa adicionar comentários extensos que abrangem várias linhas. Em Python, você pode criar um bloco de comentário usando três aspas simples (''') ou três aspas duplas (""").

Exemplo:

```

  '''
  Este é um comentário de várias linhas.
  Ele pode abranger várias linhas de código e é usado
  para fornecer explicações detalhadas ou documentação.
  '''

```

5. Boas práticas ao usar comentários: Mantenha os comentários claros, concisos e relevantes. Eles devem explicar o código de forma eficaz e ajudar os leitores a entender a lógica por trás dele. Evite comentários óbvios ou desnecessários que não adicionem valor ao código. Além disso, os comentários devem ser atualizados junto com o código. À medida que você faz alterações no código, lembre-se de revisar e atualizar os comentários relevantes para garantir que eles permaneçam precisos e úteis.

Os comentários são uma ferramenta valiosa para melhorar a legibilidade e a manutenção do seu código Python. Use-os sabiamente para fornecer informações claras e úteis, tornando seu código mais compreensível tanto para você quanto para outros programadores.




