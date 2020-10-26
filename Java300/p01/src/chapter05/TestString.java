package chapter05;

/**
 * 测试String类的常用方法
 */
public class TestString {
    public static void main(String[] args) {
        String s1 = "core java";
        String s2 = "Core java";
        System.out.println(s1.equals(s2));
        System.out.println(s1.equalsIgnoreCase(s2));
        System.out.println(s1.charAt(0));
        System.out.println(s1.indexOf("java"));
        System.out.println(s1.substring(0, 3));

    }
}
