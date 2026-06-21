 #* .\venv\Scripts\Activate
  #* python main.py
#* by default flask uses GET method

#* Importing Flask 
from flask import Flask, jsonify, render_template
import requests

 #* Create flask instance, here __name__ is the name of the current module; it helps Flask to know where to look for templates and static files. and Flask is a class and we are creating an object of that class. __name__ is a special variable in python which gives the name of the module. If we are running the script directly then it will return __main__ and if we are importing the script then it will return the name of the script.
app=Flask(__name__)


#* Defining () and route

@app.route("/",methods=['GET'])   #* TO PAAS POST METHOD; use methods=['POST']
def home():
   data="this is the profile page"
   return data

@app.route("/profile")
def profile():
   data="this is the profile page"
   return data

   
@app.route("/upload", methods=["GET"])
def form():
   return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
   return "Welcome! Form submitted successfully :)"

 #* IN POST OUR DATA IS SEND IN BODY NOT IN URL
@app.route("/submit",methods=["POST"])
def Submit():
   return "Welcome to your Home page"

#* Linking html code with python using flask(API); render_template to do the same

@app.route("/home")
def home_page():
    #* To paas varialbe and show in html =>  paas the var here and use {{var_name}} in html o show the name
    name="Anonymous"
    age=26
    return render_template("index.html", name=name, age=age)
    


@app.route("/about")
def about_us():
   data="This is about page! YOUR FORM SUBMITTED SUCCESSFULLY :)"
   return data


@app.route("/contact")
def contact_us():
   data="Follow us to get regular updates"
   return data


#* RETURNING DIFFERENT FORMAT LIKE HTML, JSON ETC
@app.route("/prog")
def prog():
   return """<h1> Namaste Bharat :) </h1> """


#* import and Use jsonify to return data in json format

@app.route("/info")
def info2():
   data={"name":"Anonymous",
         "age":26,
         "code": 7,
         "area":12}
   return jsonify(data)


#* Triggering the flask app

if __name__ == "__main__":
  app.run(debug=True, port=5050)



# * `__name__` is a special Python variable holding the module’s name.
# * When you run a script directly, `__name__` is set to `"__main__"`.
# * When a script is imported, `__name__` is the script’s filename/module name.
# * `if __name__ == "__main__":` runs the code inside only if the script is run directly.
# * It prevents code from running when the script is imported as a module elsewhere.
# * In Flask, it ensures the server starts only when you execute the file, not when imported.

#* When we say "run the script directly," it means:

#* You execute the Python file by itself from the command line, like this:

#* python main.py
#* You are telling Python, "Run this file as the main program."

#* This is different from importing the script inside another Python file**,** for example: 
 #* import main

# debug=True does two things:

# ✅ Auto-reloads the server when you save code changes (no need to re-run manually).

# ✅ Shows detailed error pages in the browser if something breaks.

# 🔁 You still need to run python main.py once to start the server.


# * PORT=5050 means the Flask server will listen for incoming requests on port 5050 instead of the default 5000. You can access your app at http://localhost:5050/ after starting it.
# * This is useful if you want to run multiple Flask apps on the same machine or avoid conflicts with other services using port 5000.



#   *                   -----------------------------------------
 #*  GETTING RESPONSE FROM FLASK API USING REQUESTS MODULE AND IN JSON FORMAT


#* using requests module to get response from flask API; we need to run the flask app first and then run this code in another file or in python shell to get the response from flask API.

@app.route("/pics")
def get_news():
   API_KEY="00cf399ecf85493caf7615633ba2bda2"
   
   # url="https://newsapi.org/v2/everything?q=tesla&from=2025-06-27&sortBy=publishedAt&apiKey={API_KEY}"
   # url="https://newsapi.org/v2/everything?q=tesla&from=2026-05-07&sortBy=publishedAt&apiKey=00cf399ecf85493caf7615633ba2bda2"
   url="https://newsapi.org/v2/everything?q=tesla&from=2026-05-07&sortBy=publishedAt&apiKey=00cf399ecf85493caf7615633ba2bda2"
   resp=requests.get(url)
   print(resp.status_code)  #* to check if we are getting response or not; 200 means success
   print(resp.json())       #* to get the response in json format