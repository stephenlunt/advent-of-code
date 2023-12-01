import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        String s = parse();
    }

    private static String parse() {
        try {
            Scanner in = new Scanner(new File("./day-06/input.txt"));

            String s = in.toString();

            return s;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return new String();
    }
}