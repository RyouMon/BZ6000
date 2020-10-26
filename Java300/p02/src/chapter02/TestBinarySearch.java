package chapter02;

import java.util.Arrays;

/**
 * 二分法查找
 */
public class TestBinarySearch {
    public static void main(String[] args) {
        int[] arr = {30,20,50,10,80,9,7,12,100,40,8};
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
        System.out.println(myBinarySearch(arr, 6));
    }
    public static int myBinarySearch(int[] array, int key) {

        int start = 0;
        int end = array.length-1;
        while (start <= end) {
            int mid = (end+start)/2;
            if (array[mid] == key){
                return mid;
            }
            if (array[mid] < key) {
                start = mid+1;
            }
            if (array[mid] > key) {
                end = mid-1;
            }
        }
        return -1;
    }
}
