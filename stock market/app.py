import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__,template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))




@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
 
   

    output=round(prediction[0],1)
    
    

    return render_template('index1.html', prediction_text='Value : {}'.format(output))

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
