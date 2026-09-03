def valida_respostas(mensagem, validas):
    resposta = input(mensagem).upper()
    while resposta not in validas:
        print("Resposta inválida!")
        resposta = input(mensagem).upper()
    return resposta

def calcular_quant(perildo,):
    quantidade = []

    indice = 0
    while indice < 3:
        quant = 0
        quant_ganhar = 0
        for resposta in respostas:
            if resposta[1] == perildo:
                quant += 1
                if resposta[0] == elevadores[indice]:
                    quant_ganhar += 1
        quantidade.append(quant_ganhar)

        indice += 1

    return quantidade

def mais_menos(perildo_total,perildo_nome):
    elev=["A","B","C"]

    total = sum(perildo_total)

    if total == 0:
        print(f'Nenhum elevador foi utilizado no perildo {perildo_nome}.')
        print()
        return

    menor = min(perildo_total)
    indice_min = elev[perildo_total.index(menor)]
    if menor == 0:
        menos = 0
    else:
        menos = (menor / total) * 100

    maior = max(perildo_total)
    indice_max = elev[perildo_total.index(maior)]
    if maior == 0:
        mais = 0
    else:
        mais = (maior / total) * 100

    if menor == 0:
        print(f'Os elevadores mais e menos usados no perildo {perildo_nome} são:')
        print(f"Mais usado: {indice_max} com {mais:.0f}% dos usos")
        print(f"Menos usado: {indice_min} com {menos:.0f}% dos usos")
        print(f"diferença de percentual {mais}%")

    elif menor == maior:
        print(f"Os elevadores no perildo {perildo_nome} tiveram a mesma quantidade de uso")

    else:
        print(f'Os elevadores mais e menos usados no perildo {perildo_nome} são:') 
        print(f"Mais usado: {indice_max} com {mais:.0f}% dos usos")
        print(f"Menos usado: {indice_min} com {menos:.0f}% dos usos")
        print(f"diferença de percentual {abs(((maior-menor)/menor)*100)}%")

    print()

coletando = True
respostas = []
elevadores = ["A","B","C"]

while coletando:
    elevador_perg = valida_respostas("Qual o elevador utilizado (A,B,C): ", ["A", "B", "C"])
    perildo_perg = valida_respostas("Em qual perildo o elevador foi utilizado (M,V,N): ", ["M", "V", "N"])

    respostas.append([elevador_perg,perildo_perg])

    coletando = valida_respostas("Deseja continuar (S/N): ", ["S", "N"]) == "S"

matutino = calcular_quant ("M")
vespertino = calcular_quant ("V")
noturno = calcular_quant ("N")

matutino_calculado = mais_menos (matutino,"matutino")
vespertino_calculado = mais_menos (vespertino,"vespertino")
noturno_calculado = mais_menos (noturno,"noturno")

perildo_mais = ""
total_matutino = sum(matutino)
total_vespertino = sum(vespertino)
total_noturno = sum(noturno)

if total_matutino == 0 and total_vespertino == 0 and total_noturno == 0:
    print("Nenhum morador contabilizado")
elif total_matutino == total_vespertino == total_noturno:
    print("Todos os perildos tiveram o mesmo fluxo de moradores")
else:
    if total_matutino > total_vespertino:
        if total_matutino > total_noturno:
            perildo_mais = "matutino"
        else:
            perildo_mais = "noturno"
    elif total_vespertino > total_matutino:
        if total_vespertino > total_noturno:
            perildo_mais = "vespertino"
        else:
            perildo_mais = "noturno"
    print(f"O perildo com o maior fluxo de moradores foi o {perildo_mais}")