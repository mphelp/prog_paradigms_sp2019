// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.util.ArrayList;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Color;

public class PEEngine extends Frame {
	protected PEGame game; 
	protected PEScreen screen;
	protected int width = 640;
	protected int height = 480;
	protected int titlebarHeight = 0;
	protected objects<PEWorldObject>;

	public void tick(){
		// call all objects' ticks
		// do all renders
		// repaint the display
	}
	public PEEngine(PEGame game){
		this.game = game;
		this.screen = new PEScreen(width, height);
		setVisible(true);

		// array list of objects
		this.objects = new ArrayList<PEWorldObject>();
	}
	public void update(Graphics g){
		this.paint(g);
	}
	public void paint(Graphics g){
		g.drawImage(screen.render(), 0, titlebarHeight, 
				width, height, Color.BLACK, null);
	}
}
