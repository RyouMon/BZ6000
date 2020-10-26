package chapter05;

/**
 * 构造方法
 */

class Point{
    double x, y;

    // 构造方法名称和类名必须保持一致
    public Point(double x, double y){
        // super(); // 构造方法的第一句总是super()
        this.x = x; // this表示创建好的对象
        this.y = y;
    }

    // 构造方法的重载
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    public double getDistance(Point p){
        return Math.sqrt((x-p.x)*(x-p.x)+(y-p.y)*(y-p.y));
    }
}

public class TestConstructor {
    public static void main(String[] args) {
        Point p = new Point(3.0, 4.0);
        Point o = new Point(0.0, 0.0);

        System.out.println(p.getDistance(o));
    }
}
