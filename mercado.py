from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: list[Produto] = []
carrinho: list[Dict[Produto, int]] = []

def main() -> None:
    menu()
    
def menu() -> None:
    print('#####################################################')
    print('#####################  BEM-VINDO (A)   ##################')
    print('#####################  GEEK SHOP   ##################')
    print('#####################################################')
    
    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')
    
    opcao: int = int(input(f'{"\n"}OPÇÃO: '))
    
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre! ')
        sleep(1)
        exit(0)
    else:
        print('Opção inválida! ')
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('###################')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))
    
    produto: Produto = Produto(nome=nome, preco=preco)
    
    produtos.append(produto)
    
    print(f'O produto {produto.nome} foi cadastrado com sucesso!')    
    sleep(2)

    menu()
    
def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('####################')
        for produto in produtos:
            print(produto)
            print('====================')
            sleep(1)  
    else:
        print('Ainda não existem produtos cadastrados!')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho')
        print('---------------------------------------------------------------------')
        print('======================= Produtos disponíveis ==========================')
        for produto in produtos:
            print(produto)
            print('---------------------------------------------------------------------')
            sleep(1)
        codigo: int = input(('Codigo: '))
        codigo = int(codigo)
        produto: Produto = selecionar_produto_por_codigo(codigo=codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho. ')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho. ')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
        print('=====================================================================')

    else:
        print('Ainda não existem produtos para vender. ')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho. ')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        
        print('Produtos do carrinho')
        
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco*dados[1]
                print('==============================')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')        
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho. ')
    sleep(2)
    menu()
        

def selecionar_produto_por_codigo(codigo: int) -> None:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

