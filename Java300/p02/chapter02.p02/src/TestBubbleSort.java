import java.util.Arrays;

/**
 * 冒泡排序及其优化
 */
public class TestBubbleSort {
    public static void main(String[] args) {
        int[] array = {1, 3, 5, 8, 0, 2, 4, 9, 6, 7};
        int temp;
        boolean flag;
        for (int i=0; i<array.length-1; i++) {
            flag = true;
            for (int j=0; j<array.length-1-i; j++) {
                if (array[j]>array[j+1]) {
                    temp = array[j+1];
                    array[j+1] = array[j];
                    array[j] = temp;
                    flag = false;
                }
            }
            if (flag) {
                break;
            }
            System.out.println(Arrays.toString(array));
        }

    }
}
