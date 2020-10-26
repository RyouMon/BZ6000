package chapter05;

/**
 * 测试封装，default
 */
public class TestEncapsulation02 {
    public static void main(String[] args) {
        Human h = new Human();
        h.age = 18; // 编译错误
    }
}

class Human {
    int age; // private修饰

    void sayAge(){
        System.out.println(age);
    }
}

class Boy extends Human {
    void sayHello(){
        System.out.println(age); // 编译错误
    }
}
