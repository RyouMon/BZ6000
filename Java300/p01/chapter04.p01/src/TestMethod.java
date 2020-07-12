/**
 * 测试方法
 */

public class TestMethod {
    public static void main(String[] args) {
        System.out.println(add(1,2,3));
        printHello();
    }

    static int add(int a, int b, int c){
        return a+b+c;
    }

    static void printHello(){
        System.out.println("Hello！");
    }
}
