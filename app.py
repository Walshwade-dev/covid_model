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
        cough = request.form["cough"]
        fever = request.form["fever"]
        head_ache = request.form["head_ache"]
        sore_throat = request.form["sore_throat"]
        shortness_of_breath = request.form["shortness_of_breath"]
        

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
        int_features = [[int(cough, fever, sore_throat, head_ache, shortness_of_breath), gender, age_60_and_above, test_indication]]
        final_features = (int_features)
        print (final_features)

           

        # print(Contact with confirmed,
        #     Abroad,
        #     Other)

       
        
        prediction=model.predict([[cough, fever, sore_throat, head_ache, shortness_of_breath, gender, age_60_and_above]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your corona result is:".format(output))


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
