from flask import Flask, render_template,request,session,logging,url_for,redirect,flash
 



app = Flask(__name__)

@app.route("/")
def home():
  
    return 'e-kazi your job solution'


if __name__ == "__main__":
    app.run(debug =True)