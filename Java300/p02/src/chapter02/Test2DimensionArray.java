package chapter02;

/**
 * 测试2维数组
 */
public class Test2DimensionArray {
    public static void main(String[] args) {
        // 二维数组的声明
        int[][] a = new int[3][];
        a[0] = new int[2];
        a[1] = new int[3];
        a[2] = new int[4];
        // 二维数组的静态初始化
        int[][] b = {{1, 2}, {1, 2, 3}, {1, 2, 3, 4, 5}};
    }
}
