// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

// import java.util.stream.*;
// import java.util.Arrays;
import java.awt.image.BufferedImage;

public class PEScreen {
	private int width, height;
	private int bg;
	private BufferedImage image;
	private int[][] pixels; // x then y

	public PEScreen(int width, int height){
		this.width = width;
		this.height = height;
		this.pixels = new int[width][height];
		this.bg = 0x22BB11;

		this.image = new BufferedImage(width, height,
				BufferedImage.TYPE_INT_RGB);
		this.clear();
	}
	public void setPixel(int px, int py, int color){
		pixels[px][py] = color;
	}
	public void clear(){
		for (int i = 0; i < width; i++){
			for (int j = 0; j < height; j++){
				setPixel(i, j, bg);
			}
		}
	}
	public boolean inBounds(int px, int py){
		return (py < height && py >= 0 && px < width && px >= 0);
	}
	public BufferedImage render(){
		// int[] flatPixels = Arrays.stream(pixels)
		// 	.flatMapToInt(Arrays::stream)
		// 	.toArray();
		for (int i = 0; i < width; i++){
			for (int j = 0; j < height; j++){
				image.setRGB(i, j, pixels[i][j]);
			}
		}
		// image.setRGB(0,0,width,height,flatPixels,0,1);
		return image;
	}
}
