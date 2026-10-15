with open("Exame.txt", "r") as exame:
    linhas = exame.readlines()

    for linha in linhas:
        dados =linha.strip().split("- Media: ")
        nome = dados[0]
        nota = float(dados[1])
        nota_exame = float(input(f"Digite a nota do exame do aluno(a) {nome}: "))

        nova_media = (nota + nota_exame) / 2
        if nova_media > 7:
            with open ("Aprovados.txt","a") as aprovados:
                aprovados.write(f"{nome} - Media: {nova_media:.2f} - Aprovado pos exame\n")
        else:
            with open ("Reprovados.txt","a") as reprovados:
                reprovados.write(f"{nome} - Media: {nova_media:.2f} - Reprovado pos exame\n")