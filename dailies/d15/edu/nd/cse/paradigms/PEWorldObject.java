// Name: Matthew Phelps
// Date: Mar 6 2019

package edu.nd.cse.paradigms;

public abstract class PEWorldObject {
	protected int x, y;
	protected int color;

	public PEWorldObject(){
		this.x = 50;
		this.y = 50;
		this.color = 0xFFFFFF;
	}
	public void setCenter(int x, int y){
		this.x = x;
		this.y = y;
	}
	public void setColor(int color){
		this.color = color;
	}
	public int getX(){ return x; }
	public int getY(){ return y; }
	public int getColor(){ return color; }
	public abstract void tick();
	public abstract void render(PEScreen screen);
}
