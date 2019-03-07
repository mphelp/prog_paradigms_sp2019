// Name: Matthew Phelps
// Date: Feb 24 2019
import java.awt.Color;
import edu.nd.cse.paradigms.*;

public class Target extends PESquare {

	Target(Player p){
		setCenter(p.getX(), p.getY());
		setColor(0xFF0000); // red target
	}
}
