package chapter05;

/**
 * 测试toString方法
 */
public class TestToString {

    public static void main(String[] args) {
        TestToString to = new TestToString();
        System.out.println(to); // 等价于System.out.println(to.toString());
    }

    public String toString() {
        return "测试toString";
    }
}
