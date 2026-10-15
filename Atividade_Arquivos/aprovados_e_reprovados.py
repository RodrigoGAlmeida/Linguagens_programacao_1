with open("Aprovados.txt", "r") as aprovados:
    linhas = aprovados.readlines()

    print()
    print("-" * 20)
    print("Lista de Aprovados")
    print("-" * 20)
    print()

    for linha in linhas:
        print(linha.strip())



with open("Reprovados.txt", "r") as reprovados:
    linhas = reprovados.readlines()
    
    print()
    print("-" * 20)
    print("Lista de Reprovados")
    print("-" * 20)
    print()

    for linha in linhas:
        print(linha.strip())
print()
