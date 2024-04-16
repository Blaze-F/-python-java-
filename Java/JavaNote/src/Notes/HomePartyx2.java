package Notes;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class HomePartyx2 {


    public class Main {
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

            int maxPeople = 0;

            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, 1, 0, -1};

            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (apartment[i][j] == '.') {
                        int perimeter = 0;
                        for (int k = 0; k < 4; k++) {
                            int ni = i + dx[k];
                            int nj = j + dy[k];
                            if (ni >= 0 && ni < R && nj >= 0 && nj < C && apartment[ni][nj] == '.') {
                                perimeter++;
                            }
                        }
                        maxPeople = Math.max(maxPeople, perimeter);
                    }
                }
            }

            System.out.println(maxPeople-1);
        }
    }
}
