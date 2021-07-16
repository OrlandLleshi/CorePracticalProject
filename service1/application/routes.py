from application import db, app
from application.models import Story
from flask import render_template
import requests



@app.route('/')
def home():
    character = requests.get('http://character_api:5001/get_character') 
    background = requests.get('http://background_api:5002/get_background')
    endpoint = requests.post('http://endpoint_api:5003/get_endpoint', json= {'character':character.text, 'background':background.text})
    
    story= Story(character=character.text, background=background.text, endpoint=endpoint.text)

    db.session.add(story)
    db.session.commit()
    
    return render_template('index.html', character=character.text, background=background.text, endpoint=endpoint.text)

    
    
