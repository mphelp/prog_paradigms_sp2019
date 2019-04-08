// Author: Matthew Phelps
// Date:   Apr 8 2019

// FUNCTION DEFINITIONS
function Item(){
	// Sort of abstract func
	this.addToDocument = function(){
		document.body.appendChild(this.item);
	}
}

function Label(){
	this.createLabel = function(text, id){
		this.item = document.createElement("P");

		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	}
	this.setText = function(text){
		this.item.innerHTML = text;
	}
}
Label.prototype = new Item()

function Button(){
	this.createButton = function(text, id){
		this.item = document.createElement("Button");

		this.item.setAttribute("id", id);
		this.item.innerText = text;
	}
	this.addClickEventHandler = function(handler, args){
		this.item.onmouseup = function(){
			handler(args);
		}
	}
}
Button.prototype = new Item()

function changeText(args){
	var text = args[0];
	var label = args[1];
	label.item.innerText = text;
}
// Use them
button = new Button();
label  = new Label();

button.createButton("Click Here", "thebutton");
args = ["Matthew Phelps", label];
button.addClickEventHandler(changeText, args);
button.addToDocument();

label.createLabel("guess who", "theLabel");
label.addToDocument();

