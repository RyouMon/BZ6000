package chapter02;

import java.io.File;
import java.io.IOException;

/**
 * 测试File类
 */
public class TestFile {
    public static void main(String[] args) throws IOException {
        System.out.println(System.getProperty("user.dir"));
        File f1 = new File("doc/testA.txt");
        File f2 = new File("C:\\Users\\l1048\\OneDrive\\Projects\\JavaProjects\\java300\\doc\\testB.txt");
        // 创建文件
        Boolean r1 = f1.createNewFile();
        Boolean r2 = f2.createNewFile();
        System.out.println(r1);
        System.out.println(r2);
    }
}
