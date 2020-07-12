import java.io.File;

/**
 * 测试File类
 */
public class TestFile2 {
    public static void main(String[] args) {
        File f = new File("doc/testA.txt");
        System.out.println("文件是否存在" + f.exists());
        System.out.println("File是否是目录" + f.isDirectory());
        System.out.println("File是否是文件" + f.isFile());
        System.out.println("File最后修改时间" + f.lastModified());
        System.out.println("File的大小" + f.length());
        System.out.println("File的文件名" + f.getName());
        System.out.println("File的相对目录路径" + f.getPath());
        System.out.println("File的绝对目录路径" + f.getAbsolutePath());

    }
}
