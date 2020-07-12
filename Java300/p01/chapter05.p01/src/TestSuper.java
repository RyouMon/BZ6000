/**
 * 测试 super 关键字
 */
public class TestSuper {
    public static void main(String[] args) {
        new ChildClass().f();
    }
}
class FatherClass {
    public int value;

    public void f(){
        value = 199;
        System.out.println("FatherClass.value="+value);
    }
}
class ChildClass extends FatherClass {
    public int value;

    public void f(){
        super.f();
        value = 299;
        System.out.println("ChileClass.value="+value);
        System.out.println(value);
        System.out.println(super.value);
    }
}

/*
Out:
FatherClass.value=199
ChileClass.value=299
299
199
 */