public class TestOperator05 {
    public static void main(String[] args) {
        int a = 3;
        int b = 4;
        System.out.println(a&b); // 0
        System.out.println(a|b); // 7
        System.out.println(a^b); // 7
        System.out.println(~a); // -4

        // 移位
        System.out.println(3<<2); // 12
        System.out.println(12>>1); // 6
    }
}
