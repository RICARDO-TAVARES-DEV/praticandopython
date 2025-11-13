#Exercicios de logica de programação
# # Exercicio 0 (Extra)
# # Soma de dois números
# # Solicitando ao usuário o nome
# nome = input("Digite seu nome por gentileza: ")

# # Solicitando ao usuário os números para realizar a soma
# n1 = int(input(f"{nome}, digite um número: "))
# n2 = int(input(f"{nome}, digite outro número: "))

# # Faz a soma
# soma = n1 + n2

# # Exibe o resultado
# print(f"{nome}, a sua soma tem o seguinte resultado: {soma}")
# # estou tentando comentar

# # Exercicio 1
# # Solicitar ao usuário um número e verificar se este é par ou ímpar
# nome=input("Digite seu nome por favor.")
# n1=int(input(f"{nome}, digite um número: "))

# if n1%2 == 0:
#     print(f"{nome}, o seu número digitado,{n1} é par.")
# else:
#     print(f"{nome},seu numero digitado é ímpar.")

#Exercicio 2
#Criar uma calculadora
# usuario = input("Digite seu nome por gentileza: ")

# numero1 = int(input(f"{usuario}, digite o seu primeiro número: "))
# numero2 = int(input(f"{usuario}, digite o seu segundo número: "))

# operador = input(f"{usuario}, escolha a operação (+, -, *, /): ")

# if operador == "+":
#     resultado = numero1 + numero2
#     print(f"{usuario}, o resultado da soma é: {resultado}")
# elif operador == "-":
#     resultado = numero1 - numero2
#     print(f"{usuario}, o resultado da subtração é: {resultado}")
# elif operador == "*":
#     resultado = numero1 * numero2
#     print(f"{usuario}, o resultado da multiplicação é: {resultado}")
# elif operador == "/":
#     resultado = numero1 / numero2
#     print(f"{usuario}, o resultado da divisão é: {resultado}")
# else:
#     print(f"{usuario}, operação inválida.")

#Exercicio 3
#Fatorial de 1 ate 10 numeros
# usuario = input("Digite seu nome por favor: ")
# numero = int(input(f"Digite o seu número {usuario}: "))

# fatorial = 1
# for i in range(1, numero+1):
#     fatorial *= i

# print(f"{usuario}, o fatorial de {numero} é {fatorial}")

#Exercicio 4 Uma sequencia de 5 números solicitados e mostrar a média dos 5 números 
# num1=int(input("Digite o primeiro número: "))
# num2=int(input("Digite o segundo número: "))
# num3=int(input("Digite o terceiro número: "))
# num4=int(input("Digite o quarto número: "))
# num5=int(input("Digite o quinto número: "))
# media=(num1+num2+num3+num4+num5)/(5)
# print(f"A média dos números digitados é : {media}")

#Exercicio 5 Pedir dois numeros um é a base e o outro é o expoente e calcular a potência da base
base=int(input("Digite seu número de base por favor: "))
expoente=int(input("Digite o seu expoente por gentileza: "))
potencia=(base**expoente)
print(f"A potencia de sua base {base} elevada a {expoente} é {potencia} . ")

