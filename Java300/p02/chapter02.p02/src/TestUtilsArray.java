import java.util.Arrays;

/**
 * 测试工具类Arrays
 */
public class TestUtilsArray {
    public static void main(String[] args) {
        int[] s = {4, 5, 2, 6, 1};
        System.out.println(Arrays.toString(s));
        // 对数组进行排序
        Arrays.sort(s);
        System.out.println(Arrays.toString(s));
        System.out.println(Arrays.binarySearch(s, 4));
        // 找不到元素会返回负数
        System.out.println(Arrays.binarySearch(s, 8));
    }
}
