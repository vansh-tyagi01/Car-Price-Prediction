from flask import Flask,render_template,request,url_for,redirect
import pandas as pd
import pickle

app=Flask(__name__)
car=pd.read_csv("Cleaned_Car.csv")

model = pickle.load(open("LinearRegressionModel.pkl","rb"))

# @app.route('/')
# def index():
#     companies = sorted(car['company'].unique())
#     car_models = sorted(car['name'].unique())
#     year = sorted(car['year'].unique(),reverse=True)
#     fuel_type = car['fuel_type'].unique()

#     return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)



@app.route("/", methods=["GET", "POST"])
def index():

    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    prediction = None

    if request.method == "POST":

        company = request.form.get('company')
        name = request.form.get('name')
        year = int(request.form.get('years'))
        fuel = request.form.get('fuel')
        kms_driven = int(request.form.get('kms_driven'))

        data = pd.DataFrame([{
            "name": name,
            "company": company,
            "year": year,
            "kms_driven": kms_driven,
            "fuel_type": fuel
        }])

        prediction = round(model.predict(data)[0], 2)

    return render_template(
        "index.html",
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_type=fuel_type,
        prediction=prediction
    )