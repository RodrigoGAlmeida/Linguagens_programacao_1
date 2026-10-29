with open("Notas.txt", "r") as notas:
    linhas = notas.readlines()

   

    for linha in linhas:
        nota = []
        dados = linha.split(",")
        nome = dados[0]
        for j in dados[1:]:
            
            if dados.index == 0:
                nome = j
            else:
                numero = float(j)
                nota.append(numero)

        media = sum(nota)/3
        if media >= 7:
            with open("Aprovados.txt","a") as aprovados:
                aprovados.write(f"{nome} - Media: {media:.2f}\n")
        elif media>= 5:
             with open("Exame.txt","a") as exame:
                exame.write(f"{nome} - Media: {media:.2f}\n")       
        else:
             with open("Reprovados.txt","a") as reprovados:
                reprovados.write(f"{nome} - Media: {media:.2f}\n")
      