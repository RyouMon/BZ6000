package chapter05;

/**
 * 测试多态
 */
public class TestPolymorphic {
    public static void main(String[] args) {
        Animal d = new Dog(); // 向上自动转型
        Dog d2 = (Dog)d; // 向下强制转型
    }

    static void animalCry(Animal a) {
        a.shout();
    }
}

class Animal{
    public void shout() {
        System.out.println("叫了一声");
    }
}

class Dog extends Animal{
    public void shout() {
        System.out.println("汪汪汪");
    }
}

class Cat extends Animal{
    public void shout() {
        System.out.println("喵喵喵");
    }
}

