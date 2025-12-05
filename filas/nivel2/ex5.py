#Crie uma fila e conte quantos elementos tem. 
clientes=["Álvaro","Robson","Maurício","Jonas","José","Ricardo"]#aqui temos uma lista ou fila  de nomes 

def conta():#criamos a função conta e não precisamos definir parametros pois a exigencia é somente verificar qual é a quantidade de elementos dentro da fila 
 return len(clientes)#aqui no retorno teremos o resultado com o len
print(conta())#aqui destacamos o resultado ou seja informamos a quantidade de clientes na fila.

# - Criou a lista `fila` com os nomes dos clientes.  
# - Definiu a função `conta()` sem parâmetros, já que a lista está acessível diretamente.  
# - Usou `len(fila)` para retornar a quantidade de elementos na fila.  
# - Chamou a função com `print(conta())`, exibindo o número de clientes.  
# O raciocínio está certo: o `len()` é exatamente o recurso usado em Python para contar quantos itens existem dentro de uma lista.  
