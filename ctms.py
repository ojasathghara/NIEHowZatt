from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html",title="Schedule")

@app.route("/teams")
def teams():
    return render_template("teams.html",title="All Teams")

@app.route("/points")
def points():
    return render_template("points.html",title="Points")

@app.route("/rules")
def rules():
    return render_template("rules.html",title="Rules")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/login")
def login():
    return render_template("login.html",title="Login admin")

@app.route("/ongoing")
def ongoing():
    return render_template("ongoing.html",title="Current Match")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",title="Dash Board")

if __name__ == "__main__":
    app.run(debug=True)