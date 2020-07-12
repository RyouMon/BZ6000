import java.io.File;

/**
 * 递归打印文件目录
 */
public class PrintFileTree {
    public static void main(String[] args) {
        printFile(new File("G:/Anime"), 0);
    }

    public static void printFile(File file, int level) {
        for (int i = 0; i < level; i++) {
            System.out.print("-");
        }
        System.out.println(file.getName());
        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (File eachFile:files) {
                printFile(eachFile, level+1);
            }
        }
    }
}
