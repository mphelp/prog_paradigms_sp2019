// Name: Matthew Phelps
// Date: Mar 6 2019

package edu.nd.cse.paradigms;

import java.util.Queue;
import java.lang.Object;

public class PEEventQueue implements Queue {
	public PEKeyEvent peek(){}
	public PEKeyEvent element(){}
	public PEKeyEvent poll(){}
	public PEKeyEvent remove(){}
	public boolean add(PEKeyEvent evt){
		return true;
	}
	public boolean offer(PEKeyEvent evt){
		return true;
	}
}
