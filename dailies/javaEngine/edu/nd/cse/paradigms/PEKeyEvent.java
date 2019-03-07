// Name: Matthew Phelps
// Date: Mar 5 2019

package edu.nd.cse.paradigms;

import java.awt.event.KeyEvent;

public class PEKeyEvent extends PEEvent {
	PEKeyEvent(KeyEvent awtKeyEvent){
		this.awtKeyEvent = awtKeyEvent;
	}
	public int getKeyCode(){
		return awtKeyEvent.getKeyCode();
	}

	public static final int VK_DOWN = KeyEvent.VK_DOWN;
	public static final int VK_UP = KeyEvent.VK_UP;
	public static final int VK_RIGHT = KeyEvent.VK_RIGHT;
	public static final int VK_LEFT = KeyEvent.VK_LEFT;
	public static final int VK_W = KeyEvent.VK_W;
	public static final int VK_A = KeyEvent.VK_A;
	public static final int VK_S = KeyEvent.VK_S;
	public static final int VK_D = KeyEvent.VK_D;
	public static final int VK_SPACE = KeyEvent.VK_SPACE;
	private KeyEvent awtKeyEvent;
}
