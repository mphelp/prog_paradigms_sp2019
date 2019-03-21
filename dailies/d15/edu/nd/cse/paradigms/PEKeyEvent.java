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
		
		this.awtKeyEvent = awtKeyEvent;
	}
	public int getKeyCode(){
		return awtKeyEvent.getKeyCode();
	}

	private int VK_DOWN;
	private int VK_UP;
	private int VK_RIGHT;
	private int VK_LEFT;
	private KeyEvent awtKeyEvent;
}
