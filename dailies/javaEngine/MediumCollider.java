// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public class MediumCollider extends Collider {
	public MediumCollider(PEEngine engine){
		super(engine);
	}
	public void processCollision(Projectile pr, PEWorldObject wo){
		if (wo instanceof Enemy){
			// If enemy not hit
			if (((Enemy)wo).getHP() == 0){
				System.out.println("Enemy hit by projectile");
				((Enemy)wo).getsHit();
				wo.setColor(0xBB0000);
			} else {
				System.out.println("Enemy destroyed by projectile");
				engine.remove(wo);
			}
			pr.reset();
		}
	}
}
