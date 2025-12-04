#Crie uma fila e verifique se está vazia antes de remover. 
#Criamos a fila [0, 1, 2, 3, 4].
# Removemos o primeiro elemento com pop(0).
# Verificamos se a lista está vazia com len(fila).
# Repetimos o processo até esvaziar a fila.
fila = [0, 1, 2, 3, 4]
removido=fila.pop(0)
verifica=len(fila)
if verifica==0:
    print(f"Lista está vazia,{fila}")
else:
    print(f"Lista não está vazia ainda temos estes elementos.{fila}")
    
    removido=fila.pop(0)
verifica=len(fila)
if verifica==0:
    print(f"Lista está vazia,{fila}")
else:
    print(f"Lista não está vazia ainda temos estes elementos.{fila}")
    
    removido=fila.pop(0)
verifica=len(fila)
if verifica==0:
    print(f"Lista está vazia,{fila}")
else:
    print(f"Lista não está vazia ainda temos estes elementos.{fila}")
    
    removido=fila.pop(0)
verifica=len(fila)
if verifica==0:
    print(f"Lista está vazia,{fila}")
else:
    print(f"Lista não está vazia ainda temos estes elementos.{fila}")
    
    removido=fila.pop(0)
verifica=len(fila)
if verifica==0:
    print(f"Lista está vazia,{fila}")
else:
    print(f"Lista não está vazia ainda temos estes elementos.{fila}")
