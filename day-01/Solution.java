import java.io.*;
import java.util.*;

public class Solution {
    private static ArrayList<Integer> totals = new ArrayList<>();

    public static void main(String[] args) {
        try {
            readInputFile();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println("Highest value: " + getHighestCals());
        System.out.println("Top 3: " + getTopThree());
    }

    private static void readInputFile() throws FileNotFoundException {
        Scanner in = new Scanner(new File("./day-01/input.txt"));

        int total = 0;
        while (in.hasNext()) {
            String line = in.nextLine();
            
            if (line.equals("")) {
                totals.add(total);
                total = 0;
            } else {
                total += Integer.parseInt(line);
            }
        }
    }

    private static int getHighestCals() {
        return Collections.max(totals);
    }

    private static int getTopThree() {
        Collections.sort(totals, Collections.reverseOrder());
        
        int topThree = 0;
        for (int i = 0; i < 3; i++) {
            topThree += totals.get(i);
        }
        return topThree;
    }
}