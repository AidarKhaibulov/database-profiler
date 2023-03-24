import java.util.Scanner;

import static org.junit.Assert.assertEquals;

public class Main {

    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        String text;
        int id;
        CipherManager cm = new CipherManager(3);
        while (true) {
            //cm.createCipher();
            System.out.println("Введите текстовое сообщение");
            //text = in.nextLine();
            text = "aabbccddppqq";
            //text = "00110011001111110011000000101011";
            System.out.println("Введите id желаемой шифровки");
            //id = in.nextInt();
            in.nextLine();
            System.out.println(cm.applyCipherToString(text));
        }

    }

}