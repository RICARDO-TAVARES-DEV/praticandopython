#Remova o primeiro elemento da fila. 
fila=["A","B"]
fila.remove("A")#aqui eu utilizei o remove mas ele funcionou pois eu especifiquei o elemento e não a posição do elemento solicitada que nesse caso é 0 ou a primeira posição se eu tivesse que remover o elemento da posição 2500. ficaria inviável.
print(fila)

fila=["A","B"]
fila.pop(0)#aqui eu já determinei que eu queria remover o elemento da primeira posição ou seja indice ou posição zero(0)
print(fila)


