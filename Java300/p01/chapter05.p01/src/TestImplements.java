/**
 * 测试接口与实现
 */
public class TestImplements {
    public static void main(String[] args) {
        Voiant voiant = new Angle();
        voiant.fly();
        System.out.println(Voiant.FLY_HIGTH);

        Honest honest = new GoodMan();
        honest.helpOther();
    }
    /*
     * Out：
     * 我是天使，飞起来啦
     * 100
     * 我是好男人，扶老奶奶过马路
     */
}
/*飞行接口*/
interface Voiant {
    int FLY_HIGTH = 100; // 总是 public static final
    void fly(); // 总是 public abstract
}
/*善良接口*/
interface Honest {
    void helpOther();
}
/*Angle类实现飞行接口和善良接口*/
class Angle implements Voiant, Honest {

    @Override
    public void fly() {
        System.out.println("我是天使，飞起来啦");
    }

    @Override
    public void helpOther() {
        System.out.println("我是天使，扶老奶奶过马路");
    }
}

class GoodMan implements Honest {

    @Override
    public void helpOther() {
        System.out.println("我是好男人，扶老奶奶过马路");
    }
}

class BirdMan implements Voiant {

    @Override
    public void fly() {
        System.out.println("我是鸟人，我在飞。");
    }
}




