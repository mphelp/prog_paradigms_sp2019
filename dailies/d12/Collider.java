public abstract class Collider{
	protected PEEngine engine;
	public Collider(PEEngine engine){
		this.engine = engine;
	}
	public abstract void processCollision(PECircle c, PEWorldObject wo);
	public void processCollision(PEWorldObject wo1, PEWorldObject wo2){
		if (wo1 instanceof PECircle){
			processCollision(w01, w02);
		} else {
			System.out.println("not defined "+w01.getClass().getName());
		}
	}
}
