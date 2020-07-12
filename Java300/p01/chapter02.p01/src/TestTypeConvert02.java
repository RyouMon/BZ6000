/**
 * 测试强制类型转化
 */
public class TestTypeConvert02 {
    public static void main(String[] args) {
        double x = 3.14;
        int nx = (int)x;
        char c = 'a';
        int d = c+1;
        System.out.println(nx); // 3
        System.out.println(d); // 98
        System.out.println((char)d); //b
    }
}
