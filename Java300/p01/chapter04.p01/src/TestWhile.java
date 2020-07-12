/**
 * 测试while循环
 */
public class TestWhile {
    public static void main(String[] args) {
        // 计算 1+2+3...+100的和
        int i = 0;
        int sum = 0;
        while(i<=100){
            sum += i;
            i ++;
        }
        System.out.println("sum="+sum);
    }
}
