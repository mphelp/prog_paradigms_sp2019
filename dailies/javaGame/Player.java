// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
public class Player extends PECircle {
	private int radius;

	Player(int x, int y, int radius){
		setCenter(x, y);
		this.radius = radius;
		setRadius(radius);
		//testing
		System.out.println("Player created");
	}
	// public void tick(){
 	// }
}
