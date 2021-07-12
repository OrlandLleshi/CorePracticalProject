from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_background', methods=['GET'])
def get_background():
    return random.choice([
        'Young rich kid that grew up in the city',
        'Young poor kid that grew up in the city',
        'Young wealthy kid that grew up in the country', 
        'Young poor kid that grew up in the country', 
        ])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)