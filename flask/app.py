# packages
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pandas as pd
import csv
import re


# create app instance
app = Flask(__name__)
app.secret_key = "hellotherebill"
app.permanent_session_lifetime = timedelta(minutes=1)

                    
df = pd.read_csv("DoctorData.csv", index_col=0)







# search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template('search.html')

    elif request.method == 'POST':
        df = pd.read_csv("DoctorData.csv", index_col=0)
        # turns the zipcode into string
        df['Zipcode'] = df['Zipcode'].astype(str)
        # getting the users input for doctors names/specialty 
        user_input = request.form.get('user_input')
        # getting the users input  zip codes 
        user_zip = request.form.get('user_zip')
         
        
        if user_input == "": 
            df = df[df.Zipcode == user_zip] 
    
                
        if user_zip == "":
            df = df[df.Specialty == user_input]

        return render_template("search.html", column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Patient ID", zip=zip)
    
        
        

        
# home page 
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

# login in page
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

# user page    
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
# log out page 
@app.route("/logout")    
def logout():
    flash("you have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))       
 
    
            
# main driver
if __name__ == "__main__":
    app.run(debug=True, threaded=True)



    

   