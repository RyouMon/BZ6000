package chapter02;

import java.util.Arrays;

/**
 * 使用二维数组储存数据
 */
public class TestTableData {
    public static void main(String[] args) {
        Object[] a1 = {1001, "KANA", "159CM", 31};
        Object[] a2 = {1002, "AKI", "162CM", 32};
        Object[] a3 = {1003, "INORI", "153CM", 22};
        Object[][] b = new Object[3][];
        b[0] = a1;
        b[1] = a2;
        b[2] = a3;
        for (Object[] each:b) {
            System.out.println(Arrays.toString(each));
        }
    }
}
