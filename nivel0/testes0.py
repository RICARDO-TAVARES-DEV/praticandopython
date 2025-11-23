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
#-------------------------------------------------------------------
#Exercicio 22 Receba uma frase e mostre quantas palavras tem. 
# frase=input("Digite uma frase: ")
# frase1=frase.replace(" ","")#ele remove os espaços em branco na frase e como ele pediu somente a 
# #a quantidade de letras eu precisei utilizar o metodo replace(" ","")
# frase2=len(frase1)#Aqui eu so precisei utilizar o len para constatar o número de letras na frase toda
# print(frase2)
#--------------------------------------------------------------------------------------------------
#Exercicio 23 Receba uma frase e mostre a primeira palavra.
frase=input("Digite sua frase: ")#aqui eu peço ao usuário uma frase
frase1=frase.replace(" ","")#Eu utilizei o metodo Replace para retirar os espaços em branco e ficar 
#somente com as strings da frase
frase2=(frase1[0:2])#Aqui eu com o conjunto de strings ficou facil em usar a indexação, que é 
#processo de acessar elementos individuais em uma sequência (como strings, listas e tuplas) usando sua posição numérica, começando sempre do 0 para o primeiro elemento. É realizada usando colchetes [] 
print(frase2)
#--------------------------------------------------------------------------------------------------
#Exercicio 24 







        

