package chapter02;

/**
 * 测试算数运算符
 */
public class TestOperator01 {
    public static void main(String[] args) {
        // 测试二元运算符
        byte a = 1;
        int b = 2;
        long b2 = 3;
        // byte c = a+b; //报错
        // int c2 = a+b2; // 报错
        float f1 = 3.14f;
        float d = b+b2;

        // float d2 = f1+6.2; //报错

        System.out.println(9%5);
        System.out.println(-9%5);
        System.out.println(9%-5);

        /*
        Out
        4
        -4
        4
         */

        // 测试自增和自减
        int A = 3;
        int B = A++; // 先把A赋值给B，再自增。
        System.out.println("A="+A+"\nB="+B);
        /*Out：
        A=4
        B=3
         */
        A = 3;
        B = ++A; // A先自增，再赋值给B。
        System.out.println("A="+A+"\nB="+B);
        /*Out：
        A=4
        B=4
         */
    }
}
