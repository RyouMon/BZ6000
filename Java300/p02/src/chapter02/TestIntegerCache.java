package chapter02;

/**
 * 测试包装类的缓存问题
 */
public class TestIntegerCache {
    public static void main(String[] args) {
        Integer int1 = 127;
        Integer int2 = 127;
        System.out.println(int1==int2); // true
        System.out.println(int1.equals(int2)); // true
        Integer int3 = 1000;
        Integer int4 = 1000;
        System.out.println(int3==int4); // false
        System.out.println(int3.equals(int4)); // true
    }

}
