import edu.nd.cse.paradigms.*;

public abstract class Collider{
	protected PEEngine engine;
	public Collider(PEEngine engine){
		this.engine = engine;
	}
	public abstract void processCollision(PECircle c, PEWorldObject wo);
	public void processCollision(PEWorldObject wo1, PEWorldObject wo2){
		if (wo1 instanceof PECircle){
			processCollision((PECircle)wo1, wo2);
		} else {
			System.out.println("not defined "+wo1.getClass().getName());
		}
	}
}
