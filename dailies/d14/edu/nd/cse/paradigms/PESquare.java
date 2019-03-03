// Name: Matthew Phelps
package edu.nd.cse.paradigms;

public class PESquare {
	private int x, y;
	private int size;
	private int color;

	public PESquare(){
		this.x = 50;
		this.y = 50;
		this.size = 10;
	}
	public getX(){ return x; }
	public getY(){ return y; }
	public setSize(int size){
		this.size = size;
	}
	public setCenter(int x, int y){
		this.x = x;
		this.y = y;
	}
	public setColor(int color){
		this.color = color;
	}

	public void tick(){}
	public void render(PEScreen screen){
		for (int i = x - (int)size/2; i < x + (int)size/2; i++){
			for (int j = y - (int)size/2; j < y + (int)size/2; j++){
				if screen.inBounds(i, j)
					screen.setPixel(i, j, this.color);
			}	 
		}
	}
}
