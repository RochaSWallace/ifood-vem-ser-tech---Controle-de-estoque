
def cadastro_produto() -> list:

    print("bem vindo ao cadastro de produtos!")
    produto = {}

    produto["id"] = input("Digite o id do produto: ")
    produto["nome"] = input("Digite o nome do produto a ser cadastrado: ")
    produto["valor"] = float("Digite o valor do produto: ")
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
        escolha = int(input("Escolha um das opções acima: "))

        match escolha:
            case 1:
                produtos.append(cadastro_produto())
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
