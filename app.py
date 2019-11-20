from flask import Flask, render_template, url_for, redirect, request, session, flash
from functools import wraps
from database import Database, Player, Team, Match, LastMatch

methods = ['GET', 'POST'] #defined for ease

#session is stored in server as data
#session id is stored in client side as cookies

app = Flask(__name__)
app.secret_key = '1499058058097067107'


#----------------------------------------------------DATABASE INIT-------------------------------------------------------------------------
db = Database()


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

    topTeams = db.topTeams()   #home
    matches = db.homeMatches()  #home

    return render_template("home.html",title="Home", teams=topTeams, matches=matches)

@app.route("/schedule")
def schedule():

    allMatches = db.fullMatches() #./schedule

    return render_template("schedule.html",title="Schedule", schedule=allMatches)

@app.route("/points")
def points():

    allPoints = db.points() #./points

    allTeams = db.allTeams()    #./points

    return render_template("points.html",title="Points", points=allPoints, teams=allTeams)

@app.route("/rules")
def rules():
    return render_template("rules.html",title="Rules")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/lastMatch")
def lastMatch():

    matchRaw = db.getLastMatch()

    if matchRaw == (()):

        return render_template("lastMatch.html", title='Last Match', status=False)

    else:
        match = {
            'team1': matchRaw[0][0],
            'team2': matchRaw[0][1],
            'mom': matchRaw[0][2],
            'draw': matchRaw[0][3]
        }

        return render_template("lastMatch.html", title="Last Match", match=match, status=True)

@app.route("/teams/<teamName>")
def indieTeam(teamName):

    team = db.indieTeam(teamName)

    return render_template("indieTeam.html",title=team[0]['name'], teamStat=team[0], players=team[1])


#-------------------ADMIN and FORMS ROUTES---------------------------------
@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():

    ad_matches = db.ad_matches()    #./dashboard

    #---------------OPERATIONS--------------------------------

    if request.method == 'POST':

        if request.form.get('operation') == 'schedule_match':

            team1 = request.form.get('team1_id')
            team2 = request.form.get('team2_id')
            date  = request.form.get('date')

            match = Match(team1_id=team1, team2_id=team2, date=date)

            db.addMatch(match)   

            return redirect(url_for('dashboard'))  

        elif request.form.get('operation') == 'delete_match':

            match_id = request.form.get('match_id')

            match = Match(match_id=match_id)

            db.deleteMatch(match)

            return redirect(url_for('dashboard'))

        elif request.form.get('operation') == 'add_team':

            name = request.form.get('team_name')
            captain = request.form.get('captain_name')

            team = Team(name=name, captain=captain)

            db.addTeam(team)

            return redirect(url_for('dashboard'))

        elif request.form.get('operation') == 'delete_team':

            id = request.form.get('team_id')

            team = Team(id=id)

            db.deleteTeam(team)

            return redirect(url_for('dashboard'))

        
        elif request.form.get('operation') == 'add_player':

            name = request.form.get('player_name')
            team_id = request.form.get('team_id')

            player = Player(name=name, team_id=team_id)

            db.addPlayer(player)

            return redirect(url_for('dashboard'))

        elif request.form.get('operation') == 'delete_player':

            id = request.form.get('player_id')
            team_id = request.form.get('team_id')

            player = Player(id=id, team_id=team_id)

            db.deletePlayer(player)

            return redirect(url_for('dashboard'))


    return render_template("./admin/dashboard.html",title="Dash Board", matches=ad_matches)

@app.route("/dashboard/summary", methods=methods)
@login_required
def summary():

    if request.method == 'POST':

        match_id = request.form.get('match_id')
        team1_id = request.form.get('win_id')
        team2_id = request.form.get('lose_id')
        mom = request.form.get('man_of_match')

        draw = False

        if request.form.get('draw'):
            draw = True

        match = LastMatch(match_id, team1_id, team2_id, mom, draw)
        db.storeLastMatch(match)

        return redirect(url_for('dashboard'))


    return render_template("./admin/summary.html", title="Summary")

@app.route("/dashboard/playerStat", methods=methods)
@login_required
def playerStat():
    return render_template("./admin/playerStat.html", title="Stats")



@app.route("/dashboard/allTeams", methods=methods)
@login_required
def allTeamsAdm():

    ad_teams = db.ad_teams()    #./dashboard/allTeams

    return render_template("./admin/teams.html", title="Stats", teams=ad_teams)


@app.route("/dashboard/allPlayers", methods=methods)
@login_required
def allPlayers():

    ad_players = db.ad_players()    #./dashboard/allPlayers

    return render_template("./admin/allPlayers.html", title="Stats", players=ad_players)


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

    return render_template("./admin/login.html",title="Login admin", error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

# ----------------------------------------------------------------ROUTES END-----------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)