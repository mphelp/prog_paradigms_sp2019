// Name: Matthew Phelps
// Date: Mar 6 2019
package edu.nd.cse.paradigms;

public class PECircle extends PEWorldObject {
	private int radius;

	public PECircle(){
		super();
		this.radius = 10;
	}
	public void setRadius(int radius){
		this.radius = radius;
	}

	public void tick(){}
	public void render(PEScreen screen){
		for (int i = x - radius; i < x + radius; i++){
			for (int j = y - radius; j < y + radius; j++){
				if (Math.hypot(i-x, j-y) <= 1.00){
					screen.setPixel(i, j, this.color);
				}
			}	 
		}
	}
	public boolean inObjectBoundary(int qx, int qy){
		return (Math.hypot(qx - x, qy - y) <= (float)radius);
	}
}
