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
		target = new Target(player);

		// TODO: Add enemies
		enemy1 = new Enemy(50,30,20,
				10,300,-1,1,2);
		enemy2 = new Enemy(80,30,30,
				10,300, 1,1,1);
		// 

		// Adding to engine

		engine.add(player);	
		engine.add(target);
		engine.add(enemy1);
		engine.add(enemy2);

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
		int px = player.getX();
		int py = player.getY();
		int tx = target.getX();
		int ty = target.getY();
		switch (keycode){
			case PEKeyEvent.VK_DOWN:
				py += 5;
				break;
			case PEKeyEvent.VK_LEFT:
				px -= 5;
				break;
			case PEKeyEvent.VK_RIGHT:
				px += 5;
				break;
			case PEKeyEvent.VK_UP:
				py -= 5;
				break;
			case PEKeyEvent.VK_A:
				tx -= 5;
				break;
			case PEKeyEvent.VK_W:
				ty -= 5;
				break;
			case PEKeyEvent.VK_D:
				tx += 5;
				break;
			case PEKeyEvent.VK_S:
				ty += 5;
				break;
				// add event for spacebar
		}
		player.setCenter(px,py);
	}

	private Enemy enemy1;
	private Enemy enemy2;
	protected PEEngine engine;
	private Player player;
	protected EasyCollider collider;
	// private PESquare square;	
}
