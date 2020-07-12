public class TestArray01 {
    public static void main(String[] args) {
        // 1、静态初始化
        int[] arr01 = {1, 2, 3}; // 静态初始化基本类型数组
        User[] arr02 = {new User("Wen"), new User("Hana")}; // 静态初始化引用类型数组
        // 2、动态初始化
        int[] arr03 = new int[2]; // 动态初始化数组，先分配空间
        arr03[0] = 1; // 给数组元素赋值
        arr03[1] = 2; // 给数组元素赋值
        // 3、默认初始化
        int[] arr4 = new int[2]; // 默认值：0，0
        boolean[] arr5 = new boolean[2]; // 默认值：false，false
        String[] arr6 = new String[2]; // 默认值：null，null

        // 数组的遍历
        int[] arr = {1, 2, 3, 4, 5, 6};
        for(int each: arr) {
            System.out.println(each);
        }
    }
}

class User{
    private String name;

    public User(String name) {
        this.name = name;
    }
}
