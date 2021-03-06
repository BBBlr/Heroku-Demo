# Working file . Model should be dumped using pickle commnad not joblib

import numpy as np

from flask import Flask, request, jsonify, render_template

import joblib

import pickle

app = Flask(__name__)

model = pickle.load(open('Jaipur_model_pickle.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # prediction = model.predict(final_features)

    prediction = model.predict([int_features])      # 2-d array is reuqired as an input

    output = round(prediction[0],2)

    return render_template('index.html', prediction_text='Night temperature would be {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)