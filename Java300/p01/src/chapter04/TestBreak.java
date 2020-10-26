package chapter04;

import java.lang.Math;

/**
 * 测试循环语句中的break
 */
public class TestBreak {
    public static void main(String[] args) {
        int total = 0; // 计数器
        System.out.println("Begin");
        while(true){
            total++;
            int i = (int)(100*Math.random());
            // 当i=88时退出循环
            if(i==88){
                break;
            }
        }
        System.out.println("Game over, used "+total+" times");
    }
}
