/**
 * 测试关系运算符
 */
public class TestOperator03 {
    public static void main(String[] args) {
        int a = 3;
        System.out.println(a==3);
        System.out.println(a!=3);
        System.out.println(a<5);

        char b1 = 'a';
        char b2 = 'c';
        System.out.println((int)b1); // 强制类型转化
        System.out.println(0+b1); // 输出为int 结果为97
        System.out.println(0+b2); // 输出为int 结果为99
        System.out.println(b1<b2); // 结果为true

    }
}
