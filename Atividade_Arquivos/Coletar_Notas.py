coletando = True

while coletando:
    resposta = []

    
    nome = input("Digite o nome do Aluno: ")
    resposta.append(nome)

    for i in range (3):
        nota = float(input(f"Digite a {i+1}ª nota: " ))
        resposta.append(nota)

    resultado = ",".join(map(str, resposta))    

    with open("Notas.txt", "a") as notas:
        notas.write(f"{resultado}\n")
    print(resultado) 

    continuar = input("Deseja adicionar outro aluno (S/N): ").upper()
    validas = ["S","N"]
    while continuar not in validas:
        print("Resposta inválida!")
        continuar = input("Deseja adicionar outro aluno (S/N): ").upper()

    if continuar == "S":
        coletando = True
    elif continuar == "N":
        coletando = False
