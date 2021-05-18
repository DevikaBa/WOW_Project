# Python libraries, using the Flask package allowed us to import functions necessary to make our program user friendly
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pandas as pd
import csv
from flask_fontawesome import FontAwesome


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
    # HTTP request , comsuming data, GET request is used for viewing something
    if request.method == "GET":
        return render_template('search.html')
    # POST is used for changing something
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



# user page / ###this function sessions in not in use ,but for future use##   
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
 




 








    
            
# main driver/ the allows or prevents parts of the code from being run when the modules are imported
if __name__ == "__main__":
    app.run(debug=True, threaded=True)



    

   