from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    character = requests.get('http://character_api:5000/get_character') 
    background = requests.get('http://background_api:5000/get_background')
    endpoint = requests.post('http://endpoint_api:5000/get_endpoint', json= {'character':character.text, 'background':background.text})
    return ender_template('index.html', character=character.text, background=background.text, endpoint=endpoint.text)


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)