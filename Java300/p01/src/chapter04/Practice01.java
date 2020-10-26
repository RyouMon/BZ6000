package chapter04;

/**
 * 练习
 * 用while循环分别计算100以内的奇数和及偶数和，并输出
 */
public class Practice01 {
    public static void main(String[] args) {
        int sum1 = 0;
        int sum2 = 0;
        int i = 0;
        while(i<=100){
            if(i%2==0){
                sum1 += i;
            }else{
                sum2 += i;
            }
            i++;
        }
        System.out.println("奇数和为"+sum2);
        System.out.println("偶数和为"+sum1);
    }
}
