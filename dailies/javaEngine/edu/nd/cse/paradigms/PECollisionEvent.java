// Name: Matthew Phelps
// Date: Mar 5 2019

package edu.nd.cse.paradigms;

import java.util.List;

public class PECollisionEvent extends PEEvent {
	protected List<PEWorldObject> pairObjects;

	public PECollisionEvent(PEWorldObject wo1, PEWorldObject wo2){
		this.pairObjects = new List<PEWorldObject>();
		pairObjects.add(wo1);
		pairObjects.add(wo2);
	}
	public List<PEWorldObject> getWorldObjects(){
		return pairObjects;
	}
}
