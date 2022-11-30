package Notes;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UseingBufferedReader throws IOException{

    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String input_string = bf.readLine();

    int input_integer = Integer.parseInt(bf.readLine());

    // TODO 왜 Class 단위 Throws 가 VScode 상에선 되지 않는지 알아보기.

}
