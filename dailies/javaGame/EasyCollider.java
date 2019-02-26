// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public class EasyCollider extends Collider {
	public EasyCollider(PEEngine engine){
		super(engine);
	}
	public void processCollision(Player pl, PEWorldObject wo){
		System.out.println("Player destroyed!");
		engine.remove(pl);
	}
}
