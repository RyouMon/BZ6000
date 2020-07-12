/**
 * 玩家，对应DIP中的高层模块
 */
public class Player {
    /**
     * 开福特
     * 不好的依赖，高层模块依赖了低层模块
     * Player直接使用Ford对象作为参数，Ford类修改，Player类需要重新编译和调式
     */
    public void play(Ford car){
        car.accelerate();
        car.brake();
    }
    /**
     * 开奇瑞
     * 不好的依赖，高层模块依赖了低层模块
     * Player直接使用Chery对象作为参数，Chery类修改，Player类需要重新编译和调式
     */
    public void play(Chery car){
        car.accelerate();
        car.brake();
    }
    /**
     * 开车
     * 好的依赖
     * 只有ICar修改时Player才需要修改
     */
    public void play(ICar car){
        car.accelerate();
        car.brake();
    }
}

