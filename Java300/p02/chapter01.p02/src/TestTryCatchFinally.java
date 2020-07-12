import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * 测试Try-Catch-Finally语句
 * 捕获异常
 */
public class TestTryCatchFinally {
    public static void main(String[] args) {
        FileReader reader = null;
        try {
            reader = new FileReader("doc/testA.txt");
            char c = (char) reader.read();
            System.out.println(c);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }
}
