#Crie uma fila de nomes e imprima o próximo a ser atendido. 
fila=["João","Julio","Jair","José"]#fila inicial
print(fila)#mostrando a fila inicial
proximo=fila.pop(0)#fila.pop(0) sempre remove o primeiro elemento da lista (quem está na frente da fila).
print(fila)#Mostrando a fila depois que o primeiro da fila foi atendido.
print(fila.pop(0))
print(fila)

