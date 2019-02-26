// Name: Matthew Phelps
// Date: Feb 21 2019
import edu.nd.cse.paradigms.*;

public abstract class Collider{
	protected PEEngine engine;
	public Collider(PEEngine engine){
		this.engine = engine;
	}
	// 
	public abstract void processCollision(PECircle c, PEWorldObject wo);
	public abstract void processCollision(Enemy e, PEWorldObject wo);



	public void processCollision(PEWorldObject wo1, PEWorldObject wo2){
		// Here is where we redirect to collisions in easy, medium, hard based on types of objects
		if (wo1 instanceof PECircle){
			processCollision((PECircle)wo1, wo2);
		} else if (wo1 instanceof Enemy && wo2 instanceof Enemy){
			// ignore
		} else {
			// System.out.println("not defined "+wo1.getClass().getName());
		}
	}
}
