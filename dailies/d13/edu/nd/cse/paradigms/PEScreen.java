// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.awt.image.BufferedImage;

public class PEScreen {
	private int width, height;
	private int bg;
	private BufferedImage image;
	private int[][] pixels; // x then y

	public PEScreen(int width, int height){
		this.width = width;
		this.height = height;

		this.bg = 0x22BB11;

	}
	public void setPixel(int px, int py, int color){
		pixels[px][py] = color;
	}
	public void clear(){}
	public boolean inBounds(int px, int py){
		return false;
	}
	public BufferedImage render(){
		return image;
	}
}
