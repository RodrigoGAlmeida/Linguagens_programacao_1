def valida_respostas(mensagem, validas):
    resposta = input(mensagem).upper()
    while resposta not in validas:
        print("Resposta inválida!")
        resposta = input(mensagem).upper()
    return resposta

def calcular_quant(perildo, elevadores):
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
        quantidade.append(quant)

        indice += 1

    return quantidade

def elevador_mais(perildo_total):
    elevador=["A","B","C"]
    mais=(max(perildo_total)/sum(perildo_total)) * 100
    indice_max = elevador[perildo_total.index(max(perildo_total))]
    return mais, indice_max

coletando = True
respostas = []

while coletando:
    elevador_perg = valida_respostas("Qual o elevador utilizado (A,B,C): ", ["A", "B", "C"])
    perildo_perg = valida_respostas("Em qual perildo o elevador foi utilizado (M,V,N): ", ["M", "V", "N"])

    respostas.append([elevador_perg,perildo_perg])

    coletando = valida_respostas("Deseja continuar (S/N): ", ["S", "N"]) == "S"

print(respostas)

matu = calcular_quant ("M", ["A","B","C"])
matu_mais = elevador_mais(matu)
print (matu_mais)