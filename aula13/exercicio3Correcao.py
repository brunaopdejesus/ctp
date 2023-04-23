
# 3. pedir o multiplicando e exibir no formato de tabuada

# pedir a tabuada
tab = int(input("tabuada: "))

# pedir o multiplicador
m = int(input("multiplicando: "))

# INÍCIO DO LAÇO
for i in range(1, m + 1, 1):
    mult = tab * i
    print(f"{tab} x {i} = {mult}")

