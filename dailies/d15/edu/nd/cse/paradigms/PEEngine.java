// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.util.ArrayList;
import java.util.List;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.event.*;
import java.util.LinkedList;

public class PEEngine extends Frame implements KeyListener {
	protected PEGame game; 
	protected PEScreen screen;
	private PECentralClock clock;
	protected int width = 640;
	protected int height = 480;
	protected int titlebarHeight = 0;
	protected ArrayList<PEWorldObject> objects;
	protected LinkedList<PEKeyEvent> queue;

	public PEEngine(PEGame game){
		this.game = game;
		this.screen = new PEScreen(width, height);
		setVisible(true);
		this.clock = new PECentralClock(this);

		// array list of objects
		this.objects = new ArrayList<PEWorldObject>();
		// event queue
		this.queue = new LinkedList<PEKeyEvent>();
		// register self as Key listener
		addKeyListener(this);
	}
	public void tick(){
		// eventloopiterate all the key events
		eventLoopIterate();

		// call all objects' ticks
		for (PEWorldObject wo: objects){
			wo.tick();
		}
		screen.clear();
		// do all renders after clear
		for (PEWorldObject wo: objects){
			screen.renderWorldObject(wo);
		}
		// repaint the display
		repaint();
	}
	public void update(Graphics g){
		this.paint(g);
	}
	public void paint(Graphics g){
		g.drawImage(screen.render(), 0, titlebarHeight, 
				width, height, Color.BLACK, null);
	}
	public void add(PEWorldObject wo){
		objects.add(wo);
	}
	public void remove(PEWorldObject wo){
		objects.remove(wo);
	}

	// New for d15:
	private void processEvent(PEKeyEvent evt){
		this.game.keyPressed(evt.getKeyCode());
	}
	private void eventLoopIterate(){
		while(!queue.isEmpty()){
			processEvent(queue.remove());
		}
	}
	public void keyPressed(KeyEvent evt){
		PEKeyEvent peke = new PEKeyEvent(evt);
		processEvent(peke);
	}
	public void keyReleased(KeyEvent evt){}
	public void keyTyped(KeyEvent evt){}
}
