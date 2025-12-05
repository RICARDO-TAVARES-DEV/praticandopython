#Crie uma função que adiciona um elemento à fila. 
numeros = [0, 1, 2, 3, 4]#aqui eu criei a fila chamada numeros.

def aumenta(numero):#definimos o nome da função que é aumenta e informamamos o nome do parametro,que nesse caso é numero e nao podemos colocar o numero direto
    numeros.append(numero)#com o append vamos adicionar o elemento numero na fila
    return numeros#aqui ele retorna a fila cujo nome é numeros sem adiconar nada

print(aumenta(5))#com o print chamamos a função aumenta e entre parenteses adicionamos o número 5 por exemplo.


    