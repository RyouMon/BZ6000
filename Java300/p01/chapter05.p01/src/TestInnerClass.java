/**
 * 测试内部类
 */
public class TestInnerClass {
    public static void main(String[] args) {
        Outer.Inner inner = new Outer().new Inner(); // 创建内部类
        inner.show();
        /* Out:外部类的成员变量age：10 */
    }
}
/* 外部类Outer */
class Outer {
    private int age = 10;
    public void show() {
        System.out.println(age);
    }
    /* 内部类Inner */
    public class Inner {
        public void show() {
            // 访问外部类属性
            System.out.println("外部类的成员变量age："+Outer.this.age);
        }
    }
}