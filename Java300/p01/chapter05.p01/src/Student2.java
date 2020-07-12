/**
 * 简单的学生类编写
 */
public class Student2 {
    // 属性
    int id;
    String name;
    int age;
    Computer computer;

    // 方法
    void study(){
        System.out.println("我正在学习");
    }

    void play(){
        System.out.println("我在玩游戏，使用"+computer.brand);
    }

    // 程序执行的入口，必须要有
    public static void main(String[] args) {
        Student2 stu = new Student2();
        Computer computer = new Computer();
        computer.brand = "联想";
        stu.computer = computer;
        stu.name = "梁闻";
        stu.play();
    }
}
class Computer{
    String brand;
}
