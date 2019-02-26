// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;

public class Projectile extends PESquare {
	private int offScreenX;
	private int offScreenY;
	private int targX;
	private int targY;
	private double  doubX;
	private double  doubY;
	private boolean hasTarget;

	Projectile(){
		this.offScreenX = -10;
		this.offScreenY = -10;
		setCenter(offScreenX, offScreenY);
		this.doubX = x;
		this.doubY = y;
		this.hasTarget = false;
		//testing
		System.out.println("Projectile created");
	}
	public void sendToTarget(Player pl, Target t){
		// current
		setCenter(pl.getX(),pl.getY());
		this.doubX = x;
		this.doubY = y;
		// target
		this.targX = t.getX();
		this.targY = t.getY();
		this.hasTarget = true;
		System.out.println("Target set");
	}
	public void tick(){
		double x_dist = targX - doubX;
		double y_dist = targY - doubY;
		// relocate standing still if no target or HIT target
		if (!hasTarget || (Math.abs(x_dist) < 2 && Math.abs(y_dist) < 2)){
			setCenter(-10,-10);
			this.hasTarget = false;
			this.doubX = x;
			this.doubY = y;
			// TODO: Set color
			// setColor(Color.)
			return;
		}
		// else move to target
		double hyp = Math.hypot(x_dist, y_dist);
		this.doubX = x + 2*x_dist/hyp;
		this.doubY = y + 2*y_dist/hyp;
		setCenter((int)Math.round(doubX), (int)Math.round(doubY));

 	}
}
