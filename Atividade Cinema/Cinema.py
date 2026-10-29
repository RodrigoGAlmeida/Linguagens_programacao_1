coletando = True
submenu = True 
while coletando:

    print("====SISTEMA DE AVALIAÇÃO DO CINEMA====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")
    print()
    menu = input("Digite a opção desejada: ")
    print()

    if menu == "1":
        registrando = True
        while registrando:
            resposta = []
            idade = int(input("Digite a sua idade: "))
            resposta.append(idade)
            
            while submenu:
                       
                print("===AVALIE A SUA EXPERIÊNCIA===")
                print("1. Ótimo")
                print("2. Bom")
                print("3. Regular")
                print("4. Ruim")
                print("5. Péssimo")
                avaliacao = input("Digite a avaliação desejada: ")
                print()

                if avaliacao == "1": 
                    opcao = "Otimo"
                    resposta.append(opcao)
                    submenu = False
                    registrando = False

                elif avaliacao == "2":
                    opcao = "Bom"
                    resposta.append(opcao)
                    submenu = False
                    registrando = False                  
                       
                elif avaliacao == "3":
                    opcao = "Regular"
                    resposta.append(opcao)
                    submenu = False
                    registrando = False                   
                elif avaliacao == "4":
                    opcao = "Ruim"
                    resposta.append(opcao)
                    submenu = False
                    registrando = False
                elif avaliacao == "5":
                    opcao = "Pessimo"
                    resposta.append(opcao)
                    submenu = False
                    registrando = False
                else:
                     print("Opção invalida")
                     print("Tente novamente")
                     print()
        

            resultado = ";".join(map(str, resposta))    
            with open ("avaliacoes.txt", "a") as avaliacoes:
                    avaliacoes.write(f"{resultado}\n")
            submenu = False
                
    elif menu == "2":
         with open ("avaliacoes.txt", "r") as avaliacoes:
              linhas = avaliacoes.readline()
              for linha in avaliacoes:
                   print(linha.strip())

    elif menu == "3":
        total_otimo = 0
        total_bom = 0
        total_regular = 0
        total_ruim = 0
        total_pessimo = 0
        novo = 9999
        novo_avaliacao = ""
        velho = 0
        velho_avaliacao = ""
        total = 0
        with open ("avaliacoes.txt", "r") as avaliacoes:
            for linha in avaliacoes:
                if not linha.strip():
                    continue

                total += 1
                dados = linha.strip().split(";")
                idade = int(dados[0])
                if idade < novo:
                    novo = idade
                    novo_avaliacao = dados[1]
                if idade > velho:
                    velho = idade
                    velho_avaliacao = dados[1]

                if dados[1] == "Otimo":
                    total_otimo += 1
                elif dados[1] == "Bom":
                    total_bom += 1
                elif dados[1] == "Regular":
                     total_regular +=1
                elif dados[1] == "Ruim":
                     total_ruim += 1
                elif dados[1] == "Pessimo":
                     total_pessimo += 1

        print("===ESTATÍSTICAS DAS AVALIAÇÕES===")
        print(f"Total de respondentes: {total}")
        print("Ótimo: ", total_otimo)
        print("Bom: ",total_bom)
        print("Regular: ",total_regular)
        print("Ruim: ",total_ruim)
        print("Péssimo: ",total_pessimo)
        print("Respondente mais velho:")
        print("Idade: ",velho)
        print("Avaliação: ",velho_avaliacao)
        print("Respondente mais novo:")
        print("Idade: ",novo)
        print("Avaliação: ",novo_avaliacao)

        coletando = False

    elif menu == "4":
        coletando = False
    else:
        print("Opção invalida")
        print("Tente novamente")