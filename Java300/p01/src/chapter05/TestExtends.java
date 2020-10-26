package chapter05;

/**
 * 测试继承
 */
public class TestExtends {
    public static void main(String[] args) {
        Student s = new Student("Wen", 22, "市场营销");
        s.study();
        s.rest();
    }
}

class Person{
    String name;
    int age;

    public void rest(){
        System.out.println("休息一会");
    }
}

class Student extends Person{
    String major;

    public Student(String name, int age, String major) {
        this.major = major;
    }

    public void study(){
        System.out.println("学习一会");
    }
}
