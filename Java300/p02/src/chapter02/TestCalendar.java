package chapter02;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

/**
 * 测试日期类的使用
 */
public class TestCalendar {
    public static void main(String[] args) {
        // 获取日期的相关属性
        Calendar c1 = new GregorianCalendar(1996, Calendar.DECEMBER, 2, 13, 24, 24);
        int year = c1.get(Calendar.YEAR);
        int month = c1.get(Calendar.MONTH)+1; // 0-11
        int day = c1.get(Calendar.DATE); // 也可以使用DAY_OF_MOUTH
        int weekday = c1.get(Calendar.DAY_OF_WEEK); // 1-7 周日-周六
        System.out.printf("%d年%d月%d日 星期：%d\n", year, month, day, weekday);

        // 设置日期的相关属性
        Calendar c2 = new GregorianCalendar();
        c2.set(Calendar.YEAR, 8012);
        System.out.println(c2.get(Calendar.YEAR));
        // 日期的计算
        Calendar c3 = new GregorianCalendar();
        c3.add(Calendar.YEAR, -100);
        System.out.println(c3.get(Calendar.YEAR));
        // 日期对象和时间对象的转化
        Date d4 = c3.getTime();
        Calendar c4 = new GregorianCalendar();
        c4.setTime(new Date());
    }
}
