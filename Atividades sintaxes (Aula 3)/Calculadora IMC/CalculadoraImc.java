import java.util.Scanner;

public class CalculadoraImc {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o seu peso: ");
        double peso = scanner.nextDouble();

        System.out.print("Digite a sua altura em metros: ");
        double altura = scanner.nextDouble();

        double imc = peso / (altura * altura);

        System.out.println("O IMC é: " + imc);

        if (imc < 18.5) {
            System.out.println("Abaixo do peso");
        } else if (imc < 24.9) {
            System.out.println("Peso saudável");
        } else if (imc < 29.9) {
            System.out.println("Sobrepeso");
        } else {
            System.out.println("Obeso");
        }

        scanner.close();
    }
}
