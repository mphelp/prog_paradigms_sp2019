// Name: Matthew Phelps

abstract public class PEWorldObject {
	private int x, y;
	private int color;

	public PEWorldObject(){}
	public void setCenter(int x, int y){
		this.x = x;
		this.y = y;
	}
	public void setColor(int color){
		this.color = color;
	}
	public int getX(){ return x; }
	public int getY(){ return y; }
	public abstract void tick();
	public abstract void render(PEScreen screen);
}
