package chapter02;

/**
 * 测试枚举类型
 */
public class TestEnum {
    public static void main(String[] args) {
        Season season = Season.Spring;
        System.out.print(Season.Spring);
        switch (season) {
            case Spring:
                System.out.println("春天");
                break;
            case Sumner:
                System.out.println("夏天");
                break;
            case Autumn:
                System.out.println("秋天");
                break;
            case Winter:
                System.out.println("冬天");
                break;
        }
    }
}

enum Season {
    Spring, Sumner, Autumn, Winter
}
