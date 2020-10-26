package chapter04;

/**
 * 测试do while循环
 */
public class TestDoWhile {
    public static void main(String[] args) {
        // 计算 1+2+3...+100的和
        int i = 0;
        int sum = 0;
        do{
            sum += i;
            i ++;
        }while(i<=100);
        System.out.println("sum="+sum);
    }
}
