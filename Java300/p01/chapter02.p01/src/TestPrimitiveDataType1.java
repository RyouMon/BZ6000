/**
 * 测试整数型
 */
public class TestPrimitiveDataType1 {
    public static void main(String[] args) {
        int a = 15;
        int b = 015; //八进制 0开头
        int c = 0x15; //十六进制 0x开头
        int d = 0b0100; //二进制 0b或0B开头

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);

        byte age = 127;
        short salary = 30000;
        int population = 300000000;
        long globalPopulation = 74000000000L;
    }
}
