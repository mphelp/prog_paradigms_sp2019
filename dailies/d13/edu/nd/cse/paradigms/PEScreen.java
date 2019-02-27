// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.awt.image.BufferedImage;

public class PEScreen {
	private BufferedImage image;

	public PEScreen(int width, int height){}
	public void setPixel(int px, int py, int color){}
	public void clear(){}
	public boolean inBounds(int px, int py){
		return false;
	}
	public BufferedImage render(){
		return image;
	}
}
