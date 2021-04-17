# packages
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import csv

# create app instance
app = Flask(__name__)
app.secret_key = "hellotherebill"
app.permanent_session_lifetime = timedelta(minutes=1)

# df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
#                        "Patient ID": [123, 456],
#                        "Misc Data Point": [8, 53],
#                        "zip codes": [ "000000", "999999"]})
df = pd.read_csv("DoctorData.csv", index_col=0)
# df.to_html("output.html")
# pd.set_option('display.max_columns', 6)
# pd.set_option('display.max_rows', 5)
# # # print(df.head())

# # print(df.loc[df['Zip code'] == 91301])
# filt = (df['Specialty'] == 'Family Medicine')
# print(df.loc[filt])
# print(df[filt])


@app.route("/patient_list", methods=["POST", "GET"])
def patient_list():
    return render_template("patient_list.html", column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Patient ID", zip=zip)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template('search.html')

    elif request.method == 'POST':
        df = pd.read_csv("DoctorData.csv", index_col=0)
        user_input = request.form.get('user_input')
        # user_zip = request.form.get('user_zip')
         # specialty
        df = df[df.Specialty == user_input]

        
        flash("congrats, you have found your doctor") 



        print(user_input)
   
        return render_template("patient_list.html", column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Patient ID", zip=zip)
    
        
        

        
       
        
        

    
           
    

     

       
          

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Succesful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")
   
@app.route("/user", methods=["POST", "GET"]) 
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", user=user)    
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")    
def logout():
    flash("you have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))       
 
    
            
# main driver
if __name__ == "__main__":
    app.run(debug=True, threaded=True)



    

   