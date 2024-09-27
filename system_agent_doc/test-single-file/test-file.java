import java.util.Scanner;

public class RaddoppiaNumero {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inserisci un numero intero: ");
        int numero = scanner.nextInt();

        int risultato = raddoppia(numero);

        System.out.println("Il raddoppio è: " + risultato);

        scanner.close();
    }

    private static int raddoppia(int numero) {
        return numero * 2;
    }
}
