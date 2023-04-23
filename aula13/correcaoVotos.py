# votação três candidatos

c1 = 0
c2 = 0
c3 = 0
c4 = 0

while True:
    print("1 - HUGUINHO\n"
          "2 - ZEZINHO\n"
          "3 - LUIZINHO")
    voto = int(input("Voto: "))

    match voto:
        case 0:
            break
        case 1:
            c1 = c1 + 1
        case 2:
            c2 = c2 + 1
        case 3:
            c3 = c3 + 1
        case _:
            c4 = c4 + 1
            print("Voto inválido")

def porcentagem(voto, votosTotal):
    porcentagem = 100 * float(voto)/float(votosTotal)
    porcentagem = round(porcentagem,2)
    return str(porcentagem) + "%"

votosTotal = c1 + c2 + c3 + c4

print(f"""
        1 - Huguinho = {c1} votos, {porcentagem(c1, votosTotal)}
        2 - Zezinho = {c2} votos, {porcentagem(c2, votosTotal)}
        2 - Luizinho = {c3} votos, {porcentagem(c3, votosTotal)}
        2 - Nulo = {c4} votos, {porcentagem(c4, votosTotal)}""")

# Ao final, mostrar a quantidade de votos de cada candidato e
# votos nulos. Tambem mostrar o percentual de cada
# # candidato incluindo os votos nulos
