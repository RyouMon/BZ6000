import java.util.Date;

/**
 * 测试Data类
 */
public class TestData {
    public static void main(String[] args) {
        Date date1 = new Date();
        System.out.println(date1.toString());
        long i = date1.getTime();
        Date date2 = new Date(i - 1000);
        Date date3 = new Date(i + 1000);
        System.out.println(date1.after(date2));
        System.out.println(date1.before(date2));
        System.out.println(date1.equals(date2));
        System.out.println(date1.after(date3));
        System.out.println(date1.before(date3));
        System.out.println(date1.equals(date3));
        System.out.println(new Date(1000L*60*60*24*365*39L).toString());
    }
}
