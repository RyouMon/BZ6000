package pool;
import java.awt.*;
import javax.swing.*;


public class BallGame extends JFrame{

    Image ball = Toolkit.getDefaultToolkit().getImage("images/ball.png");
    Image desk = Toolkit.getDefaultToolkit().getImage("images/desk.jpg");

    double x = 100;
    double y = 100;
    boolean right = true;

    public void paint(Graphics g){
        System.out.println("窗口被画一次");
        g.drawImage(desk,0,30,null);
        g.drawImage(ball,(int)x,(int)y,null);
        if(right){
            x = x+10;
        }else{
            x = x-10;
        }
        if(x>1280-46-50){
            right = false;
        }

        if(x<46){
            right = true;
        }
    }

    void launchFrame(){
        setSize(1280,750);
        setLocation(50,50);
        setVisible(true);
        //重画
        while(true){
            repaint();
            try{
                Thread.sleep(40);
            }catch(Exception e){
                e.printStackTrace();
            }

        }
    }
    public static void main(String[] args){
        BallGame game = new BallGame();
        game.launchFrame();
    }
}
