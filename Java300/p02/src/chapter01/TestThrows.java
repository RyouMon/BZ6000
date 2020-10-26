package chapter01;

import java.io.FileReader;
import java.io.IOException;

/**
 * 声明异常
 */
public class TestThrows {
    public static void main(String[] args) throws IOException {
        readFile();
    }
    public static void readFile() throws IOException {
        FileReader reader = null;
        reader = new FileReader("doc/testA.txt");
        char c = (char) reader.read();
        System.out.println(c);
        reader.close();
    }
}
