// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
public class Enemy extends PESquare {
	private int maxX;
	private int minY;
	private boolean directionRight;
	private int hitPoints;
	private int stride;

	Enemy(int x, int y, int maxX, int minY, boolean directionRight,
			int hitPoints, int stride){
		this.x 		= x;
		this.y 		= y;
		this.maxX = maxX;
		this.minY = minY;
		this.directionRight 	= directionRight;
		this.hitPoints 	= hitPoints;
		this.stride 		= stride;
		System.out.println("Enemy created and directionRight is "+directionRight);
	}
	public void tick(){
		int x = getX();
		int y = getY();
		if (x >= maxX || x <= minX){
			directionRight = !directionRight;
		}	
		x += (directionRight)*stride;
}
