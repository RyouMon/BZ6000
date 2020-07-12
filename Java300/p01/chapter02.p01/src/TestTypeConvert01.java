/**
 * 测试自动类型转化
 */
public class TestTypeConvert01 {
    public static void main(String[] args) {
        int a = 234;
        long b = a;
        double d = b;

        // a = b; long不能自动转化为int类型
        // long e = 3.23F; float不能自动转化为long类型
        float f = 234234L;

        // 特例，不超过表数范围即可
        byte b2 = 123;
    }
}

