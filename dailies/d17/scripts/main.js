// Creat button and Label on the fly
var Item = {
	addToDocument: function(){
		document.body.appendChild(this.item);
	}
}

var Label = {
	createLabel: function(text, id){
		this.item = document.createElement("P");

		this.item.setAttribute("id", id);
		//var t = document.createTextNode(text);
		//this.item.appendChild(t);
		this.item.innerHTML = text;
	},
	setText: function(text){
		this.item.innerHTML = text;
	}
}
Label.__proto__ = Item

var Button = {
	createButton: function(text, id){
		this.item = document.createElement("Button");

		this.item.setAttribute("id", id);
		this.item.innerText = text;
	},
	addClickEventHandler: function(handler, args){
		this.item.onmouseup = function(){
			handler(args);
		}
	}
}
Button.__proto__ = Item

function changeText(args){
	var text = args[0];
	var label = args[1];
	label.item.innerText = text;
}
// Use them
Button.createButton("Click Here", "theButton");
args = ["Matthew Phelps", Label];
Button.addClickEventHandler(changeText, args);
Button.addToDocument();

Label.createLabel("guess who", "theLabel");
Label.addToDocument();

