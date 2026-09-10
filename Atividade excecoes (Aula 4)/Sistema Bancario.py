class MinhaExcecao (ValueError):
    pass

try:
    saldo = float(input("Digite o seu saldo: "))
    saque = float(input("Digite o valor do saque: "))

    if saque >= 0 :
        print("Valor do saque invalido")
    elif saque > saldo :
        print("Saldo insuficiente")

except MinhaExcecao as erro:
    print(erro)

else:
    saldo -= saque
    print("Saque realizado com sucesso")
    print(f"Saldo restante: R${saldo :.2f}")

finally:
    print("Operação bancária finalizada!")