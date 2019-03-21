// Name: Matthew Phelps

package edu.nd.cse.paradigms;

import java.util.TimerTask;
import java.util.Timer;

class PECentralClock extends TimerTask {
	protected Timer timer;
	private PEEngine engine;

	PECentralClock(PEEngine engine, int rate){
		timer = new Timer();
		timer.scheduleAtFixedRate(this, 0, rate);
		this.engine = engine;
	}
	PECentralClock(PEEngine engine){
		timer = new Timer();
		timer.scheduleAtFixedRate(this, 0, 250);
		this.engine = engine;
	}
	public void run(){
		// call engine tick
		engine.tick();
	}
}
