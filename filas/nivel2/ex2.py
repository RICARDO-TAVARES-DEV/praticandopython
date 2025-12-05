#Crie uma função que remove o primeiro elemento da fila. 
frutas=["abacate","amora","ameixa","abacaxi"]#criamos uma lista ou fila de frutas

def retira(fruta):#definimos a função retira e nome do parametro fruta
    frutas.pop(fruta)#na fila ou lista chamada de frutas eu uso o pop para retirar algum elemento chamado fruta 
    return frutas
print(retira(0))#aqui retornamos o resultado da função que é a retirada do primeiro elemento.

    