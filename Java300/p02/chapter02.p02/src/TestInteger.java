/**
 * 测试int的包装类Integer
 */
public class TestInteger {
    public static void main(String[] args) {
        // 基本类型转换为Integer对象
        Integer int1 = Integer.valueOf(10);
        Integer int2 = 20; // 自动装箱
        // Integer对象转换为int
        int a = int1.intValue();
        int b = int1; // 自动拆箱
        // 字符串转换为Integer对象
        Integer int3 = Integer.parseInt("334");
        Integer int4 = new Integer("2343");
        // 常见int类型相关的常量
        System.out.println("int能表示的最大整数："+Integer.MAX_VALUE);
    }
}
