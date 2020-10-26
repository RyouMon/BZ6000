package chapter05;

/**
 * 测试接口
 */
public class TesttInterface implements C{
    public void testa() {
    }
    public void testb() {
    }
    public void testc() {
    }
}

interface A {
    void testa();
}

interface B {
    void testb();
}
// 接口的多继承
interface C extends A, B {
    void testc();
}