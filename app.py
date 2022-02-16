# Unsplash Image Scraper API
# Description: An API that takes in a search parameter uses it to search
# for an image in Unsplash. It returns a JSON as
# {"imageURL": "URL to image"}.
# To use this:
# 1. Register for an API key at https://unsplash.com/s/photos/register.
# 2. Open a terminal at the location of app.py.
# 3. Type in and run: py ./app.py
# 4. To make a search use {URL}/search?q=searchParam where searchParam
# is the image you're looking for.

import json
import os
import sys
import logging
from urllib.request import urlopen

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# Receive my API KEY from Heroku
API_KEY = os.getenv("API_KEY", "optional-default")

app = Flask(__name__, template_folder='templates/')

# Check what's wrong
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)



# Include Flask CORS in application to solve Cross Origin Resource Sharing
# Source: https://flask-cors.readthedocs.io/en/latest/
CORS(app)


@app.route('/')
def index():
    """
    Renders the API instructions
    :return: HTML home page.
    """
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Takes in a search parameter and uses that parameter to search
    an image on Unsplash. After getting a response back from Unsplash,
    it takes the raw image URL and sends back the URL as JSON formatted
    as {"imageUrl": url to image}.
    To use url/?search=searchTerm where searchTerm is the image
    you're looking for.
    :return: Json file formatted as {"imageUrl": url to image}.
    """
    if request.method == 'GET' or request.method == 'POST':
        # Get the request
        args = request.args
        # Get the query string
        q = args.get('q')
        # Create the URL for unsplash to take the first image for the
        # first image
        url = 'https://api.unsplash.com/search/photos/?page=1&query=' + q \
              + '&client_id=' + API_KEY + '&per_page=1'
        # Send the GET request
        response = urlopen(url)
        # Parse the json
        data_json = json.loads(response.read())
        # Set the imageUrl to change
        imageUrl = ''
        # Store a raw image url to output
        for result in data_json['results']:
            # Take the raw image URL
            imageUrl = result['urls']['raw']
        # Send out json object as {searchTerm : imageUrl }
        return jsonify({"imageUrl": imageUrl})
    # Incorrect usage, send back to home page.
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    """
    Sets the 404 page.
    :param error:
    :return: Renders the 404 html page.
    """
    return render_template('404.html', title='404'), 404


if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
