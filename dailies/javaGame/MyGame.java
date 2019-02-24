// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame {
	public void start(){
		// Definitions
		engine = new PEEngine(this);

		// TODO: Add player

		// TODO: Add target

		// TODO: Add enemies
		// Enemy enemy1 = new Enemy(50,30,10,300,true)
		// 

		// circle = new PECircle();
		// circle.setRadius(25);
		// circle.setCenter(100,100);
		// square = new PESquare();
		// square.setCenter(150,150);
		// square.setSize(40);

		// Adding to engine
		// engine.add(circle);
		// engine.add(square);

		

		// Collider
		collider = new EasyCollider(engine);
	}
	public void tick(){}
	public void collisionDetected(List<PEWorldObject> worldObjects){
		int i = 0;
		for (PEWorldObject wo: worldObjects){
			collider.processCollision(wo, worldObjects.get(i));
			i++;
		}
	}
	public void keyPressed(int keycode){
		int x = circle.getX();
		int y = circle.getY();
		switch (keycode){
			case PEKeyEvent.VK_DOWN:
				y += 5;
				break;
			case PEKeyEvent.VK_LEFT:
				x -= 5;
				break;
			case PEKeyEvent.VK_RIGHT:
				x += 5;
				break;
			case PEKeyEvent.VK_UP:
				y -= 5;
				break;
		}
		circle.setCenter(x,y);
	}

	private Enemy enemy1;
	private Enemy enemy2;
	protected PEEngine engine;
	// private PECircle circle;
	protected EasyCollider collider;
	// private PESquare square;	
}
