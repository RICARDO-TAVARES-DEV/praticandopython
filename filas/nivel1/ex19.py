#Crie uma fila de 10 números e imprima apenas os maiores que 5. 
numeros=[0,4,5,6,2,9,3,1,20,11,7]
ordem=sorted(numeros)
print(ordem)
for n in ordem:
    if n>5 and n!=5:
     print(f"Esse número {n} é maior que 5.")
    

    