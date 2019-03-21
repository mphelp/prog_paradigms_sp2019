// Name: Matthew Phelps
// Date: Feb 17 2019
import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame {
	public void start(){
		engine = new PEEngine(this);
		circle = new PECircle();
		circle.setRadius(25);
		circle.setCenter(25,25);
		engine.add(circle);
	}
	public void tick(){}
	public void collisionDetected(List<PEWorldObject> worldObjects){}
	public void keyPressed(int keycode){
		int x = circle.getX();
		int y = circle.getY();
		switch (keycode){
			case PEKeyEvent.VK_DOWN:
				y += 5;
				break;
		}
		circle.setCenter(x,y);
	}
	protected PEEngine engine;
	protected PECircle circle;
}
