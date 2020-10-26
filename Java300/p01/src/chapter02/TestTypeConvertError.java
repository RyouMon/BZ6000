package chapter02;

/**
 * 测试类型转换的常见问题
 */

public class TestTypeConvertError {
    public static void main(String[] args) {
        // 一 溢出问题
        int money = 1000000000; // 10亿
        int years = 20;
        int total = money*years; // 超过int的范围，发生了溢出。
        System.out.println("total="+total); // total=-1474836480
        long total1 = money*years; // 仍会造成溢出，结果会转成int，再转long，但是已经发生了数据丢失。
        System.out.println("total="+total1); // total=-1474836480
        long total2 = (long)money*years; // 先将一个因子变为long类型，整个表达式将使用long来计算，结果不会溢出。
        System.out.println("total="+total2); // total=20000000000

        // 二 命名问题
        int l = 2; // 分不清l还是1
        long a = 23451l; // 建议使用大写L、
        System.out.println(l+1);
    }
}
