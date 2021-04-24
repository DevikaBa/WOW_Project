# Python libraries, using the Flask package allowed us to import functions necessary to make our program user friendly
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pandas as pd
import csv
from flask_fontawesome import FontAwesome
from fuzzywuzzy import fuzz
import Levenshtein as lev 


# create app instance
app = Flask(__name__)
# using font awesome to create an attractive user page 
fa = FontAwesome(app)
app.secret_key = "PythonDoctors"
app.permanent_session_lifetime = timedelta(minutes=1)    

# this code is necessary to read the csv file  
df = pd.read_csv("DoctorData.csv", index_col=0)


# the get and post methods are used to retrieve data from our database and post the data requested

@app.route('/search', methods=['GET', 'POST'])
# function for search page
def search():

    if request.method == "GET":
        return render_template('search.html')

    elif request.method == 'POST':
        # coding to read the csv file
        df = pd.read_csv("DoctorData.csv", index_col=0)
        # coding that turns the zipcode function into string
        df['Zipcode'] = df['Zipcode'].astype(str)
        # coding to allow the user to input for doctors names/specialty 
        user_input = request.form.get('user_input')
        # coding to allow the user to input for zip codes searches
        user_zip = request.form.get('user_zip')
         
       # filtering speciality per user input
        if user_input != "":
            word = df = df[df.Specialty == user_input]  

     # filtering if user input is entered in lower and upper case

            # match1 = "Family Medicine"
            # match2 = "family medicine"
            # Ratio = fuzz.ratio(match1.lower(),match2.lower())
            # Partial_Ratio = fuzz.partial_ratio(match1.lower(),match2.lower())
            # print(Ratio)
            # print(Partial_Ratio)

        # filtering zip code per user input
        if user_zip != "":
            df = df[df.Zipcode == user_zip]
        # rendering the search function
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
    # The requests module allows us to send HTTP requests using Python
    # Session (session) data is stored on the server
    if request.method == "POST":
       # which will use a cookie with a defined expiration date
        session.permanent = True
        # requesting from form
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
        # redirect to the login page if your not logged in
        return redirect(url_for("login"))
# log out page 
@app.route("/logout")    
def logout():
    # flashes this comment if your logged out
    flash("you've been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    # redirects user to login page if they log out
    return redirect(url_for("login"))       
 
    
            
# main driver
if __name__ == "__main__":
    app.run(debug=True, threaded=True)



    

   