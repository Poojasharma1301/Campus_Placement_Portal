from typing import MutableMapping
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import pandas as pd
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        ssc_p = float(request.form['ssc_p'])
        hsc_p = float(request.form['hsc_p'])
        degree_p= float(request.form['degree_p'])
        mba_p= float(request.form['mba_p'])

        gender = request.form['gender']
        print(gender)
        if(gender == 'Male'):
            gender = 1
        
        else:
            gender = 0

        specialisation= request.form['specialisation']
        print(specialisation)
        if(specialisation == 'Mkt&HR'):
            specialisation = 1
        
        else:
            specialisation = 0

        workex = request.form['workex']
        if(workex == 'workex_yes'):
            workex= 1
        
        else:
            workex = 0


        hsc_s = request.form['hsc_s']
        if(hsc_s == 'hsc_commerce'):
            hsc_commerce = 1
            hsc_science = 0
            hsc_art = 0
        
        elif(hsc_s =='hsc_science'):
            hsc_commerce = 0
            hsc_science = 1
            hsc_art = 0
        else:
            hsc_commerce = 0
            hsc_science = 0
            hsc_art = 1

        degree_t = request.form['degree_t']
        if(degree_t== 'degree_t_st'):
            degree_t_st = 1
            degree_t_cm = 0
            degree_t_o = 0
                
        
        elif(degree_t== 'degree_t_cm'):
            degree_t_st = 0
            degree_t_cm = 1
            degree_t_o = 0
        else:
           degree_t_st = 0
           degree_t_cm = 0
           degree_t_o = 1
       
        print("Donne")
        prediction = model.predict([[hsc_p,ssc_p,degree_p,mba_p,gender,specialisation,workex,hsc_commerce,hsc_art,hsc_science,degree_t_st,degree_t_cm,degree_t_o]])
        print("Done")
        if prediction==1:
             return render_template('index.html',prediction_text="Congratulations You're Placed")
        else:
             return render_template('index.html',prediction_text="Develop Your self Not Placed")
                
if __name__=="__main__":
    app.run(debug=True)
