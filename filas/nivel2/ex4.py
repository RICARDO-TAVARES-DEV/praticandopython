#Crie uma fila de clientes e simule atendimento de todos. 
fila=["Álvaro","Robson","Maurício","Jonas","José"]#criamos a fila de clientes

def zerou():#criamos a função zerou pra simular o atendimento de todos
    fila.clear()#utilizamos o metodo clear que zera ou limpa ou atende todos os cliente
    return fila#retornamos a fila zerada após a execução do clear.
print(zerou())#aqui eu não preciso colocar nada pois o  resultado já está no return da fila

    # A lista fila representa os clientes aguardando atendimento.

    # A função zerou() usa fila.clear(), que remove todos os elementos da lista.

    # O return fila mostra a lista já vazia.

    # O print(zerou()) confirma que a fila ficou vazia ([]).