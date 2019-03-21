// Name: Matthew Phelps
// Date: Feb 24 2019
import edu.nd.cse.paradigms.*;
import java.util.List;
import java.util.ArrayList;

public class MyGame extends PEGame {
	public void start(){
		
		// Add engine
		engine = new PEEngine(this);

		// Add player: x position, y position, size
		player = new Player(200, 200, 20);

		// Add target
		target = new Target(player);

		// Add projectile
		projectile = new Projectile();

		// Add enemies: x position, y position, size
		//        min x position, max x position, directionRightScalar, 
		// 				hit points, speed
		enemy1 = new Enemy(50,30,20,
				10,300,-1,0,2);
		enemy2 = new Enemy(80,30,30,
				10,300, 1,0,1);

		// Add ALL to engine
		engine.add(projectile);
		engine.add(player);	
		engine.add(target);
		engine.add(enemy1);
		engine.add(enemy2);

		// Collider
		collider = new HardCollider(engine);
	}
	public void tick(){}
	public void collisionDetected(List<PEWorldObject> worldObjects){
		int i = 0;
		for (PEWorldObject wo: worldObjects){
			collider.processCollision(wo, worldObjects.get(i^1));
			i++;
		}
	}
	public void keyPressed(int keycode){
		int px = player.getX();
		int py = player.getY();
		int tx = target.getX();
		int ty = target.getY();
		switch (keycode){
			// move target
			case PEKeyEvent.VK_DOWN:
				ty += 5;
				break;
			case PEKeyEvent.VK_LEFT:
				tx -= 5;
				break;
			case PEKeyEvent.VK_RIGHT:
				tx += 5;
				break;
			case PEKeyEvent.VK_UP:
				ty -= 5;
				break;
			// move player
			case PEKeyEvent.VK_A:
				px -= 5;
				break;
			case PEKeyEvent.VK_W:
				py -= 5;
				break;
			case PEKeyEvent.VK_D:
				px += 5;
				break;
			case PEKeyEvent.VK_S:
				py += 5;
				break;
			// shoot projectile
			case PEKeyEvent.VK_SPACE:
				projectile.sendToTarget(player, target);
				break;
		}
		target.setCenter(tx,ty);
		player.setCenter(px,py);
	}

	private Enemy enemy1;
	private Enemy enemy2;
	private Player player;
	private Target target;
	private Projectile projectile;

	protected HardCollider collider;
	protected PEEngine engine;
}
