/**
 * 测试类型转换异常
 */
class Animal{

}
class Dog extends Animal{

}
class Cat extends Animal{

}
public class TestClassCastException {
    public static void main(String[] args) {
        Animal dog = new Dog();
        if (dog instanceof Cat) {
            Cat cat = (Cat)dog;
        }
    }
}
