
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")


if operacao == "+":
    resultado = soma(numero1, numero2)
elif operacao == "-":
    resultado = subtracao(numero1, numero2)
elif operacao == "*":
    resultado = multiplicacao(numero1, numero2)
elif operacao == "/":
    resultado = divisao(numero1, numero2)
else:
    resultado = "Erro: operação inválida"

# Imprimindo o resultado da operação
print("Resultado: ", resultado)