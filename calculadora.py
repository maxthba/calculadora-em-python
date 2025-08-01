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
    print("digite 1 para soma")
    print("digite 2 para subitracao")
    print("digite 3 para multiplicacao")
    print("digite 4 para divisao")

    escolha = input("digite a opcao desejada:")
limpar_terminal()

