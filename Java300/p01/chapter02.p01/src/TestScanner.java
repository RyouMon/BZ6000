import java.util.Scanner;

/**
 * 测试Scanner对象
 */

public class TestScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入你的名字");
        String name = scanner.nextLine();
        System.out.println("请输入你的性别");
        String sex = scanner.nextLine();
        System.out.println("请输入你的年龄");
        int age = scanner.nextInt();

        System.out.println("###############");
        System.out.println(name);
        System.out.println(sex);
        System.out.println(age);

    }
}
