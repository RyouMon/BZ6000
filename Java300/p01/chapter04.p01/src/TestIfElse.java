import java.lang.Math;

/**
 * 测试双选择结构
 */
public class TestIfElse {
    public static void main(String[] args) {
        // 随机产生一个【0，4）区间的数值，以此数值为半径计算圆形的面积和周长
        double r = 4 * Math.random();
        double area = Math.PI * Math.pow(r, 2);
        double circle = 2 * Math.PI * r;
        System.out.println("半径为："+r);
        System.out.println("面积为："+area);
        System.out.println("周长为："+circle);

        if(area>=circle){
            System.out.println("面积大于等于周长");
        }else{
            System.out.println("周长大于面积");
        }
    }
}
