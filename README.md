# Unsplash Image Scraper
https://unsplash-amazable.herokuapp.com/

# Software Development Meme Generator

This project was developed using Flask.

## Search GET Method
After the API's URL web address, add the following /search? followed by the key value pairs below.
Set the key as q and the value as the image you're looking for.

### Example Search GET Method
https://unsplash-amazable.herokuapp.com/search?q=cats

### Example Success JSON Response
{ "imageURL": "https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixid=MnwyOTE1MTd8MHwxfHNlYXJjaHwxfHxjYXRzfGVufDB8fHx8MTY0NDYzMTUzOQ&ixlib=rb-1.2.1" }


### Search POST Method
Make a JSON POST request to this web app's search page. /search?
Set the key as q and the value as the image you're looking for.

### Example Search POST Method
{ "q":"cats"}

### Example Search POST Method
{ "imageURL": "https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixid=MnwyOTE1MTd8MHwxfHNlYXJjaHwxfHxjYXRzfGVufDB8fHx8MTY0NDYzMTUzOQ&ixlib=rb-1.2.1" } 
