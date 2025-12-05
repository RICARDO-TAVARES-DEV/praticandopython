#Crie uma função que mostra o próximo da fila sem remover. 
frutas=["abacate","amora","ameixa","abacaxi"]#criamos uma lista ou fila de frutas

def proximo():#determinamos a função proximo onde eu nao preciso colocar parametro 
    return frutas[0] #aqui eu ja retorno a lista frutas com a indexação
print(proximo())#chamando a função vazia pois o resultado ja esta no retorno.

# A lista frutas funciona como uma fila (estrutura de dados onde o primeiro que entra é o primeiro que sai).
# A função proximo() retorna frutas[0], ou seja, o primeiro elemento da lista.
# O print(proximo()) mostra o próximo da fila sem alterar a lista.