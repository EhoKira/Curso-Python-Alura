import os

restaurantes = [{"nome": "Pizzelle", "categoria": "Pizza Frita", "ativo": False}, 
                {"nome": "Forneto", "categoria": "Pizzaria", "ativo": True},
                {"nome": "Saladaria", "categoria": "Açaí", "ativo": False},
                {"nome": "Cabra's Burger", "categoria": "Hamburgueria", "ativo": True}]
                
def exibir_nome_do_programa():
    """  """
    print("""
    ██╗░░██╗██╗██████╗░░█████╗░██╗░██████╗
    ██║░██╔╝██║██╔══██╗██╔══██╗╚█║██╔════╝
    █████═╝░██║██████╔╝███████║░╚╝╚█████╗░
    ██╔═██╗░██║██╔══██╗██╔══██║░░░░╚═══██╗
    ██║░╚██╗██║██║░░██║██║░░██║░░░██████╔╝
    ╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═════╝░

    ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Encerrando o app")
    
def voltar_menu():
    try:
        voltar = input("\nDigite Y ou N para voltar ao menu principal: ")
        if voltar == "y":
            main()
        elif voltar == "n":
            print("Saiu!")
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "-" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
  
def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu()

def cadastrar_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante 
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    """

    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    print(f"O Restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu()

def listar_restaurantes():
    """ Essa função é responsável por listar os restaurantes 
    Outputs:
    - Nome dos restaurante
    - Categoria
    - Status
    """

    exibir_subtitulo("Listando os restaurantes")

    print(f"{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | {"Status"}")

    for i, restaurante in enumerate(restaurantes, 1):
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"{i}. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_menu()

def alternar_estado_restaurante():
    exibir_subtitulo("Altenar estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso." if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso."
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    
    voltar_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
    
