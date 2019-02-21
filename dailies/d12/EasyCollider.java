public class EasyCollider extends Collider{
	public EasyCollider(PEEngine){
		super(engine);
	}
	public void processCollision(PECircle c, PEWorldObject wo){
		System.out.println("Circle destroyed");
		engine.remove(c);
	}
}
