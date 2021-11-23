import joblib
from flask import Flask, render_template, redirect, url_for, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/terms')
def terms():
    return render_template("tc.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/disinformation")

def disindex():
    return render_template("disinformation.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")
def ValuePredictorBreast(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 5:
        loaded_model_Breast = joblib.load('BreastDTC.pkl')
        result = loaded_model_Breast.predict(to_predict)
    return result[0]


@app.route("/predictcancer",  methods=['GET', 'POST'])
def predictcancer():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 5:
            result = ValuePredictorBreast(to_predict_list, 5)
        if(int(result) == 1):
            prediction = "Patient has a high risk of Breast Cancer, please consult your doctor immediately"
        else:
            prediction = "Patient has a low risk of Breast Cancer"
    return render_template("cancer_result.html", prediction_text=prediction)

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

def ValuePredictordiabetes(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 6:
        loaded_model_diabetes = joblib.load('diabetesDTC.pkl')
        result = loaded_model_diabetes.predict(to_predict)
    return result[0]


@app.route("/predictdiabetes",  methods=['GET', 'POST'])
def predictdiabetes():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 6:
            result = ValuePredictordiabetes(to_predict_list, 6)
        if(int(result) == 1):
            prediction = "Patient has a high risk of Diabetes, please consult your doctor immediately"
        else:
            prediction = "Patient has a low risk of Diabetes"
    return render_template("diabetes_result.html", prediction_text=prediction)


@app.route("/heart")
def heart():
    return render_template("heart.html")

def ValuePredictorheart(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 7:
        loaded_model_heart = joblib.load('HeartDTC.pkl')
        result = loaded_model_heart.predict(to_predict)
    return result[0]


@app.route("/predictheart",  methods=['GET', 'POST'])
def predictheart():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 7:
            result = ValuePredictorheart(to_predict_list, 7)
        if(int(result) == 1):
            prediction = "Patient has a high risk of Heart Disease, please consult your doctor immediately"
        else:
            prediction = "Patient has a low risk of Heart Disease"
    return render_template("heart_result.html", prediction_text=prediction)

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

def ValuePredictorKidney(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 7:
        loaded_model_kidney = joblib.load('KidneyRFC.pkl')
        result = loaded_model_kidney.predict(to_predict)
    return result[0]


@app.route("/predictkidney",  methods=['GET', 'POST'])
def predictkidney():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 7:
            result = ValuePredictorKidney(to_predict_list, 7)
        if(int(result) == 1):
            prediction = "Patient has a high risk of Kidney Disease, please consult your doctor immediately"
        else:
            prediction = "Patient has a low risk of Kidney Disease"
    return render_template("kidney_result.html", prediction_text=prediction)


@app.route("/liver")
def liver():
    return render_template("liver.html")

def ValuePredictorliver(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 7:
        loaded_model_liver = joblib.load('LiverRFC.pkl')
        result = loaded_model_liver.predict(to_predict)
    return result[0]


@app.route("/predictliver",  methods=['GET', 'POST'])
def predictliver():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 7:
            result = ValuePredictorliver(to_predict_list, 7)
        if(int(result) == 2):
            prediction = "Patient has a high risk of Liver Disease, please consult your doctor immediately"
        else:
            prediction = "Patient has a low risk of Liver Disease"
    return render_template("liver_result.html", prediction_text=prediction)




if __name__ == "__main__":
    app.run(debug=True)