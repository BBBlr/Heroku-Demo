import flask
from flask import request, render_template
import joblib
app = flask.Flask(__name__)
app.config["DEBUG"]=True

from flask_cors import CORS
CORS(app)

@app.route('/', methods=['GET'])
def default():
    return '''<h1> Hello Data Scientist </h1>'''

@app.route('/corona', methods=['GET'])
def corona():
    return '''<h1> Corona infection not flattening. </h1>'''


@app.route('/search', methods=['GET'])
def search():
    return '''<h1> Searching ....''' +request.args['s']+ ''' </h1>'''

@app.route('/predict', methods=['GET'])
def predict():

    model = joblib.load('Jaipur_model.pkl')
    temperature = model.predict([[int(request.args['morning']),
                            int(request.args['noon']),
                            int(request.args['evening']),
                            ]])
    return str(round(temperature[0]))

app.run()