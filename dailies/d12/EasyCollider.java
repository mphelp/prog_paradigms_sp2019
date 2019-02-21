import edu.nd.cse.paradigms.*;

public class EasyCollider extends Collider{
	public EasyCollider(PEEngine engine){
		super(engine);
	}
	public void processCollision(PECircle c, PEWorldObject wo){
		System.out.println("Circle destroyed! oh no! that was intended");
		engine.remove(c);
	}
}
