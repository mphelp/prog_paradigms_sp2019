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
	private double 	hypotenuse;
	private boolean hasTarget;

	Projectile(){
		this.offScreenX = -10;
		this.offScreenY = -10;
		setCenter(offScreenX, offScreenY);
		this.doubX = x;
		this.doubY = y;
		this.hasTarget = false;
		this.hypotenuse = 1;
	}
	public void sendToTarget(Player pl, Target t){
		// current
		setCenter(pl.getX(),pl.getY());
		this.doubX = x;
		this.doubY = y;
		// target
		this.targX = t.getX();
		this.targY = t.getY();
		double x_dist = targX - doubX;
		double y_dist = targY - doubY;

		this.hypotenuse = Math.hypot(x_dist, y_dist);
		this.hasTarget = true;
	}
	public void reset(){
		this.hasTarget = false;
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
			return;
		}
		// else move to target
		// double hyp = Math.hypot(x_dist, y_dist);
		int pixel_x, pixel_y;
		this.doubX = x + 8*x_dist/hypotenuse; // speed: 6
		this.doubY = y + 8*y_dist/hypotenuse;
		if (x_dist > 0){
			pixel_x = (int)Math.ceil(doubX);
		} else {
			pixel_x = (int)Math.floor(doubX);
		}
		if (y_dist > 0){
			pixel_y = (int)Math.ceil(doubY);
		} else {
			pixel_y = (int)Math.floor(doubY);
		}
		setCenter(pixel_x, pixel_y);
 	}
}
