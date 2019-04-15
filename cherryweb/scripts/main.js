// Matthew Phelps

// Initialize
UpButton    = new Button();
DownButton  = new Button();
TitleLabel  = new Label();
MovieImg    = new Img();
RatingLabel = new Label();
MyContainer = new MyDiv();

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

// Args
let user_id = 149 // arbitrarily chosen
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
getMovieRecommendation(args); // retrieve first recommendation

// Click event handlers defined in paradigms.js
UpButton.addClickEventHandler(voteUp, args);
DownButton.addClickEventHandler(voteDown, args);

// Add
TitleLabel.addToDocument();
MyContainer.addToDocument();
RatingLabel.addToDocument();

