// Matthew Phelps

// Initialize
UpButton    = new Button();
DownButton  = new Button();
TitleLabel  = new Label();
MovieImg    = new Img();
RatingLabel = new Label();
MyContainer       = new MyDiv();

// Create
TitleLabel.createLabel("Movie Title", "titleLabel");
RatingLabel.createLabel("Movie Rating", "ratingLabel");

MyContainer.createMyDiv("container");
UpButton.createButton("UP", "upbutton");
MovieImg.createImg("movieimg");
DownButton.createButton("DOWN", "downbutton");

UpButton.addTo(MyContainer);
MovieImg.addTo(MyContainer);
DownButton.addTo(MyContainer);

// Add
TitleLabel.addToDocument();
MyContainer.addToDocument();
RatingLabel.addToDocument();

// Testing movie img
let user_id = 149
let MovieAddr = "http://student04.cse.nd.edu:51043/movies/";
let RecAddr = "http://student04.cse.nd.edu:51043/recommendations/";
let ImgLocation  = "https://www3.nd.edu/~cmc/teaching/cse30332/images";
let RatingAddr = "http://student04.cse.nd.edu:51043/ratings/";
args = [
  user_id,
  RecAddr,
  MovieImg,
  TitleLabel,
  RatingLabel,
  MovieAddr,
  ImgLocation,
  RatingAddr
]
getMovieRecommendation(args)

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

