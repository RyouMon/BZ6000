/**
 * 测试抽象类
 */
public class TestAbstract {
    public static void main(String[] args) {
        Dog2 d = new Dog2();
        d.shout();
    }
}
// 抽象类
abstract class Animal2{
    abstract public void shout(); // 抽象方法
}

class Dog2 extends Animal2{
    // 子类必须实现父类的抽象方法,否则编译错误。
    public void shout() {
        System.out.println("汪汪汪");
    }
}
