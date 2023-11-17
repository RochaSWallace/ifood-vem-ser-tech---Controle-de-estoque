def atualizar_cadastro(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            for key in produto.keys(id):
                print(key)
            return produto

id_produto = int(input("Digite o ID do produto: "))
produto_encontrado = atualizar_cadastro(produto, id_produto)

if produto_encontrado is not None:
        while True:
            print("""Escolha a informação a ser atualizada:
                    1 - Nome
                    2 - Valor
                    3 - Quantidade
                    4 - Descrição
                    5 - Sair""")
            escolha = int(input("Digite o número correspondente à informação que deseja atualizar: "))

            if escolha == 5:
                break
            elif escolha == 1:
                produto_encontrado["nome"] = input("Digite o novo nome do produto: ")
            elif escolha == 2:
                produto_encontrado["valor"] = float(input("Digite o novo valor do produto: "))
            elif escolha == 3:
                produto_encontrado["quantidade"] = int(input("Digite a nova quantidade do produto em estoque: "))
            elif escolha == 4:
                texto_descritivo = input("Digite o novo texto descritivo ou 'S' para manter o mesmo: ").lower()
                if texto_descritivo != "s":
                    produto_encontrado["descricao"] = texto_descritivo
                else:
                    print("Opção inválida. Tente novamente.")

            print("Cadastro atualizado com sucesso!")

        else:
            print("Produto não encontrado.")