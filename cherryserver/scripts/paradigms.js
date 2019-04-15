// Author: Matthew Phelps
// Date:   Apr 8 2019

// FUNCTION DEFINITIONS
function Item(){
	// Sort of abstract func
	this.addToDocument = function(){
		document.body.appendChild(this.item);
	}
	this.addTo = function(node){
		node.item.appendChild(this.item);
	}
}

function MyDiv(){
	this.createMyDiv = function(id){
		this.item = document.createElement("DIV");

		this.item.setAttribute("id", id);
	}
}
MyDiv.prototype = new Item()

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

function Dropdown(){
	this.createDropdown = function(dict, id, selected){
		this.item = document.createElement("SELECT");

		this.item.setAttribute("id", id);
		for (var index in dict){
			var option = document.createElement("OPTION");
			option.text = dict[index];
			this.item.add(option);
		}
	}
	this.getSelected = function(){
		return this.item.selectedIndex + 1;
	}
}
Dropdown.prototype = new Item()

var movie_id;

function changeText(args){
	var label = args[0];
	var addr  = args[1];
	var xhr = new XMLHttpRequest();
	xhr.open('GET', addr, true);
	xhr.send(null);
	xhr.onload = function(e){
		label.item.innerText = xhr.responseText;
		movie_id = Number(JSON.parse(xhr.responseText)['id']);
		console.log(movie_id);
	}
}
function sendVote(args){
	var drop = args[0]; 
	var addr = args[1];
	var movie_id = args[2];
	if (!movie_id){
		console.error("Movie id not been retrieved. Cannot send vote yet");
		return
	}

	var req = new XMLHttpRequest();
	req.open('PUT', addr, true);
	var data = {}
	data['movie_id'] = movie_id; 
	data['rating']   = drop.getSelected();
	console.log(JSON.stringify(data))
	
	req.send(JSON.stringify(data));
	req.onload = function(e){
		// Do nothing currently
		console.log('Response:\n ');
		console.log(req.responseText);
	}
}

