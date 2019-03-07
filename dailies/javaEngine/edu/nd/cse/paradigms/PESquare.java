// Name: Matthew Phelps
// Date: Mar 6 2019
package edu.nd.cse.paradigms;

public class PESquare extends PEWorldObject {
	private int size;

	public PESquare(){
		super();
		this.size = 10;
	}
	public void setSize(int size){
		this.size = size;
	}

	public void tick(){}
	public void render(PEScreen screen){
		for (int i = x - (int)Math.floor(size/2); i < x + (int)Math.ceil(size/2); i++){
			for (int j = y - (int)Math.floor(size/2); j < y + (int)Math.ceil(size/2); j++){
				screen.setPixel(i, j, this.color);
			}	 
		}
	}
	public boolean inObjectBoundary(int qx, int qy){
		return ((qx >= x - (int)Math.floor(size/2)) &&
						(qx <= x + (int)Math.ceil(size/2)) &&
						(qy >= y - (int)Math.floor(size/2)) &&
						(qy <= y + (int)Math.ceil(size/2)));
	}
}
