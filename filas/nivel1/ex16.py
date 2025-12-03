#Crie uma fila e verifique se está vazia antes de remover. 
fila = [0, 1, 2, 3, 4]

while fila:   # enquanto a lista não estiver vazia
    removido = fila.pop(0)   # remove o primeiro elemento
    print("Removido:", removido)

print("Fila vazia!")
