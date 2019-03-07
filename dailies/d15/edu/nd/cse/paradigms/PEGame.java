// Name: Matthew Phelps
// Date: Feb 27 2019
package edu.nd.cse.paradigms;

import java.util.List;

public abstract class PEGame {
	public abstract void start();
	public abstract void tick();
	public abstract void keyPressed(int keyCode);
	public abstract void collisionDetected(List<PEWorldObject> objects);
}
