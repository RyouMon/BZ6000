package chapter04;

import java.lang.Math;

/**
 * 测试if else if else 多选择结构
 */
public class TestIfElseIfElse {
    public static void main(String[] args) {
        int age = (int)(100 * Math.random());
        System.out.println("年龄是"+age+"岁");
        if (age < 15){
            System.out.println("儿童");
        }else if (age < 25){
            System.out.println("青年");
        }else if (age < 45){
            System.out.println("中年");
        }else if (age < 65){
            System.out.println("中老年");
        }else if (age < 85){
            System.out.println("老年");
        }else{
            System.out.println("老寿星");
        }
    }
}
