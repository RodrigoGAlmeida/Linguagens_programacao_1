peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso/(altura**2)

print(f"O IMC é: {imc}")

if imc < 18.5 :
    print("Abaixo do peso")
elif imc < 24.9 :
    print("Peso saudável")
elif imc < 29.9 :
    print("Sobrepeso")
else: 
    print("Obeso")