// Matthew Phelps
// Date: Feb 15 2019
import paradigms.*;
public class ParadigmsTest {
	public static void main(String args[]){
		Sphere s = new Sphere(5.0);
		System.out.println(s);
		s.setRadius(6.0);
		System.out.println(s);
		System.out.println("Surface area is " + s.getSurfaceArea());
	}
}