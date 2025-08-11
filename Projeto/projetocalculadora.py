def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("Calculadora Simples")
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Digite o número da operação desejada (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = somar(num1, num2)
    print("Resultado:", resultado)
elif opcao == "2":
    resultado = subtrair(num1, num2)
    print("Resultado:", resultado)
elif opcao == "3":
    resultado = multiplicar(num1, num2)
    print("Resultado:", resultado)
elif opcao == "4":
    resultado = dividir(num1, num2)
    print("Resultado:", resultado)
else:
    print("Opção inválida!")