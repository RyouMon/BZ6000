import java.io.File;
import java.io.IOException;

/**
 * File类的综合应用
 */
public class TestFile4 {
    public static void main(String[] args) {
        // 指定一个文件
        File file = new File("doc/testC.txt");
        // 判断文件是否存在
        boolean flag = file.exists();
        // 如果存在就删除，如果不存在就创建
        if(flag){
            // 删除
            flag = file.delete();
            if (flag) {
                System.out.println("删除成功");
            } else {
                System.out.println("删除失败");
            }
        } else {
            flag = true;
            try {
                // 如果目录不存在，先创建目录
                File dir = file.getParentFile();
                dir.mkdirs();
                // 创建文件
                flag = file.createNewFile();
                System.out.println("创建成功");
            } catch (IOException e) {
                System.out.println("创建失败");
                e.printStackTrace();
            }
        }

    }

}
