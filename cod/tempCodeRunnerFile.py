    sair = 'S'
    while True:
        for produto in produtos:
            if produto["id"] == id_produto:
                print("Produto encontrado. Detalhes do produto:")
                for chave, valor in produto.items():
                    print(f"{chave.capitalize()}: {valor}")

        sair = input('Deseja continuar?(S/N)') 
        if sair.upper() != 'N':
            id_produto = int(input("Digite o ID do produto que deseja consultar: "))            
            continue
        else:
            return 