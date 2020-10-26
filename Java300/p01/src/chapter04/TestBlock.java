package chapter04;

/**
 * 测试语句块
 */
public class TestBlock {
    public static void main(String[] args) {
        int n;
        int a;
        {
            int k;
            // int n;  // 编译错误；不能重复定义变量n
        } // 变量k的作用域到此为止
    }
}
