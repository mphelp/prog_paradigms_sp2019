// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public abstract class Collider{
	protected PEEngine engine;
	public Collider(PEEngine engine){
		this.engine = engine;
	}
	// 
	// public abstract void processCollision(Player pl, PEWorldObject wo);
	// public abstract void processCollision(Enemy e, PEWorldObject wo);
	public abstract void processCollision(Projectile pr, Enemy e);


	public void processCollision(PEWorldObject wo1, PEWorldObject wo2){
		// Here is where we redirect to collisions in easy, medium, hard based on types of objects
		if (wo1 instanceof Projectile){

			if (wo2 instanceof Enemy){
				// damage enemy
				processCollision((Projectile)wo1, (Enemy)wo2);
			}

		} else if (wo1 instanceof Enemy){

			if (wo2 instanceof Player){
				engine.remove(wo2);
				System.out.println("Player destroyed by enemy !!!");
			}	

		} else {
			// System.out.println("not defined "+wo1.getClass().getName());
		}
	}
}
