// Matthew Phelps

// Initialize
UpButton    = new Button();
DownButton  = new Button();
TitleLabel  = new Label();
MovieImg    = new Img();
RatingLabel = new Label();
MyContainer       = new MyDiv();
MyContainerparent = new MyDiv();

// Create
TitleLabel.createLabel("Movie Title", "titleLabel");
RatingLabel.createLabel("Movie Rating", "ratingLabel");

MyContainer.createMyDiv("container");
MyContainerparent.createMyDiv("containerparent");
UpButton.createButton("UP", "upbutton");
MovieImg.createImg("movieimg");
DownButton.createButton("DOWN", "downbutton");

UpButton.addTo(MyContainer);
MovieImg.addTo(MyContainer);
DownButton.addTo(MyContainer);
MyContainer.addTo(MyContainerparent);

// Add
TitleLabel.addToDocument();
MyContainerparent.addToDocument();
RatingLabel.addToDocument();



// label.createLabel("guess who", "theLabel");
// label.addToDocument();

// button.createButton("Click Here", "thebutton");
// MOVIE_ID = 32
// args = [label, "http://student04.cse.nd.edu:51001/movies/"+MOVIE_ID, MOVIE_ID];
// button.addClickEventHandler(changeText, args);
// button.addToDocument();

// label2.createLabel("I thought this movie was ...", "theLabel2");
// label2.addToDocument();


// Voting Div
// mydiv.createMyDiv();
// drop.createDropdown({ 
// 	1: 'terrible',
// 	2: 'subpar',
// 	3: 'decent',
// 	4: 'great',
// 	5: 'fantastic'
// }, "thedrop", 1);

// vote.createButton("VOTE", "thevoter");
// let user_id = 32;
// voteargs = [drop, "http://student04.cse.nd.edu:51001/recommendations/32", MOVIE_ID];
// vote.addClickEventHandler(sendVote, voteargs);
// drop.addTo(mydiv);
// vote.addTo(mydiv);

// mydiv.addToDocument();

