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

function Img(){
  this.createImg = function(id){
    this.item = document.createElement("IMG");

    this.item.setAttribute("id", id);
    this.movie_id = null;
  }
}
Img.prototype = new Item()

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
function getMovieRecommendation(args){
  let user_id = args[0];
  let recAddr = args[1];
  let xhr3 = new XMLHttpRequest();
  xhr3.open('GET', recAddr + user_id, true);
  xhr3.send(null);
  xhr3.onload = function(e){
    let res = JSON.parse(xhr3.responseText);
    console.log(res);
    // set movie info
    setMovieInfo(args, res);
  }
}
function setMovieInfo(args, res){
  let movieImg    = args[2]; // object
  let movieTitle  = args[3]; // object
  let movieRating = args[4]; // object
  let movieAddr   = args[5]; // movie address
  let imgLocation = args[6]; // image name
  let ratingAddr  = args[7]; // rating address

  // add id to movie img
  movieImg.movie_id = res['movie_id'];
  // get movie info
  let xhr = new XMLHttpRequest();
	xhr.open('GET', movieAddr + res['movie_id'], true);
	xhr.send(null);
	xhr.onload = function(e){
    // label.item.innerText = xhr.responseText;
    let res = JSON.parse(xhr.responseText);
    let imgUrl = imgLocation + res['img'];
    //console.log(imgUrl);
    movieImg.item.src = imgUrl; // set src
    movieTitle.item.innerText = res['title']; // set title
  }
  // get movie rating
  let xhr2 = new XMLHttpRequest();
  xhr2.open('GET', ratingAddr + res['movie_id'], true);
  xhr2.send(null);
  xhr2.onload = function(e){
    let res2 = JSON.parse(xhr2.responseText);
    console.log(res2);
    movieRating.item.innerText = res2['rating']; // set rating
  }
}

function voteUp(args){
	// var drop = args[0]; 
	// var addr = args[1];
	// var movie_id = args[2];
	// if (!movie_id){
	// 	console.error("Movie id not been retrieved. Cannot send vote yet");
	// 	return
  // }
  let user_id = args[0];
  let recAddr = args[1];
  let movieImg    = args[2]; // object
  let movieTitle  = args[3]; // object
  let movieRating = args[4]; // object
  let movieAddr   = args[5]; // movie address
  let imgLocation = args[6]; // image name
  let ratingAddr  = args[7]; // rating address


	let req = new XMLHttpRequest();
	req.open('PUT', recAddr + user_id, true);
	let data = {}
	data['movie_id'] = movieImg.movie_id; 
	data['rating']   = 5;
	console.log(JSON.stringify(data))
	
	req.send(JSON.stringify(data));
	req.onload = function(e){
		console.log('Response:\n ');
		console.log(req.responseText);
    getMovieRecommendation(args); // show new movie
	}
}

function voteDown(args){
	// var drop = args[0]; 
	// var addr = args[1];
	// var movie_id = args[2];
	// if (!movie_id){
	// 	console.error("Movie id not been retrieved. Cannot send vote yet");
	// 	return
  // }
  let user_id = args[0];
  let recAddr = args[1];
  let movieImg    = args[2]; // object
  let movieTitle  = args[3]; // object
  let movieRating = args[4]; // object
  let movieAddr   = args[5]; // movie address
  let imgLocation = args[6]; // image name
  let ratingAddr  = args[7]; // rating address


  let req = new XMLHttpRequest();
	req.open('PUT', recAddr + user_id, true);
	let data = {}
	data['movie_id'] = movieImg.movie_id; 
	data['rating']   = 1;
	console.log(JSON.stringify(data))
	
	req.send(JSON.stringify(data));
	req.onload = function(e){
		console.log('Response:\n ');
		console.log(req.responseText);
    getMovieRecommendation(args); // show new movie
	}
}
