// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
public class Enemy extends PESquare {
	private int size;
	private int maxX;
	private int minX;
	private int directionRight;
	private int hitPoints;
	private int stride;

	Enemy(int x, int y, int size, int minX, int maxX, int directionRight,
			int hitPoints, int stride){
		// this.x 		= x;
		// this.y 		= y;
		setCenter(x, y);
		this.size = size;
		setSize(size);
		this.maxX = maxX;
		this.minX = minX;
		this.directionRight 	= directionRight;
		this.hitPoints 	= hitPoints;
		this.stride 		= stride;
		//testing
		System.out.println("Enemy created and directionRight is "+directionRight);
	}
	public void tick(){
		int x = getX();
		int y = getY();
		if (x >= maxX || x <= minX){
			directionRight = (-1)*directionRight;
		}	
		x += (directionRight)*stride;
		setCenter(x, y);
 	}
}
