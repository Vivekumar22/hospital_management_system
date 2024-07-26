from flask import *


#cretae an instance for flask
app=Flask(__name__)

#Template Rendering
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/meditation")
def meditation():
    return render_template("meditation.html")

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

@app.route("/yoga")
def yoga():
    return render_template("yoga.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

@app.route("/doctor")
def doctor():
    return render_template("doctor.html")

@app.route("/register")
def register():
    return render_template("register.html")


#main method/function
if __name__=="__main__":
    app.run()