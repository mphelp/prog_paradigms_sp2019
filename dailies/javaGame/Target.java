// Name: Matthew Phelps
// Date: Feb 24 2019
import java.awt.Color;
import edu.nd.cse.paradigms.*;

public class Target extends PESquare {

	Target(Player p){
		setCenter(p.getX(), p.getY());
		setColor(new Color(200, 0, 0)); // red target
		//testing
		System.out.println("Target created");
	}
	// public void sendToTarget(Target t){
	// 	this.targX = t.getX();
	// 	this.targY = t.getY();
	// 	this.hasTarget = true;
	// }
	public void tick(){
		// int x_dist = targX - doubX;
		// int y_dist = targY - doubY;
		// // relocate standing still if no target or HIT target
		// if (!hasTarget || (x_dist < 2 && y_dist < 2)){
		// 	setCenter(350,350);
		// 	this.hasTarget = false;
		// 	this.doubX = x;
		// 	this.doubY = y;
		// 	// TODO: Set color
		// 	// setColor(Color.)
		// 	return;
		// }
		// // else move to target
		// double hyp = hypot(x_dist, y_dist);
		// this.doubX = x + x_dist/hyp;
		// this.doubY = y + y_dist/hyp;
		// setCenter(round(doubX), doubY);

 	}
}
