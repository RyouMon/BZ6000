/**
 * 测试continue语句
 */

public class TestContinue {
    public static void main(String[] args) {
        // 把100~150之间不能被3整除的数输出，并且每行输出5个
        int count = 0;
        for(int i=100; i<=150; i++){
            if(i%3==0){
                continue;
            }else{
                System.out.print(i+"\t");
                count ++;
            }
            if(count==5){
                System.out.println();
                count = 0;
            }
        }
    }
}
