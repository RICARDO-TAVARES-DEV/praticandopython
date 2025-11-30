#*****************************INICIANTE**********************************************
#Exercicio 1: Crie uma lista com números de 1 a 5 e adicione o número 6 ao final. 
numeros=[1,2,3,4,5]
numeros.append(6)#com o comando append inseririmos um elemento no final da lista.
print(numeros)
#---------------------------------------------------------------------------------

#Exercicio 2: Crie um array de inteiros [2, 4, 6, 8] e substitua o valor da posição 2 por 10. 
numeros=[2,4,6,8]
numeros[2]=10
print(numeros)
#------------------------------------------------------------------------------------------

#Exercicio 3: Crie um dicionário com "produto": "caneta" e "preço": 2.50 e imprima o preço. 
loja={
    "produto":"caneta",
    "preço":2.50
}
print(loja["preço"])
#-------------------------------------------------------------------------------------------

#Exercicio 4: Remova o último elemento de uma lista [1, 2, 3, 4] usando pop(). 
numeros=[1,2,3,4]
numeros.pop(3)
print(numeros)
#-------------------------------------------------------------------------------------------
#Exercicio 5: Verifique se a chave "idade" existe em um dicionário {"nome": "Ana", "idade": 25}. 
alunos={
    "nome":"Ana",
    "idade":25,
}
print(alunos.get("idade"))
#-------------------------------------------------------------------------------------------
#Exercicio 6: Crie uma lista com os números [10, 20, 30] e insira o número 15 na posição 1. 
numeros=[10,20,30]
numeros[0]=15#indexação para insesubstituir o primeiro elemento pelo 15.
print(numeros)
#-------------------------------------------------------------------------------------------

#Exercicio 7: Crie um dicionário com "cidade": "Rio" e "estado": "RJ" e adicione a chave "país": "Brasil". 
cadastro={
    "cidade":"Rio de Janeiro",
    "estado":"RJ",
}
cadastro.setdefault("país","Brasil")
print(cadastro)
#-------------------------------------------------------------------------------------------

#Exercicio 8: Crie um array [1, 2, 3, 4] e imprima o tamanho usando len(). 
numeros=[1,2,3,4]
print(len(numeros))
#-------------------------------------------------------------------------------------------

#Exercicicio 9: Crie uma lista com [5, 10, 15] e multiplique o segundo elemento por 2. 
numeros=[5,10,15]
multi=numeros[1]*2#Aqui eu fiz a indexação para identificar o elemento desejado pra multiplicar por 2.
print(multi)
#-------------------------------------------------------------------------------------------
#Exercicio 10:Crie um dicionário com "nome": "Carlos" e altere o valor da chave "nome" para "João". 
alunos={
    "nome":"Carlos",
    "idade":28,
}
# alunos.pop("nome")
# print(alunos)
# alunos.setdefault("nome","João")
# print(alunos)
alunos["nome"]="João"
print(alunos)
#-------------------------------------------------------------------------------------------

