from flask import Flask, jsonify, render_template, request
import pandas as pd
import pickle



#* request is a module in python which is used to send HTTP requests. It is used to send GET, POST, PUT, DELETE requests to the server. It is also used to handle the response from the server. It is a very popular module in python and it is used in many projects. where as requests is a library in python which is used to send HTTP requests. It is built on top of the request module and it is used to send GET, POST, PUT, DELETE requests to the server. It is also used to handle the response from the server. It is a very popular library in python and it is used in many projects.

app=Flask(__name__)


 #*  Building a Frontend for ML APIs and Local Testing

@app.route('/')
def bwt():
  return render_template('index.html')
 

def get_cleaned_data(baby_data):
  
  gestation=float(baby_data['gestation'])
  parity=int(baby_data['parity'])
  age=float(baby_data['age'])
  height=float(baby_data['height'])
  weight=float(baby_data['weight'])  
  smoke=float(baby_data['smoke'])  

 
  cleaned_data ={
    "gestation": [gestation],
    "parity": [parity],
    "age": [age],
    "height": [height],
    "weight": [weight],
    "smoke": [smoke]
                 }

  return cleaned_data

@app.route('/predict', methods=['POST'])
def get_prediction():
   #*GETTING DATA FROM FORM 
  baby_data=request.form
  baby_cleaned_data=get_cleaned_data(baby_data)

  #* CONVERTING INTO DATAFRAME, BCZ  OUR TRAINED /API DATA IS IN DATAFRAME FORMAT 
  baby_df=pd.DataFrame(baby_cleaned_data)

 #* LOADING MACHINE LEARNING TRAINED MODEL , later we keep pkl file outside the model dir in production phase and delete the model directory
  with open("model.pkl","rb") as f:
    model=pickle.load(f)

 #* MAKING PREDICTION ON USER DATA
  pred=model.predict(baby_df) 
  predict=round(float(pred[0]),2)


#* RETURNING RESPONSE IN JSON FORMAT
  # response={"Prediction": predict} 
  
  return render_template("index.html", response = predict)


if __name__=="__main__":
  app.run(debug=True, port=5050)
