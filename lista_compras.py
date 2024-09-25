# lista de compras com inserir, apagar e listar

lista =[]
ctd = 0

# iniciando loop
while True:
    
    # inserir comano que deseja fazer
    comando = input("[a]dicionar [r]emover [e]numerar [s]air ")
    comando = comando.lower()
    
    # adicionar item a lista
    if comando == "a":
        item = input("Nome do item: ")
        lista.append(item)
        print("Adicionado na lista")

    # enumerar itens da lista
    elif comando == "e":
        
            # inserir nome do item para a lista
            item = input("Nome do item: ")
            if len(lista) == 0:
                print("lista vazia")
            else:
                total = input("Mostrar lista completa? [s] [n]")
                # mostra item enumerado isolado
                if total == 'n':
                    for indice, elemento in enumerate(lista):
                        if elemento == item:
                            print(indice, item)
                    
                # mostra todos os itens enumerados
                elif total == 's':
                    for indice, elemento in enumerate(lista):
                            print(indice, elemento)
                else:
                    print("digito errado")          
    
    # remove item
    elif comando == "r":
        try:
            # inserir nome do item para a lista
            item = input("Nome ou índice do item: ")
            
            # remover item pelo nome
            if item in lista:
                lista.remove(item)
                print("Item removido da lista")

            # remover item pelo indice
            elif item.isdigit:      # verifica se é um digito
                indice = int(item)      # transforma em int
                if indice >= 0 and indice < len(lista):
                    lista.remove(lista[indice])
                    print("Item removido da lista")
                else:
                    print("indice inválido")
        except ValueError:
            print("Não existe na lista")
    
    # sair do loop e mostra a lista completa
    elif comando == "s":
        print(lista)
        break
    else:
        print('por favor digite: [a] [r] [e] ou [s]')
        continue