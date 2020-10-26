package chapter02;

import java.math.*;
/**
 * 测试浮点型
 */

public class TestPrimitiveDataType2 {
    public static void main(String[] args) {
        float a = 3.14F;
        double b = 6.28;
        double c = 628E-2;

        System.out.println(c);

        // 浮点数是不精确的，存在舍入误差，一定不要用于比较。
        float f = 0.1F;
        double d = 1.0/10;
        System.out.println(f==d); // 结果总为False

        float d1 = 423432423F;
        float d2 = d1 + 1;
        if(d1==d2){
            System.out.println("d1==d2"); // 输出结果为 d1==d2
        }else{
            System.out.println("d1!=d2");
        }

        System.out.println("##############");
        // 若想精确比较，使用java.math包中的BigInteger和BigDecimal对象
        BigDecimal bd = BigDecimal.valueOf(1.0);
        bd = bd.subtract(BigDecimal.valueOf(0.1));
        bd = bd.subtract(BigDecimal.valueOf(0.1));
        bd = bd.subtract(BigDecimal.valueOf(0.1));
        bd = bd.subtract(BigDecimal.valueOf(0.1));
        bd = bd.subtract(BigDecimal.valueOf(0.1));
        System.out.println(bd); // 0.5
        System.out.println(1.0-0.1-0.1-0.1-0.1-0.1); // 0.5000000000000001

        BigDecimal bd2 = BigDecimal.valueOf(0.1);
        BigDecimal bd3 = BigDecimal.valueOf(1.0/10);
        System.out.println(bd2.equals(bd3)); // True
        }
    }

