
def cadastro_produto() -> dict:

    print("bem vindo ao cadastro de produtos!")
    produto = {}

    produto["id"] = int(input("Digite o id do produto: "))
    produto["nome"] = input("Digite o nome do produto a ser cadastrado: ")
    produto["valor"] = float(input("Digite o valor do produto: "))
    produto["quantidade"] = int(input("Digite a quantidade do produto em estoque: "))
    while True:
        especificacao = input("Digite o tipo de especificação que deseja adicionar ou S para sair: ").lower()
        if especificacao == "s":
            break
        produto[especificacao]  = input("Digite o dado da especificação: ")
    texto_descrivo = input("Caso deseje adicionar um texto descritivo, digite S: ").lower()
    if texto_descrivo == "s":
        produto["descricao"] = input("Digite o texto descritivo: ")
    return produto

def atualizar_cadastro(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            print("Produto encontrado. Atualize as informações:")
            novo_produto = cadastro_produto()
            produto.update(novo_produto)
            print("Cadastro atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def consultar_produto(produtos, id_produto):
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


def listar_produtos(produtos) -> None:
    if len(produtos) == 0:
        print("Não existem produtos cadastrados.")
    else:
        print('-'*5 + "Produtos cadastrados: " + '-'*5)
        for item in produtos:
            print(f"id: {item['id']}, Nome: {item['nome']}")
            
                  
def excluir_cadastro(produtos, id_produto):
    count = 0
    for id in produtos:
        if id["id"] == id_produto:
            produtos.remove(id)
            count = 1
    if count == 1:
        print('Produto excluído com sucesso')
        return produtos
    else:
        print('Produto não localizado.')
        return produtos
                
def main():

    produtos = []
    while True:
        print("""Menu principal: 
            1 - Cadastro produto
            2 - Consultar produto
            3 - Listar produtos
            4 - Atualizar produtos
            5 - Excluir cadastro
            6 - Sair""")
        escolha = int(input("Escolha uma das opções acima: "))

        match escolha:
            case 1:
                produtos.append(cadastro_produto())
            case 2:               
                id_produto_consulta = int(input("Digite o ID do produto que deseja consultar: "))
                consultar_produto(produtos, id_produto_consulta)
            case 3:
                listar_produtos(produtos=produtos)
            case 4:
                id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
                atualizar_cadastro(produtos, id_produto)               
            case 5:
                while True:
                    id_produto = input("Digite o ID do produto que deseja atualizar: ")
                    if id_produto.isdigit():
                        id_produto = int(id_produto)
                        excluir_cadastro(produtos,id_produto)
                        break
                    else:
                        print('Erro de digitação, favor digite novamente.')
            case 6:
                break


main()