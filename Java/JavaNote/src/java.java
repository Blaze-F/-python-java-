import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class java {
    public static int R = 0;
    public static int C = 0;
    public static char[][] apartment = new char[R][C];
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] dimensions = bf.readLine().split(" ");
        R = Integer.parseInt(dimensions[0]);
        C = Integer.parseInt(dimensions[1]);

        for (int i = 0; i < R; i++) {
            String line = bf.readLine();
            for (int j = 0; j < C; j++) {
                apartment[i][j] = line.charAt(j);
            }
        }
        //세팅
        int maxPeople = 0;

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        System.out.println(maxPeople);
    }
    public int get_width_to_rightside(int x, int y) {
        for (int j = 0; j < C; j++) {
        if(apartment[x][j] == 'X') {
            j--;
            break;
            }
            return j - y + 1;
        }
        return x;
    }
    public int set_width_to_rightside() {
        int width = 0;
        for (int i = 0; i < R; i++) {
            int j = 0;
            while (j<C) {
                if(apartment[i][j] == '.') {
                    width =
                }
            }
        }
        return
    }


}
// 한 점에 대한 가로방향 길이 2차원 배열
//메서드 분리 이전
//        int[][] prefix_sum = new int[R][C];
//
//        for (int i = 0; i < R; i++) {
//            int j = 0;
//            while(j<C) {
//                if (apartment[i][j] == '.') {
//                    int width = 0;
//
//                    // 한 점에 대한 가로방향 길이 구하기
//                    for (int k = j; k < C; k++) {
//                        if (apartment[i][k] == 'x') {
//                            j -= 1;
//                            break;
//                        }
//                        width = k - j + 1;
//                    }
//
//                    while (width >0 ) {
//                        prefix_sum[i][j] = width;
//
//                        width --;
//
//                    }
//
//            } else {
//                    j ++;
//                }
//
//            }
//        }
// 특정 좌표에서의 오른쪽 길이배열 prefix_sum 을 통해 최대인원 계산

//        for (int i = 0; i < R; i++) {
//            for (int j = 0; j < C; j++) {
//                // 해당 한 점을 집음
//                if (apartment[i][j] == '.') {
//
//                    }
//                    maxPeople = (Math.max(maxPeople, perimeter) - 1) ;
//                }
//            }
//        }