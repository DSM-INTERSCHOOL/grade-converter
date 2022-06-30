
import imp
from flask import Flask,jsonify,request
from gradeconverter import to_grade_card
import requests



app = Flask(__name__)


@app.route("/<idSchool>/grades")
def hello_world(idSchool):
    query_parameters = ''
    for key, value in request.args.items():
        if(query_parameters==''):
            query_parameters += '?{0}={1}'.format(key, value)
        else:
            query_parameters += '&{0}={1}'.format(key, value)

    print(query_parameters)
    api_url = "http://localhost:8989/"+idSchool+"/grades"+query_parameters
    print(api_url)
    response = requests.get(api_url)        
    #return jsonify(response.json())
    return to_grade_card(response.text) 


