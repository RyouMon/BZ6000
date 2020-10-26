package chapter04;

/**
 * 测试for循环
 */

public class TestFor {
    public static void main(String[] args) {
        // 计算 1+2+3...+100的和
        int sum = 0;
        for(int i=0; i<=100; i++){
            sum += i;
        }
        System.out.println("sum="+sum); // sum-5050
    }
}
