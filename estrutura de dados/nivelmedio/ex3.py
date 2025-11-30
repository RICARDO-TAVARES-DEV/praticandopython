#Crie uma lista [10, 20, 30] e multiplique todos os elementos por 2. 
numeros=[10,11,20,21,30,31,40]
pares=[n for n in numeros if n%2==0]#Aqui eu determinei quais são os números pares como já tinha visto no exercicio 2
dobro=[n * 2 for n in pares]#e aqui determinei que os indices pares pra fazer a multiplicação dos indices destacados.
print(dobro)