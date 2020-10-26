package chapter04;

/**
 * 测试重载
 */
public class TestOverLoad {
    public static void main(String[] args) {
        System.out.println(add(1, 2)); // 3
        System.out.println(add(1, 2, 3)); // 6
        System.out.println(add(1.0, 2)); // 3.0
        System.out.println(add(1, 2.0)); // 3.0
        // 方法的重载
        System.out.println(); // 零个参数
        System.out.println(1); // 参数时一个int
        System.out.println(3.0); // 参数是一个double
    }

    /* 求和的方法 */
    public static int add(int n1, int n2) {
        return n1 + n2;
    }
    // 方法名称相同，参数个数不同，构成重载
    public static int add(int n1, int n2, int n3) {
        return n1 + n2 + n3;
    }
    // 方法名称相同，参数类型不同，构成重载
    public static double add(double n1, int n2) {
        return n1 + n2;
    }
    // 方法名称相同，参数顺序不同，构成重载
    public static double add(int n1, double n2) {
        return n1 + n2;
    }
    // 编译错误，只有返回值不同不构成重载
    /*
    public static double add(int n1, int n2) {
        return n1 + n2;
    }
    */
    // 编译错误，只有参数名不同不构成重载
    /*
    public static int add(int n2, int n1) {
        return n1 + n2;
    }
    */
}
