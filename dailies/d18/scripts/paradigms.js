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
	var label = args[0];
	var addr  = args[1];
	var xhr = new XMLHttpRequest();
	xhr.open('GET', addr, true);
	xhr.send(null);
	xhr.onload = function(e){
		label.item.innerText = xhr.responseText;
	}
}

// Use them
button = new Button();
label  = new Label();

label.createLabel("guess who", "theLabel");
label.addToDocument();

button.createButton("Click Here", "thebutton");
args = [label, "http://student04.cse.nd.edu:51001/movies/32"];
button.addClickEventHandler(changeText, args);
button.addToDocument();

