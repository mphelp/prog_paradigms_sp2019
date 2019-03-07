// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public class EasyCollider extends Collider {
	public EasyCollider(PEEngine engine){
		super(engine);
	}
	public void processCollision(Projectile pr, PEWorldObject wo){
		if (wo instanceof Enemy){
			System.out.println("Enemy destroyed by projectile");
			engine.remove(wo);
			pr.reset();
		}
	}
}
