import java.lang.Math;

/**
 * 测试单选择结构
 */
public class TestIf {
    public static void main(String[] args) {
        // 通过掷三个骰子看看今天的手气如何
        int a = (int)(6 * Math.random()) + 1; // 产生随机数
        int b = (int)(6 * Math.random()) + 1;
        int c = (int)(6 * Math.random()) + 1;
        int count = a+b+c;
        if(count>15){
            System.out.println("今天运气不错！");
        }
        if(count>=10 && count<=15){
            System.out.println("今天运气一般。");
        }
        if(count<10){
            System.out.println("今天运气不怎么样。");
        }
        System.out.println("得了"+count+"点");
    }
}
