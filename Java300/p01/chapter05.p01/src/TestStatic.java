/**
 * 测试static关键字
 */
public class TestStatic {
    public static void main(String[] args) {
        User user = new User(123, "梁闻");
        user.printName(); // 梁闻
        User.printCompany(); // 尚学堂
    }
}

class User{
    int id;
    String name;
    String pwd;
    static String company = "尚学堂";

    User(int id, String name){
        this.id = id;
        this.name = name;
    }

    void printName(){
        System.out.println(this.name);
    }

    static void printCompany(){
        System.out.println(company);
    }
}