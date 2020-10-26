package chapter02;

/**
 * 测试逻辑运算符
 */
public class TestOperator04 {
    public static void main(String[] args) {
        boolean b1 = true;
        boolean b2 = false;
        System.out.println(b1&b2); // false
        System.out.println(b1|b2); // true
        System.out.println(b1^b2); // true
        System.out.println(!b1); // false

        // 测试短路逻辑
        /* int c = 3/0;
           by zero 异常
         */
        boolean b3 = 1>2&&2<(3/0); // 发生短路，不会引发报错。
        System.out.println(b3); // false
    }
}
