# #Exercicio 1 Mostre a mensagem "Olá, Mundo!" na tela. 
# print("Olá Mundo !")
# #------------------------------------------------------
# #Exercicio 2 Receba um número e mostre-o na tela. 
# numero=int(input("Digite seu número: "))
# print(numero)
# #-------------------------------------------------------
# #Exercicio 3 Receba um nome e mostre "Bem-vindo, [nome]"
# nome=input("Digite seu nome: ")
# print(f"Bem vindo {nome} ")
# #--------------------------------------------------------
# #Exercicio 4 Receba dois números e mostre a soma. 
# num1=int(input("Digite o primeiro número: "))
# num2=int(input("Digite o segundo número: "))
# soma=num1+num2
# print(soma)
# #----------------------------------------------------------
# #Exercicio 5 Receba dois números e mostre a subtração. 
# num1=3
# num2=9
# subtrai=num2-num1
# print(subtrai)
# #----------------------------------------------------------
# #Exercicio 6 Receba dois números e mostre a multiplicação. 
# num1=int(input("Digite o primeiro número: "))
# num2=int(input("Digite o segundo número: "))
# multi=num1*num2
# print(multi)
# #----------------------------------------------------------
# #Exercicio 7 Receba dois números e mostre a divisão. 
# num1=float(input("Digite o primeiro número: "))
# num2=float(input("digite o segundo número: "))
# divid=num1/num2
# print(divid)
# #--------------------------------------------------------
# #Exercicio 8 Receba um número e mostre o dobro. 
# num1=int(input("Digite um número: "))
# resultado=num1*2
# print(resultado)
# #----------------------------------------------------------
# #Exercicio 9 Receba um número e mostre o triplo. 
# num1=int(input("Digite um número: "))
# resultado=num1*3
# print(resultado)
# #---------------------------------------------------------
# #Exercicio 10 Receba um número e mostre a metade. 
# num1=int(input("Digite um número: "))
# resultado=num1/2
# print(resultado)
# #---------------------------------------------------------
# #Exercicio 11 Receba um número e mostre o quadrado. 
# num1=int(input("Digite um número: "))
# resultado=num1**2
# print(resultado)
# #-----------------------------------------------------
# #Exercicio 12 Receba um número e mostre a raiz quadrada. 
# import math
# num1=int(input("Digite um número : "))
# resultado=math.sqrt(num1)
# print(resultado)
# #-----------------------------------------------------
# #Exercicio 13 Receba um número e mostre se é maior que 10. 
# num1=int(input("Digite um número: "))
# if num1 >10:
#     print(f"O {num1} é maior que 10")
# else:
#     print(f"Esse {num1} não é maior que 10")
# #----------------------------------------------------------------------
# #Exercicio 14 Receba um número e mostre se é menor que 5. 
# num1=int(input("Digite um número: "))
# if num1 <5:
#     print(f"O {num1} é menor que 5.")
# else:
#     print(f"O {num1} é maior que 5.")
# #--------------------------------------------------------------------
# #Exercicio 15  Receba um número e mostre se é igual a 100. 
# num1=int(input("Digite seu número: "))
# if num1==100:#Aqui eu utilizei a condicional IF para verificar se o número digitado é igual(==)
#     print(f"Esse {num1} é igual a 100.")
# else:
#     print(f"Esse {num1} não é igual a 100.")
# #---------------------------------------------------------------------
# #Exercicio 16 Receba um número e mostre se é diferente de 50. 
# num1=int(input("Digite um número :"))
# if num1!=50: #Aqui eu utilizei a condicional IF para verificar se o número digitado é diferente(!=)
#     print(f"Esse {num1} é diferente de 50.")
# else:
#     print(f"Esse {num1} é igual a 50.")
#---------------------------------------------------------------------
# #Exercicio 17  Receba uma palavra e mostre em minúsculas. 
# palavra=input("Digite uma palavra: ")
# palavramenor=palavra.lower()#O metodo LOWER é usado para colocar todas as strings em minusculas
# print(palavramenor)
# #----------------------------------------------------------------
# #Exercicio 18 Receba uma palavra e mostre em maiúsculas. 
# palavra=input("Digite sua palavra: ")
# palavramaior=palavra.upper()#O metodo de string UPPER e usado para colocar todas as strings em #maiuscula.
# print(palavramaior)
#--------------------------------------------------------------
#Exercicio 19 Receba uma palavra e mostre a primeira letra. 
# palavra=input("Digite uma palavra: ")
# letra1=palavra[0]#Eu aqui utilizei a indexação , ou seja ao colocar colchete apos a variavel eu estou #indicando que eu desejo mostrar a posição de um determinado caracter começando sempre pelo zero.
# print(letra1)
#--------------------------------------------------------------
#Exercicio 20 Receba uma palavra e mostre a última letra. 
# palavra=input("Digite sua palavra: ")
# letra2=palavra[9]#Ao usar a indexação, que é processo de acessar elementos individuais em uma sequência #(como strings, listas e tuplas) usando sua posição numérica, começando sempre do 0 para o primeiro #elemento. É realizada usando colchetes [] 
# print(letra2)
# #-----------------------------------------------------------
#Exercicio  21 Receba uma palavra e mostre o número de caracteres. 
# palavra=input("Digite sua palavra: ")
# letra=len(palavra)#aqui o len ele confere o número de caracteres na string.
# print(letra)
#------------------------------------------------------------------------------------------------------
#Exercicio 22 Receba uma frase e mostre quantas palavras tem. 
# frase=input("Digite uma frase: ")
# frase1=frase.replace(" ","")#ele remove os espaços em branco na frase e como ele pediu somente a 
# #a quantidade de letras eu precisei utilizar o metodo replace(" ","")
# frase2=len(frase1)#Aqui eu so precisei utilizar o len para constatar o número de letras na frase toda
# print(frase2)
#--------------------------------------------------------------------------------------------------
#Exercicio 23 Receba uma frase e mostre a primeira palavra.Primeira forma de resolver a questão.
# frase=input("Digite sua frase: ")#aqui eu peço ao usuário uma frase
# frase1=frase.replace(" ","")#Eu utilizei o metodo Replace para retirar os espaços em branco e ficar 
# #somente com as strings da frase
# frase2=(frase1[0:2])#Aqui eu com o conjunto de strings ficou facil em usar a indexação, que é 
# #processo de acessar elementos individuais em uma sequência (como strings, listas e tuplas) usando sua posição numérica, começando sempre do 0 para o primeiro elemento. É realizada usando colchetes [] 
# print(frase2)
#---------------------------------------------------------------------------------------------------------
#Exercicio 23 Receba uma frase e mostre a primeira palavra.Segunda forma de fazer
# frase = input("Digite sua frase: ")
# palavras = frase.split(" ") # divide a frase em lista de palavras
# primeira = palavras[0]#com a indexação eu pego a primeira palavra com o índice zero(0), mas poderia #pegar qualquer posição.ele começa de frente pra trás, ou seja, pega a partir da primeira palavra.
# print(primeira)
#--------------------------------------------------------------------------------------------------
#Exercicio 24 Receba uma frase e mostre a última palavra. 
# frase=input("Digite sua frase: ")
# frase1=(frase.rsplit(" ",1))#divide a frase em duas partes, cortando pelo último espaço.com rsplit
#pois ele começa de trás pra frente
# frase2=frase1[1]#com a indexação eu  pego a segunda parte, ou seja, a última palavra.
# print(frase2)
#-------------------------------------------------------------------------------------------------
#Exercício 25 Receba um número e mostre se é maior que zero. 
# num1=float(input("Digite um número: "))
# if num1>0:#aqui eu informo que se o numero digitado for maior que zero ele retorne a informaçao.
#     print(f"Seu número digitado {num1} é maior que zero")
# else:
#     print(f"Seu número digitado {num1} não é maior que zero")
#-----------------------------------------------------------------------------------------------------
#Exercicio 26 Receba um número e mostre se é menor que zero. 
# num1=float(input("Digite seu número: "))
# if num1<0:#Aqui eu to informando que se o numero digitado for menor que zero retorne a informação.
#     print(f"Seu número digitado {num1} é menor que zero.")
# else:
#     print(f"Seu número digitado {num1} é maior que zero.")
#------------------------------------------------------------------------------------------------------
#Exercício 27 Receba um número e mostre se é igual a zero. 
# num=float(input("Digite seu número: "))
# if num==0:#aqui eu to informando que se o numero digitado for igual a zero ele retorne a informação.
#     print(f"Seu número digitado {num} é igual a zero.")
# else:
#     print(f"Seu número digitado {num} é diferente de zero.")
#--------------------------------------------------------------------------------------------------------
#Exercício 28 Receba um número e mostre se é par.
# num1=float(input("Digite seu número : "))
# if num1%2==0:# aqui eu estou informando que se o numero digitado for divisivel por dois com resto zero ele é par.
#     print(f"Seu número digitado {num1} é par.")
# else:
#     print(f"Seu número diitado {num1} é ímpar.")
#--------------------------------------------------------------------------------------------------------
#Exercicio 29 Receba um número e mostre se é ímpar. 
# num1=float(input("Digite seu número : "))
# if num1%2!=0:# aqui eu estou informando que se o numero digitado for divisivel por dois com resto zero #ele é par.
#     print(f"Seu número digitado {num1} é ímpar.")
# else:
#     print(f"Seu número digitado {num1} é par.")
#---------------------------------------------------------------------------------------------------------
#Exercicio 30 Receba um número e mostre se está entre 1 e 10.
# num=int(input("Digite seu número: "))
# if num>0 and num<11:#Eu só utilizei o método de comparação unindo os numeros maiores que zero e menores que 11.
#     print(f"O número {num} está dntro do intervalo entre 1 e 10.")
# else:
#     print(f"Esse número {num} está fora do intervalo.")
#---------------------------------------------------------------------------------------------------------#Exercicio 31 Receba um número e mostre se está fora do intervalo 1 a 10. 
# num=int(input("Digite seu número: "))
# if num>0 and num<11:#Eu só utilizei o método de comparação unindo os numeros maiores que zero e menores que 11.
#     print(f"O número {num} está dntro do intervalo entre 1 e 10.")
# else:
#     print(f"Esse número {num} está fora do intervalo entre 1 e 10.")
#---------------------------------------------------------------------------------------------------------
#Exercicio 32 Receba um número e mostre se é múltiplo de 2. 
# num=float(input("Digite seu número: "))
# if num%2==0:
#     print(f"O número {num} é múltiplo de 2.")
# else:
#     print(f"Este número {num} não é múltiplo de 2.")
#---------------------------------------------------------------------------------------------------------#Exercicio 33 Receba um número e mostre se é múltiplo de 5. 
# num=float(input("Digite seu número: "))
# if num%5==0:
#     print(f"Esse número {num} é múltiplo de 5.")
# else:
#     print(f"Esse número {num} não é múltiplo de 5.")
#---------------------------------------------------------------------------------------------------------#Exercício 34 Receba um número e mostre se é múltiplo de 10.
# num=float(input("Digite seu número: "))
# if num%10==0:
#     print(f"Esse número {num} é múltiplo de 10.")
# else:
#     print(f"Esse número {num} não é múltiplo de 10.")
#---------------------------------------------------------------------------------------------------------#Exercício 35 Receba um número e mostre se é múltiplo de 3. 
# num=float(input("Digite seu número: "))
# if num%3==0:
#     print(f"Esse número {num} é múltiplo de 3.")
# else:
#     print(f"Esse número {num} não é múltiplo de 3.")
#---------------------------------------------------------------------------------------------------------#Exercicio 36 Receba um número e mostre se é múltiplo de 7.
num=float(input("Digite seu número: "))
if num%7==0:
    print(f"Esse número {num} é múltiplo de 7.")
else:
    print(f"Esse número {num} não é multiplo de 7.")
#---------------------------------------------------------------------------------------------------------#     






        

