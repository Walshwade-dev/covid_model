from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # symptoms
        # test day and month
        test_date = request.form["test_date"]
        test_day = int(pd.to_datetime(test_date, format="%Y-%m-%d").day)
        test_month = int(pd.to_datetime(test_date, format ="%Y-%m-%d").month)
        # print("Journey Date : ",Journey_day, Journey_month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # fever
        fever = int(input("Experiencing fever"))
        
        # print("enter one or zero for yes or no")

        # sore_throat
        sore_throat = int(input("Experiencing sore_throat"))
        
        # print("enter one or zero for yes or no")

        # shortness_of_breath
        shortness_of_breath = int(input("Experiencing shortness_of_breath"))
        
        # print("enter one or zero for yes or no")

        # Head_ache
        Head_ache = int(input("Experiencing Head_ache"))
        
        # print("enter one or zero for yes or no")

        # categorical data
        # age_60_and_above

        age_60_and_above =request.form['age_60_and_above']
        if(age_60_and_above=='yes'):
            age_60_and_above = 1
            
        elif (age_60_and_above=='No'):
            age_60_and_above = 0
        
        # print(yes, 
        # No)

        gender =request.form['gender']
        if(gender=='male'):
            gender = 1
            
        elif(gender=='female'):
            gender = 0

        # print(male, 
        # female)



        test_indication =request.form['test_indication']
        if(test_indication=='Contact with confirmed'):
            test_indicatio = 1
            
        elif (test_indication == 'Abroad'):
            test_indication = 2

        else:
            test_indication = 3

           

        # print(Contact with confirmed,
        #     Abroad,
        #     Other)

       
        
        prediction=model.predict([corona_result])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your corona result is:".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
