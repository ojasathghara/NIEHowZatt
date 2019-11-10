from flask import Flask, render_template, url_for, redirect, request, session, flash
from functools import wraps

methods = ['GET', 'POST'] #defined for ease

#session is stored in server as data
#session id is stored in client side as cookies

app = Flask(__name__)
app.secret_key = '1499058058097067107'

match = {
    'team1_name': "India",
    'team2_name': "RSA",
    'winner_team': "India",
    'man_of_match': "Ojaswi"
}

indieTeamDetails = {
    'team_name': "India",
    'team_captain': "Ojaswi",
    'top_player': "Nikhil",   #must be updated after sql query.
    'matches': 5,
    'points': 10
}


# -----------------------------------------------------ROUTES------------------------------------------------------------

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

@app.route("/lastMatch")
def lastMatch():
    return render_template("lastMatch.html", title="Last Match", match=match)

@app.route("/teams/<teamName>")
def indieTeam(teamName):
    return render_template("indieTeam.html", team=indieTeamDetails)


#-------------------ADMIN and FORMS ROUTES---------------------------------
@app.route("/dashboard", methods=methods)
@login_required
def dashboard():
    return render_template("dashboard.html",title="Dash Board")

@app.route("/summary", methods=methods)
@login_required
def summary():
    return render_template("summary.html", title="Summary")

@app.route("/playerStat.html", methods=methods)
@login_required
def playerStat():
    return render_template("playerStat.html", title="Stats")

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

# ----------------------------------------------------------------ROUTES END-----------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)