package chapter02;

/**
 * 测试可变字符序列StringBuilder和StringBuffer
 */
public class TestStringBuilder {
    public static void main(String[] args) {
        // StringBuilder线程不安全，效率高（一般用它），StringBuffer线程安全，效率低
        StringBuilder sb = new StringBuilder("abcdefg");

        System.out.println(Integer.toHexString(sb.hashCode()));
        System.out.println(sb);

        sb.setCharAt(2, 'M');
        System.out.println(Integer.toHexString(sb.hashCode()));
        System.out.println(sb);
    }
}
