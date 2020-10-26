package chapter01;

/**
 * 测试空指针异常
 */
public class TestNullPointerException {
    public static void main(String[] args) {
        String str = null;
        if (str != null) {
            System.out.println(str.length());
        }
    }
}
