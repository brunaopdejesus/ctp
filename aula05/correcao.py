teto = False
inss2 = 0

qtdEmprego = int(input("quantidade de empregos: "))

if qtdEmprego > 1:
    # HÁ DOIS EMPREGOS
    sal = float(input("digite o seu salário: "))
    if sal <= 1302:
        inss = sal * 0.07
    elif sal <= 2571.29:
        inss = sal * 0.09
    elif sal <= 3856.94:
        inss = sal * 0.12
    elif sal <= 7507.49:
        inss = sal * 0.14
    else:
        # pago no teto
        teto = True
        inss = 1051.05

    if teto == True:
        # nao cobrar o inss do segundo emprego
        inss2 = 0
        sal2 = float(input("digite o seu salário 2: "))

    else:
        # cobra o inss do segundo emprego
        sal2 = float(input("digite o seu salário 2: "))
        if sal2 <= 1302:
            inss2 = sal2 * 0.07
        elif sal2 <= 2571.29:
            inss2 = sal2 * 0.09
        elif sal2 <= 3856.94:
            inss2 = sal2 * 0.12
        elif sal2 <= 7507.49:
            inss2 = sal2 * 0.14
        else:
            # pago no teto
            inss2 = 1051.05

    # cálculo do salário líquido
    sal_liq = sal + sal2 - inss - inss2

    print(f"""
            salário..........: R$ {sal:8.2f}
            salário 2........: R$ {sal2:8.2f}
            INSS.............: R$ {inss:8.2f}
            INSS 2...........: R$ {inss2:8.2f}
            salário líquido..: R$ {sal_liq:8.2f}""")


else:
    sal = float(input("digite o seu salário: "))
    if sal <= 1302:
        inss = sal * 0.07
    elif sal <= 2571.29:
        inss = sal * 0.09
    elif sal <= 3856.94:
        inss = sal * 0.09
    elif sal <= 7507.49:
        inss = sal * 0.14
    else:
        inss = 1051.05
    ... # calcular de um emprego