public class Ford implements ICar{
    @Override
    public void accelerate() {
        System.out.print("加速太快了，冲冲冲");
    }

    @Override
    public void brake() {
        System.out.print("刹车性能好，很快就停了");
    }
}
