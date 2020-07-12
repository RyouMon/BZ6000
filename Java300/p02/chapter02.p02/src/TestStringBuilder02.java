/**
 * StringBuilder的常用方法
 */
public class TestStringBuilder02 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("abcdefg");
        System.out.println(sb);
        sb.reverse();
        System.out.println(sb);
        sb.append(1);
        System.out.println(sb);
        sb.insert(0, "我");
        System.out.println(sb);
        sb.delete(0, 1);
        System.out.println(sb);
    }
}
