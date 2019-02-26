// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame {
	public void start(){
		// Definitions
		engine = new PEEngine(this, 100);

		// TODO: Add player
		player = new Player(200, 200, 20);

		// TODO: Add target
		// target = new Target();
		// TODO: Add enemies
		enemy1 = new Enemy(50,30,20,
				10,300,-1,1,2);
		enemy2 = new Enemy(80,30,30,
				10,300, 1,1,1);
		// 

		// Adding to engine

		engine.add(player);	
		engine.add(enemy1);
		engine.add(enemy2);

		// Collider
		collider = new EasyCollider(engine);
	}
	public void tick(){
		// Remove projectile after reaching target
	}
	public void collisionDetected(List<PEWorldObject> worldObjects){
		int i = 0;
		for (PEWorldObject wo: worldObjects){
			collider.processCollision(wo, worldObjects.get(i));
			i++;
		}
	}
	public void keyPressed(int keycode){
		// int x = circle.getX();
		// int y = circle.getY();
		int x = player.getX();
		int y = player.getY();
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
				// add event for spacebar
		}
		player.setCenter(x,y);
	}

	private Enemy enemy1;
	private Enemy enemy2;
	protected PEEngine engine;
	private Player player;
	protected EasyCollider collider;
	// private PESquare square;	
}
