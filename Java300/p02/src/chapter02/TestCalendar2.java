package chapter02;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

/**
 * 可视化日历
 */
public class TestCalendar2 {
    public static void main(String[] args) throws ParseException {
        System.out.println("请输入日期（格式为：2010-3-3）");
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        System.out.println("您刚刚输入对的日期是：" + str);
        // 将字符串转换为Date对象，然后传入Calendar
        DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
        Date date = df.parse(str);
        Calendar c = new GregorianCalendar();
        c.setTime(date);
        int day = c.get(Calendar.DAY_OF_MONTH);
        int maxDay = c.getActualMaximum(Calendar.DAY_OF_MONTH);
        System.out.println("日\t一\t二\t三\t四\t五\t六");

        c.set(Calendar.DAY_OF_MONTH, 1);
        for (int j=1; j<c.get(Calendar.DAY_OF_WEEK); j++) {
            System.out.print("\t");
        }
        for (int i=1; i<=maxDay; i++) {
            // 打印日期
            if (i == day) {
                System.out.print(i+"*\t");
            } else {
                System.out.print(i+"\t");
            }
            // 如果当天是星期六，进行换行
            if (c.get(Calendar.DAY_OF_WEEK) == Calendar.SATURDAY) {
                System.out.println();
            }
            c.add(Calendar.DAY_OF_MONTH, 1);
        }
    }
}
