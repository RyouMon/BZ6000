package chapter05;

/**
 * JavaBean的封装实例
 */
public class TestEncapsulation03 {
    public static void main(String[] args) {
        Preson4 p4 = new Preson4();
        p4.setAge(-20);
        p4.setAge(20);
        System.out.println(p4.getAge());
    }
}

class Preson4{
    // 属性一般使用private修饰
    private String name;
    private int age;
    private boolean man;
    // 为属性提供public修饰的set/get方法
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age>0 && age<100) {
            this.age = age;
        }else {
            System.out.println("请输入合法的年龄。");
        }

    }
    // 注意：Boolean类型的属性get方法是is开头的
    public boolean isMan() {
        return man;
    }

    public void setMan(boolean man) {
        this.man = man;
    }
}

