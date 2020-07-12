import java.lang.Math;
/**
 * 测试 switch多选择语句
 */
public class TestSwitch {
    public static void main(String[] args) {
        char a = 'a';;
        int rand = (int)(26 * Math.random());
        char b = (char)(a + rand);
        System.out.print(b + ": ");
        switch(b){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            System.out.println("元音");
            break;
        case 'y':
        case 'w':
            System.out.println("半元音");
            break;
        default:
            System.out.println("辅音");
        }
    }
}
