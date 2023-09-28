# BRUNA OLEIRA PEDROSO DE JESUS
# RM: 99518

email = input("Digite o e-mail: ")
count = 0

def validar_email(email) -> None:
    primeiraLetra = email[0]
    letraMin = "abcdefghijklmnopqrstuvwxyz"
    letraMai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    caracteres_especiais = "!#$%&'*+-/=?^_`{|}~"
    emailSeparadoStart = email.split('@')[0]
    emailSeparadoEnd = email.split('@')[1]
    pontos = emailSeparadoEnd.count('.')

    if letraMin in primeiraLetra or letraMai in primeiraLetra:
        print("E-mail inválido, digite outro correto!")
    elif caracteres_especiais in emailSeparadoStart:
        print("E-mail inválido, digite outro correto!")
    elif email.count('@') != 1:
        print("E-mail inválido, digite outro correto!")
    elif pontos < 1 or pontos > 2:
        print("E-mail inválido, digite outro correto!")
    elif '@.' in email or '.@' in email:
        print("E-mail inválido, digite outro correto!")
    elif '..' in emailSeparadoStart:
        print("E-mail inválido, digite outro correto!")
    elif emailSeparadoEnd.endswith('.'):
        print("E-mail inválido, digite outro correto!")
    else:
        arq = open("RM99518.txt", "a")
        arq.write(f"\nEmail: {email}")
        print("E-mail gravado com sucesso!")

validar_email(email)

