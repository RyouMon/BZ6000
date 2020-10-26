package chapter04;

/**
 * 测试递归
 */
public class TestRecurtion {
    public static void main(String[] args) {
        System.out.println(factorial(10));
    }

    /* 计算n的阶乘*/
    static long factorial(int n) {
        if (n==1) {
            return 1;
        }else {
            return n * factorial(n-1);
        }
    }
}
