package pool;

import javax.swing.*;
import java.awt.*;


public class BallGame2 extends BallGame {

    Image ball = Toolkit.getDefaultToolkit().getImage("images/ball.png");
    Image desk = Toolkit.getDefaultToolkit().getImage("images/desk.jpg");

    double x = 100;
    double y = 100;

    double degree = 3.14/3; //弧度60°

    public void paint(Graphics g){
        System.out.println("窗口被画一次");
        g.drawImage(desk,0,30,null);
        g.drawImage(ball,(int)x,(int)y,null);

        x = x+10*Math.cos(degree);
        y = y+10*Math.sin(degree);
        if(y>720-25-50||y<25){
            degree = -degree;
        }
        if(x<35||x>1280-35-50){
            degree = 3.14-degree;
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
        BallGame2 game = new BallGame2();
        game.launchFrame();
    }
}
