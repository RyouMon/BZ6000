package chapter04;

/**
 * 练习
 * 用while循环输出1-1000之间能被5整除的数，且每行输出5个
 */
public class Practice02 {
    public static void main(String[] args) {
        int i = 1;
        while (i<=1000){
            if (i%5==0){
                System.out.print(i+"\t");
            }
            i++;
            if (i%25==0){
                System.out.println();
            }
        }
    }
}
