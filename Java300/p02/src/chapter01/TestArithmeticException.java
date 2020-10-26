package chapter01;

/**
 * 测试算术异常
 */
public class TestArithmeticException {
    public static void main(String[] args) {
        int b=0;
        if (b!=0) {
            System.out.println(1/b);
        }
    }
}
