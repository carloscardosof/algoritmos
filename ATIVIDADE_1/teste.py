nota1 = 8.0
nota2 = 5.5
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3

if media >= 7 and nota1 >= 6 and nota2 >= 6 and nota3 >= 6:
    print("Aprovado sem restrições")
elif media >= 7:
    print("Aprovado com restrição em uma nota")
elif media >= 6:
    if nota1 < 6 or nota2 < 6 or nota3 < 6:
        print("Recuperação por nota baixa")
    else:
        print("Recuperação pela média")
else:
    print("Reprovado")