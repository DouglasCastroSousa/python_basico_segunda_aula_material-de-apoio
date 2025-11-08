nota = float(input("Digite a sua nota: "))


if nota < 0:
    print("essa nota não existe")
elif nota >= 0 and nota < 5:
    print("Reprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
elif nota >= 7 and nota <= 10:
    print("Aprovado")
else:
    print("A nota é maior do que 10")