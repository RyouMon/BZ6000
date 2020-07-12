/**
 * 测试参数传递机制
 */
public class User3 {
    int id;
    String name;
    String pwd;

    public User3(int id, String name){
        this.id = id;
        this.name = name;
    }

    public void testParameterTranfer01(User3 u){
        // u1的地址传递给u，u与u1指向同一个对象
        u.name = "高小八";
    }

    public void testParameterTranfer02(User3 u){
        // u的地址与u1的地址不一样，u的改变不会影响u1指向的对象
        u = new User3(200, "高三");
    }

    public static void main(String[] args) {
        User3 u1 = new User3(100, "高小七");

        u1.testParameterTranfer01(u1);
        System.out.println(u1.name); // 高小八

        u1.testParameterTranfer02(u1);
        System.out.println(u1.name); // 高小八
    }

}
