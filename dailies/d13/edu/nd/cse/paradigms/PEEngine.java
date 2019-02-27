// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Color;

public class PEEngine extends Frame {
	protected PEGame game; 
	protected PEScreen screen;
	protected int width = 640;
	protected int height = 480;
	protected int titlebarHeight = 0;

	public PEEngine(PEGame game){
		this.game = game;
	}
	public void paint(Graphics g){}
}
