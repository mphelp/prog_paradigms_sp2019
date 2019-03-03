// Name: Matthew Phelps
// Date: Feb 27 2019

import edu.nd.cse.paradigms.*;

class MyGame extends PEGame {
	private PEEngine engine;
	private CoolSquare cs;

	public void start(){
		engine = new PEEngine(this);

		cs = new CoolSquare();
		cs.setCenter(100, 100);
		cs.setSize(200);

		engine.add(cs);
	}
	public void tick(){}
}

