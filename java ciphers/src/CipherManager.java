import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class CipherManager {
    static Scanner in = new Scanner(System.in);
    private int id;
    private int cipherAlgorithm;
    private String key;
    private int lastBlockZeros;
    private int elementsType;
    private int groupSize;


    public CipherManager(int id) {
        BufferedReader reader;
        String[] args = new String[6];
        try {
            reader = new BufferedReader(new FileReader("CIPHERS.txt"));
            String line = reader.readLine();
            while (line != null) {
                args = line.split(" ");
                if (Integer.parseInt(args[0]) == id) {
                    break;
                }
                line = reader.readLine();
            }
            reader.close();
            this.id = Integer.parseInt(args[0]);
            this.cipherAlgorithm = Integer.parseInt(args[1]);
            this.key = args[2];
            this.lastBlockZeros = Integer.parseInt(args[3]);
            this.groupSize = Integer.parseInt(args[4]);
            this.elementsType = Integer.parseInt(args[5]);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void createCipher() {
        System.out.println("Введите уникальный ключ шифровки");
        id = in.nextInt();
        System.out.println("""
                Выберите алгоритм, указав нужную цифру:
                1 - Простая перестановка
                2 - Вертикальная перестановка
                3 - Rail Fence
                4 - Множественная перестановка""");
        cipherAlgorithm = in.nextInt();
        in.nextLine();
        System.out.println("Укажите ключ шифрования");
        key = in.nextLine();
        System.out.println("""
                Выберите способ шифрования последнего блока:
                1 - С добавлением нулей
                2 - Без добавления нулей""");
        lastBlockZeros = in.nextInt();
        System.out.println("""
                Выберите тип элементов:
                1 - Символ
                2 - Бит
                3 - Байт""");
        elementsType = in.nextInt();
        System.out.println("Введите размер группы элементов:");
        groupSize = in.nextInt();
        System.out.println(cipherAlgorithm);
        System.out.println(key);
        System.out.println(lastBlockZeros);
        System.out.println(elementsType);
        System.out.println(groupSize);

        try (FileWriter writer = new FileWriter("CIPHERS.txt", true)) {
            // запись всей строки
            String text = id + " " +
                    cipherAlgorithm + " " +
                    key + " " +
                    lastBlockZeros + " " +
                    groupSize + " " +
                    elementsType + "\n";
            writer.write(text);

            writer.flush();
            System.out.println("Шифровка сохранена!");
        } catch (IOException ex) {

            System.out.println(ex.getMessage());
        }
    }

    private void addingZeros(char[] keys, String[] splitedText) {
        int lastBlockIndex = splitedText.length - 1;
        if (splitedText[lastBlockIndex].length() < keys.length * groupSize) {
            StringBuilder newBlock = new StringBuilder(splitedText[lastBlockIndex]);
            newBlock.append("\0".repeat(Math.max(0, keys.length * groupSize - (splitedText[lastBlockIndex].length()))));
            splitedText[lastBlockIndex] = String.valueOf(newBlock);
        }
    }

    private void deleteZeros(StringBuilder newString, int numberOfBlocks, int j, String[] newBlock) {
        String zero = "\0";
        if (lastBlockZeros == 2 && j == numberOfBlocks) {
            StringBuilder editedBlock = new StringBuilder();
            for (String s : newBlock)
                if (!s.contains("\0"))
                    editedBlock.append(s);

            newString.append(new String(editedBlock));
        } else {
            StringBuilder toReturn = new StringBuilder();
            for (String s : newBlock)
                toReturn.append(s);
            newString.append(new String(toReturn));
        }

    }

    public String applyCipherToString(String text) {
        if (elementsType == 2) {// Means we have text consisting of groups of bits. So we have to apply our algorithm to each group of bits
            String[] splitedBits = text.split("(?<=\\G.{" + 8*groupSize + "})");
            groupSize=1;
            StringBuilder toReturn= new StringBuilder();
            for (int i = 0; i < splitedBits.length; i++) {
                if(i+1==splitedBits.length) {
                    groupSize=2;
                    addingZeros(key.toCharArray(), new String[]{splitedBits[i]});
                    groupSize=1;
                }
                splitedBits[i]=applyPermutationToGroups(splitedBits[i]);
                toReturn.append(splitedBits[i]);
            }
            return String.valueOf(toReturn);
        } else
            return applyPermutationToGroups(text);
    }

    private String applyPermutationToGroups(String text) {
        //split our text into key size groups
        StringBuilder newString = new StringBuilder();
        char[] keys = key.toCharArray();
        String[] splitedText = text.split("(?<=\\G.{" + key.length() * groupSize + "})");
        int numberOfBlocks = splitedText.length;

        //zeros adding if needed
        if(elementsType!=2)
            addingZeros(keys, splitedText);
        int j = 0;//for counting last block
        for (String block : splitedText) {
            String[] newBlock = new String[block.length() / groupSize];
            System.out.println(block);
            for (int i = 0; i < block.length() / groupSize; i++)
                newBlock[Integer.parseInt(String.valueOf(keys[i]))] = block.substring(i * groupSize, (i + 1) * groupSize);
            j++;
            //deleting zeros if needed
            if(elementsType!=2)
                deleteZeros(newString, numberOfBlocks, j, newBlock);
            else {
                StringBuilder toResult=new StringBuilder();
                for (int i = 0; i < newBlock.length ; i++) {
                    toResult.append(newBlock[i]);
                }
                newString.append(toResult);
            }
        }
        return newString.toString();
    }
}
