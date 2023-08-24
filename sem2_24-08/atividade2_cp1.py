def preencherDicionario(dicionario: dict(),
                        nome: str,
                        idade: int,
                        email: str,
                        endereco: str,
                        dataNascimento: str) -> str:
    dicionario['nome'] = nome
    dicionario['idade'] = idade
    dicionario['email'] = email
    dicionario['endereco'] = endereco
    dicionario['dataNascimento'] = dataNascimento

    return "Dicionário preenchido com sucesso!"


def exibirDicionario(dicionario: dict()) -> dict():
    return dicionario


def editarDicionario(dicionario: dict(), key: str, newValue: str) -> str:
    if key in dicionario:
        dicionario[key] = newValue
        return "Dicionário editado com sucesso!"
    else:
        return "Insira uma chave que exista no dicionário."

dicionario = {
    'nome': '',
    'idade': '',
    'email': '',
    'endereco': '',
    'dataNascimento': ''
}
print(dicionario)

import os
while True:
    os.system("clear")
    print("""
          0 - SAIR
          1 - Preencher dicionário
          2 - Exibir dicionário
          3 - Editar dicionário
          """)
    item = int(input("Escolha um item: "))

    match item:
        case 0:
            break
        case 1:
            nome = input("Insira o nome: ")
            idade = input("Insira a idade: ")
            email = input("Insira o e-mail: ")
            endereco = input("Insira o endreço: ")
            dataNascimento = input("Insira a data de nascimento: ")
            print(preencherDicionario(dicionario, nome, idade, email, endereco, dataNascimento))
        case 2:
            print(exibirDicionario(dicionario))
        case 3:
            key = input("Insira qual chave deseja alterar: ")
            newValue = input("Insira qual valor deseja inserir: ")
            print(editarDicionario(dicionario, key, newValue))