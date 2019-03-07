// Name: Matthew Phelps
// Date: Mar 5 2019

package edu.nd.cse.paradigms;

import java.awt.event.KeyEvent;
import java.lang.Object;

public class PEKeyEvent {
	PEKeyEvent(KeyEvent awtKeyEvent){
		this.VK_DOWN = awtKeyEvent.VK_DOWN;
		this.VK_UP = awtKeyEvent.VK_UP;
		this.VK_RIGHT = awtKeyEvent.VK_RIGHT;
		this.VK_LEFT = awtKeyEvent.VK_LEFT;
		this.VK_W = awtKeyEvent.VK_W;
		this.VK_A = awtKeyEvent.VK_A;
		this.VK_S = awtKeyEvent.VK_S;
		this.VK_D = awtKeyEvent.VK_D;
		this.VK_SPACE = awtKeyEvent.VK_SPACE;

		this.awtKeyEvent = awtKeyEvent;
	}
	public int getKeyCode(){
		return awtKeyEvent.getKeyCode();
	}

	private int VK_DOWN;
	private int VK_UP;
	private int VK_RIGHT;
	private int VK_LEFT;
	private int VK_W; 
	private int VK_A; 
	private int VK_S; 
	private int VK_D; 
	private int VK_SPACE;
	private KeyEvent awtKeyEvent;
}
