package Notes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UseingBufferedReader {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String input_string = bf.readLine();

        int input_integer = Integer.parseInt(bf.readLine());

        System.out.println(input_integer);
        System.out.println(input_string);

    }

}
