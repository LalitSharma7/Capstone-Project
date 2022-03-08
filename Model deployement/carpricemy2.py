#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler


# In[2]:


app = Flask(__name__)
model = pickle.load(open(r"C:\Users\lalisharma\Documents\model\reg3.pkl", "rb"))
@app.route('/',methods=['GET'])
def Home():
    return render_template('cars.html')


# In[3]:


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
       
    if request.method == 'POST':
        year = int(request.form['year'])
        km_driven=int(request.form['km_driven'])
        mileage=float(request.form['mileage'])
        engine=int(request.form['engine'])
        max_power=int(request.form['max_power'])
        seats=int(request.form['seats'])
        fuel_Diesel=request.form['fuel_Diesel']
        if(fuel_Diesel=='Petrol'):
                fuel_LPG=0
                fuel_Petrol=1
                fuel_Diesel=0
        elif(fuel_Diesel=='Diesel'):
            fuel_LPG=0
            fuel_Petrol=0
            fuel_Diesel=1         
        else:
            fuel_LPG=0
            fuel_Petrol=1
            fuel_Diesel=0
        seller_type_Individual=request.form['seller_type_Individual']
        if(seller_type_Individual=='Individual'):
            seller_type_Individual=1
            seller_type_TrustmarkDealer=0
        else:
            seller_type_Individual=0
            seller_type_TrustmarkDealer=1
        transmission_Manual=request.form['transmission_Manual']
        if(transmission_Manual=='Manual'):
            transmission_Manual=1
        else:
            transmission_Manual=0
        owner_FourthAboveOwner=request.form['owner_Fourth & Above Owner']
        if(owner_FourthAboveOwner=='Fourth & Above Owner'):
            owner_FourthAboveOwner=1
            owner_SecondOwner=0
            owner_TestDriveCar=0
            owner_ThirdOwner=0
        elif(owner_FourthAboveOwner=='Second Owner'):
            owner_FourthAboveOwner=0
            owner_SecondOwner=1
            owner_TestDriveCar=0
            owner_ThirdOwner=0
        elif(owner_FourthAboveOwner=='Test Drive Car'):
            owner_FourthAboveOwner=0
            owner_SecondOwner=0
            owner_TestDriveCar=0
            owner_ThirdOwner=0
        else:
            owner_FourthAboveOwner=0
            owner_SecondOwner=0
            owner_TestDriveCar=1
            owner_ThirdOwner=0
        prediction=model.predict(np.array([[year, 
                                            km_driven,
                                            mileage,
                                            engine,
                                            max_power,
                                            seats,
                                            fuel_Diesel,
                                            fuel_LPG,
                                            fuel_Petrol,
                                            seller_type_Individual,
                                            seller_type_TrustmarkDealer,
                                            transmission_Manual,
                                            owner_FourthAboveOwner,
                                            owner_SecondOwner,
                                            owner_TestDriveCar,
                                            owner_ThirdOwner
                                            ]]))
        output=round(prediction[0],2)
        if output<0:
            return render_template('cars.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('cars.html',prediction_text="You can sell the Car at {} ".format(output))
    else:
        return render_template('cars.html')


# In[4]:


if __name__=="__main__":
    app.run(debug=True)

