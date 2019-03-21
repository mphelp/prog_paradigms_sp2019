package paradigms;
public class Sphere {
	private double radius;
	public Sphere(double radius){
		this.radius = radius;
	}
	public void setRadius(double radius){
		this.radius = radius;
	}
	public double getRadius(){
		return this.radius;
	}
	public double getVolume(){
		return (4.0/3.0)*Math.PI*Math.pow(radius,3);
	}
	public double getSurfaceArea(){
		return 4.0*Math.PI*Math.pow(radius,2);
	}
	public String toString(){
		String s = String.format("Radius: %15.1f\n", radius);
		s += String.format("Volume: %29.13f\n", getVolume());
		s += String.format("Surface Area: %23.13f\n", getSurfaceArea());
		return s;
	}
}
