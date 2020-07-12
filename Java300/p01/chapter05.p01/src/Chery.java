public class Chery implements ICar{
    @Override
    public void accelerate() {
        System.out.print("加速慢，像蜗牛一样");
    }

    @Override
    public void brake() {
        System.out.print("跑的慢，很快就停下来了");
    }
}
