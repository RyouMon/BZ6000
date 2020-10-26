package chapter05;

/**
 * 测试静态初始化块
 */
public class User2 {
    int id;
    String name;
    String pwd;
    static String company;

    static {
        System.out.println("执行类的初始化工作");
        company = "尚学堂";
        printCompany();
    }

    void printName(){
        System.out.println(this.name);
    }

    static void printCompany(){
        System.out.println(company);
    }

    public static void main(String[] args) {
        User2 user2 = null;
    }
}
