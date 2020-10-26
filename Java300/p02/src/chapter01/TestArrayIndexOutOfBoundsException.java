package chapter01;

/**
 * 测试数组下标越界异常
 */
public class TestArrayIndexOutOfBoundsException {
    public static void main(String[] args) {
        int[] arr = new int[5];
        int index = 5;
        if (index<arr.length) {
            System.out.println(arr[index]);
        }
    }
}
