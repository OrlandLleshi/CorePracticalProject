from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_character', methods=['GET'])
def get_character():
    return random.choice(['Arian','Ricky','Thiago', 'Carson', 'Duncan'])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)