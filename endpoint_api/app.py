from flask import Flask, request, Response


app = Flask(__name__)

@app.route("/get_endpoint", methods=["GET", "POST"])
def endpoint():
    story=request.get_json()
    
    if story['character']== 'Ricky' and story['background'] == 'Young rich kid that grew up in the city':
        end = "Bad Ending"
        
    elif story['character']== 'Ricky' and story['background'] == 'Young poor kid that grew up in the city':
        end = "Good Ending"

    elif story['character']== 'Arian' and story['background'] == 'Young rich kid that grew up in the city':
        end = "Bad Ending"
        
    elif story['character']== 'Arian' and story['background'] == 'Young poor kid that grew up in the city':
        end = "Good Ending"

    elif story['character']== 'Thiago' and story['background'] == 'Young rich kid that grew up in the city':
        end = "Good Ending"
        
    elif story['character']== 'Thiago' and story['background'] == 'Young poor kid that grew up in the city':
        end = "Bad Ending"

    elif story['character']== 'Carson' and story['background'] == 'Young rich kid that grew up in the city':
        end = "Good Ending"
        
    elif story['character']== 'Carson' and story['background'] == 'Young poor kid that grew up in the city':
        end = "Good Ending"

    elif story['character']== 'Duncan' and story['background'] == 'Young rich kid that grew up in the city':
        end = "Bad Ending"
        
    else: 
        end = "Good Ending"

    return Response(str(end))
        
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

    