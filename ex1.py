num1 = float(input("Digite um numero "))
op = input("Digite um operador [ + - * / ] ").strip()
num2 = float(input("Digite outro numero "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Digitou um valor invalido")

