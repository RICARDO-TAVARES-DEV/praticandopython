#Crie uma fila e remova todos os elementos usando while. 
fila = ["amora","ameixa","abacate","abacaxi","cacau","banana","caqui","damasco","morango"]

while fila: # enquanto a lista não estiver vazia
    removido = fila.pop(0)   # removeremos o primeiro elemento a cada rodada.
    print("Removido:", removido)

print("Fila vazia!")
