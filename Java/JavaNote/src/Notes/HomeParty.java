package Notes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HomeParty {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] dimensions = bf.readLine().split(" ");
        int R = Integer.parseInt(dimensions[0]);
        int C = Integer.parseInt(dimensions[1]);
        char[][] apartment = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = bf.readLine();
            for (int j = 0; j < C; j++) {
                apartment[i][j] = line.charAt(j);
            }
        }
        String input_string = bf.readLine();
        int input_integer = Integer.parseInt(bf.readLine());


    }


}
