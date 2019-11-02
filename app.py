from flask import Flask, render_template, url_for, redirect, request, session, flash
from functools import wraps

methods = ['GET', 'POST'] #defined for ease

#session is stored in server as data
#session id is stored in client side as cookies

app = Flask(__name__)
app.secret_key = '1499058058097067107'

#------------------DECORATOR WRAPPER FOR MANAGING LOGIN SESSIONS
def login_required(f):
    @wraps(f)
    def wrap(*args, **kws):
        if "logged_in" in session:
            return f(*args, **kws)
        
        else:
            flash("You need to login first!")
            return redirect(url_for('login'))

    return wrap

#-----------------NAVIGATIONAL ROUTES---------------------
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

#------------------------MATCH DETAILS ROUTE---------------------
@app.route("/ongoing", methods=methods)
def ongoing():
    return render_template("ongoing.html",title="Current Match")

#-------------------ADMIN ROUTES---------------------------------
@app.route("/dashboard", methods=methods)
@login_required
def dashboard():
    return render_template("dashboard.html",title="Dash Board")

@app.route("/match", methods=methods)
@login_required
def match():
    return render_template("match.html", title="Match")


#--------------------LOGIN-LOGOUT ROUTES--------------------------
@app.route("/login", methods=methods)
def login():
    error = None
    if request.method == 'POST':
        if request.form['login_username'] !='admin' or request.form['login_password'] !='password':
            error = "! Invalid credentials, please try again"
        
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))

    return render_template("login.html",title="Login admin", error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)