import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mult(num1, num2):
    return num1 * num2

def som(num1, num2):
    return num1 + num2

def sub (num1, num2):
    return num1 - num2

def div (num1, num2):
    if num2 == 0:
        return "nao e possivel dividir por zero"
    return num1 / num2

rodando = True
while rodando:
    opcoes = ["soma", "subtracao", "multiplicacao", "divisao"]
    print(".soma")
    print(".subtracao")
    print(".multiplicacao")
    print(".divisao")

    escolha = input("digite a opcao desejada:").lower()
    limpar_terminal()
    while escolha not in opcoes:
        print("opcao invalida,tente novamente")
        input("Pressione Enter para continuar...")
        print(".soma")
        print(".subtracao")
        print(".multiplicacao")
        print(".divisao")
        escolha =input("escolha uma das opcoes acima:").lower()
        limpar_terminal()
    
    if escolha == "soma":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        print(f"O resultado da soma é: {som(num1, num2)}")
    
    elif escolha == "subitracao":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        print(f"O resultado da subtracao é: {sub(num1, num2)}")

    elif escolha == "multiplicacao":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        print(f"O resultado da multiplicacao é: {mult(num1, num2)}")

    elif escolha == "divisao":
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        print(f"O resultado da divisao é: {div(num1, num2)}")

    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        rodando =False
    limpar_terminal()
    
