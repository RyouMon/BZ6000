package chapter02;

import java.io.File;
import java.io.IOException;

/**
 * 测试File类
 */
public class TestFile3 {
    public static void main(String[] args) throws IOException {
        File f = new File("doc/testC.txt");
        f.createNewFile();
        f.delete();
        File f2 = new File("test/testFile/testFile2");
        boolean r = f2.mkdir();
        System.out.println(r);
        r = f2.mkdirs();
        System.out.println(r);
        File f3 = new File("test");
        r = f3.delete();
        System.out.println(r);
    }

}
