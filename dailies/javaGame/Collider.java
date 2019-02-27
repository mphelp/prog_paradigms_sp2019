// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public abstract class Collider{
	protected PEEngine engine;
	public Collider(PEEngine engine){
		this.engine = engine;
	}
	public abstract void processCollision(Projectile pr, PEWorldObject wo);

	public void processCollision(PEWorldObject wo1, PEWorldObject wo2){
		if (wo1 instanceof Projectile){

				processCollision((Projectile)wo1, wo2);

		} else if (wo1 instanceof Enemy){

			if (wo2 instanceof Player){
				engine.remove(wo2);
				System.out.println("Player killed by enemy !!!");
			}	

		} else {
			// Ignore all other cases
		}
	}
}
