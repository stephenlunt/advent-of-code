import java.io.*;
import java.util.*;

public class Solution {
    // Store each rucksack string representation in an ArrayList
    private static ArrayList<String> rucksacks = new ArrayList<>();

    public static void main(String[] args) {
        readFile();
        System.out.println(problemOne());
        System.out.println(problemTwo());
    }

    private static void readFile() {
        try {
            Scanner in = new Scanner(new File("./day-03/input.txt"));

            while (in.hasNextLine()) {
                rucksacks.add(in.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
    }

    private static int problemOne() {
        int sum = 0;

        for (String r : rucksacks) {
            int n = r.length() / 2;
            String firstCompartment = r.substring(0, n);
            String secondCompartment = r.substring(n);

            // Checks if a character from the first comparement is in the second
            for (int i = 0; i < firstCompartment.length(); i++) {
                char currentChar = firstCompartment.charAt(i);
                if (secondCompartment.indexOf(currentChar) != -1) {
                    // Adds to the sum the priority of the chars
                    int ascii = currentChar;
                    if (ascii > 96 ) {
                        sum += ascii - 96;
                        break;
                    } else {
                        sum += ascii - 38;
                        break;
                    }
                }
            }
        }

        return sum;
    }

    private static int problemTwo() {
        int n = rucksacks.size();
        int sum = 0;

        for (int i = 0; i < n; i += 3) {
            // Get each rucksacks in sets of three
            String rucksackOne = rucksacks.get(i);
            String rucksackTwo = rucksacks.get(i + 1);
            String rucksackThree = rucksacks.get(i + 2);
            System.out.println(rucksackOne + " " + rucksackTwo + " " + rucksackThree);

            for (int j = 0; j < rucksackOne.length(); j++) {
                char letter = rucksackOne.charAt(j);
                
                // If all 3 rucksacks contain the char, add this to the sum
                if (rucksackTwo.indexOf(letter) != -1 && rucksackThree.indexOf(letter) != -1) {
                    int ascii = letter;
                    if (ascii > 96 ) {
                        sum += ascii - 96;
                        break;
                    } else {
                        sum += ascii - 38;
                        break;
                    }
                }
            }
        }

        return sum;
    }
}