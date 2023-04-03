    # Versão com elif
'''
print("""
    1 - Cadastro
    2 - Consulta
    3 - Alteração
    4 - Exclusão
""")
opcao = int(input("Digite a opcao desejada: "))

if opcao == 1:
    print("Efetuando o cadastro")
elif opcao == 2:
    print("Efetuando a consulta")
elif opcao == 3:
    print("Efetuando a Alteração")
elif opcao == 4:
    print("Efetuando a Exclusao")
else:
    print("Opcao invalida, digite uma opcao entre 1 e 4!")
'''
# switch(opcao)
# {
#     case 1:
#         print(a); break;
#     case 2:
#         print(b); break;
#     defaultL
#         print(c); break;
# }
print("""
    1 - Cadastro
    2 - Consulta
    3 - Alteração
    4 - Exclusão
""")

# match case nao compara com sinal de > ou <, só equivalência
# else não funciona, usar match _

opcao = input("Digite a opcao desejada: ")
if opcao.isdigit(): # verifica se é número
    opcao = int(opcao)
    match opcao:
        case 1:
            print("Efetuando o cadastro")
        case 2:
            print("Efetuando a consulta")
        case 3:
            print("Efetuando a Alteração")
        case 4:
            print("Efetuando a Exclusao")
        case _:
            print("Opcao invalida, digite uma opcao entre 1 e 4!")
else:
    print("Digite um número")



