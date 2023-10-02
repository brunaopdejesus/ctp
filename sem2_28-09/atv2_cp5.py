def validar_email(email) -> None:
    primeiraLetra = email[0]
    letraMin = "abcdefghijklmnopqrstuvwxyz"
    letraMai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    caracteres_especiais = "!#$%&'*+-/=?^_`{|}~"
    emailSeparadoStart = email.split('@')[0]
    emailSeparadoEnd = email.split('@')[1]
    pontos = emailSeparadoEnd.count('.')

    if primeiraLetra not in letraMin and primeiraLetra not in letraMai:
        print("E-mail inválido, digite outro correto!\n")
    elif caracteres_especiais in emailSeparadoStart:
        print("E-mail inválido, digite outro correto!\n")
    elif email.count('@') != 1:
        print("E-mail inválido, digite outro correto!\n")
    elif pontos < 1 or pontos > 2:
        print("E-mail inválido, digite outro correto!\n")
    elif '@.' in email or '.@' in email:
        print("E-mail inválido, digite outro correto!\n")
    elif '..' in emailSeparadoEnd:
        print("E-mail inválido, digite outro correto!\n")
    elif emailSeparadoEnd.endswith('.'):
        print("E-mail inválido, digite outro correto!\n")
    else:
        arq = open("RM99518.txt", "a")
        arq.write(f"\nEmail: {email}")
        print("E-mail gravado com sucesso!\n")

while True:
    email = input("\nDigite o e-mail: ")
    validar_email(email)
    continuar = input("Deseja inserir outro e-mail? (S/N): ").strip().lower()
    if continuar != 's':
        break
