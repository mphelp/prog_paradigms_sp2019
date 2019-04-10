// Matthew Phelps

button = new Button();
label  = new Label();
label2 = new Label();
drop   = new Dropdown();
mydiv  = new MyDiv();
vote   = new Button();

label.createLabel("guess who", "theLabel");
label.addToDocument();

button.createButton("Click Here", "thebutton");
args = [label, "http://student04.cse.nd.edu:51001/movies/32"];
button.addClickEventHandler(changeText, args);
button.addToDocument();

label2.createLabel("I thought this movie was ...", "theLabel2");
label2.addToDocument();


// Voting Div
mydiv.createMyDiv();
drop.createDropdown({ 
	1: 'fantastic',
	2: 'great',
	3: 'decent',
	4: 'subpar',
	5: 'terrible'
}, "thedrop", 1);

vote.createButton("VOTE", "thevoter");
let user_id = 32;
voteargs = [drop, "http://student04.cse.nd.edu:51001/recommendations/32"];
vote.addClickEventHandler(sendVote, args);
drop.addTo(mydiv);
vote.addTo(mydiv);

mydiv.addToDocument();

