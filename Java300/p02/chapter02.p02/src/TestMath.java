/**
 * 测试Math类
 */
public class TestMath {
    public static void main(String[] args) {
        // 取整相关操作
        System.out.println(Math.ceil(3.2)); // 4.0
        System.out.println(Math.floor(3.2)); // 3.0
        System.out.println(Math.round(3.2)); // 3
        System.out.println(Math.round(3.8)); // 4
        // 绝对值、开方、a的b次幂等操作
        System.out.println(Math.abs(-45)); // 45
        System.out.println(Math.sqrt(9)); // 3.0
        System.out.println(Math.pow(2, 3)); // 8.0
        System.out.println(Math.pow(2, 4)); // 16.0
        // Math类中常用的常量
        System.out.println(Math.PI); // 3.141592653589793
        System.out.println(Math.E); // 2.718281828459045
        // 随机数
        System.out.println(Math.random());// [0, 1)
    }
}
