import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
/**
 * 测试DateFormat类和SimpleDateFormat类
 */
public class TestSimpleDateFormat {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat s1 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        SimpleDateFormat s2 = new SimpleDateFormat("yyyy-MM-dd");
        // 将时间对象转换成字符串
        String daytime = s1.format(new Date());
        System.out.println(daytime);
        System.out.println(s2.format(new Date()));
        System.out.println(new SimpleDateFormat("hh:mm:ss").format(new Date()));
        // 将符合指定格式的字符串转换成时间对象，字符串格式需要和指定格式一致。
        String time = "2007-10-7";
        Date date = s2.parse(time);
        System.out.println("date1:" + date);
        time = "2020-1-26 13:06:30";
        date = s1.parse(time);
        System.out.println("date2:" + date);
    }
}
