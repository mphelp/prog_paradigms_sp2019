// Name: Matthew Phelps
// Date: Feb 17 2019
import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame {
	public void start(){
		engine = new PEEngine(this);
		// Eventually will be circle
		square = new PESquare();
		// circle.setRadius(25);
		// circle.setCenter(25,25);
		// engine.add(circle);
		square.setSize(10);
		engine.add(square);
	}
	public void tick(){}
	public void collisionDetected(List<PEWorldObject> worldObjects){}
	public void keyPressed(int keycode){
		int x = square.getX();
		int y = square.getY();
		switch (keycode){
			case PEKeyEvent.VK_DOWN:
				y += 5;
				break;
		}
		square.setCenter(x,y);
	}
	protected PEEngine engine;
	// protected PECircle circle;
	protected PESquare square;
}
