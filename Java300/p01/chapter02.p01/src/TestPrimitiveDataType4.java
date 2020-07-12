/**
 * 测试布尔型
 */
public class TestPrimitiveDataType4 {
    public static void main(String[] args) {
        boolean man = true;

        if(man){ // 推荐写法
            System.out.println("男性");
        }

        man = false;

        if(man=true){ // 错误写法
            System.out.println("男性");
        }
    }
}
