import java.util.Scanner;

public class Test {
    int b;
    int a = 1;
    boolean boleano = true;
    boolean boleano2 = false;
    

    public static void main(String[] args) {
        int soma = 1 + 1;
        // boolean boleano = true;
        System.out.println("Hello World!");

        if ((soma == 2) || (soma == 3)) {
            this.boleano = false;
            System.out.println("Soma é igual a 2");
        } else {
            System.out.println("Soma é diferente de 2");
        }

        while (soma < 10 || boleano == true) {
            System.out.println("Soma é menor que 10");
            soma++;
        }

        for (int i = 0; i < 5; i++) {
            System.out.println("Valor de i: " + i);
        }
    }
}

int a = 1;

public class Test{
    int a;
}