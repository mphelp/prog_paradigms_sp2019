// Use them
button = new Button();
label  = new Label();

label.createLabel("guess who", "theLabel");
label.addToDocument();

button.createButton("Click Here", "thebutton");
args = [label, "http://student04.cse.nd.edu:51001/movies/32"];
button.addClickEventHandler(changeText, args);
button.addToDocument();

