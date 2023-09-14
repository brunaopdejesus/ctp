import os
# ---- preenche mais de um registro
def preenche_registros(t: list, reg: dict) -> None:
    while True:
        x = input("Instagram:")
        if x != '.':
            reg['instagram'] = x
            reg['nome'] = input("Nome: ")
            reg['celular'] = input("Celular: ")
            t.append(reg.copy())
        else:
            break

# ---- pesquisa um registro
def pesquisa(insta: str, t: list) -> bool:
    for i in range(0, len(t), 1):
        if t[i]['instagram'] == insta:
            exibe_registro(t, i)
            return True
    return False

# ---- preenche um registro
def preenche_registro(t: list, reg: dict) -> None:
    print("PREENCHENDO O REGISTRO")
    reg['instagram'] = input("Instagram: ")
    reg['nome'] = input("Nome: ")
    reg['celular'] = input("Celular: ")
    t.append(reg.copy())

# ---- exibe um registro especifico
def exibe_registro(t: list, i: int) -> None:
    print(f"\nREGISTRO.....: {i}")
    print(f"Instagram: {t[i]['instagram']}")
    print(f"Nome: {t[i]['nome']}")
    print(f"celular: {t[i]['celular']}\n")

# ---- exibir todos os registros da tabela
def exibe_tabela(t: list) -> None:
    for indice in range(len(t)):
        exibe_registro(t, indice)


def cadastro_pesquisa(t:list, reg:dict, insta:str) -> None:

    for i in range(0, len(t), 1):
        if t[i]['instagram'] == insta:
            print("Usuário já cadastrado\n")
            break
        else: 
            reg['instagram'] = insta
            reg['nome'] = input("Nome: ")
            reg['celular'] = input("Celular: ")
            t.append(reg.copy())
            print("\nUsuário cadastrado com sucesso!")

 
# ============= PRINCIPAL
tabela = list()
contato = dict()

while True:
    os.system("clear")

    print("""
    0 - SAIR
    1 - CADASTRAR UM CONTATO
    2 - EXIBIR A TABELA (CONTATOS CADASTRADOS)
    3 - PREENCHE REGISTROS
    4 - PESQUISA CONTATO
    5 - CADASTRANDO (PESQUISANDO)
    6 - EDIÇÃO (PESQUISANDO)
    """)
    
    opcao = int(input("Escolha: "))
    match opcao:
        case 0:
            break
        case 1:
            preenche_registro(tabela, contato)
        case 2:
            exibe_tabela(tabela)
        case 3:
            preenche_registros(tabela,contato)
        case 4:
            insta = input("Instagram: ")
            if pesquisa(insta, tabela) == False:
                print("Instagram não cadastrado!")
        case 5:
            insta = input("Instragam: ")
            cadastro_pesquisa(tabela, contato, insta)


    input("\nDigite algo para continuar...")
