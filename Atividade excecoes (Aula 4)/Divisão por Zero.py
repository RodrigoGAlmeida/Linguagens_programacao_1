class minhaExecao(Exception):
    pass

try:
    n_1 = int(input("Digite o primeiro número: "))
    n_2 = int(input("Digite o segundo número: ")) 
    if n_1 == 0 or n_2 == 0:
        raise minhaExecao ("Impossivel dividir por 0")
    else:
        divisao = n_1 / n_2 
        print(f"A divisão de {n_1} e {n_2} é: {divisao}")
        
except minhaExecao as erro:
    print(erro)
    
finally:
    print("Operação Encerrada")