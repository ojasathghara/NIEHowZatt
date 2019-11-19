import pymysql as sql
import random

class Match():
    match_id = 0
    team1_id = 0
    team2_id = 0
    team1_name = ""
    team2_name = ""
    date = ""

    def __init__(self, match_id=0, team1_id=0, team2_id=0, date=""):
        self.match_id = match_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.date = date

class Team():
    id = 0
    name = ""
    captain = ""
    
    matches = 0,
    wins = 0,
    lose = 0,
    draw = 0,
    points = 0

    def __init__(self, id=0, name="", captain=""):
        self.id = id
        self.name = name
        self.captain = captain

class Player ():
   
    id = 0
    team_id = 0
    name = ""
    team_name = ""
    
    sc_runs = 0
    pl_balls = 0
    st_rate = 0
    
    th_balls = 0
    gv_runs = 0
    wickets = 0

    def __init__(self, id=0, name="", team_id=""):
        self.id = id
        self.name = name
        self.team_id = team_id        


class Database():
    host = ""
    user = ""
    passwd = ""
    db = ""
    con = ''
    cur = ''

    def __init__(self, host="localhost", user="root", passwd="Ojaswi825#", db="ctms"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

        self.con = sql.connect(host=host, user=user, password=passwd, db=db, use_unicode=True, charset='utf8')
        self.cur = self.con.cursor()

    def addTeam(self, team):

        insertTeamString = f"""insert into teams(name, captain) values("{team.name}", "{team.captain}");"""
        self.cur.execute(insertTeamString)
        self.con.commit()

    def deleteTeam(self, team):

        deleteTeamString = f"""delete from teams where id = {team.id};"""
        self.cur.execute(deleteTeamString)
        self.con.commit()

    def addPlayer(self, player):

        getTeamString = f"select name from teams where id = {player.team_id};"
        self.cur.execute(getTeamString)        
        teamNameTuple = self.cur.fetchall()
        teamName =teamNameTuple[0][0]

        addPlayerString = f"""insert into players(name, team_id, team_name) values("{player.name}", {player.team_id}, "{teamName}");"""
        self.cur.execute(addPlayerString)
        self.con.commit()

    def deletePlayer(self, player):

        deletePlayerString = f"""delete from players where id = {player.id} and team_id = {player.team_id};"""
        self.cur.execute(deletePlayerString)
        self.con.commit()

    def addMatch(self, match):

        getTeam1String = f"select name from teams where id = {match.team1_id};"
        self.cur.execute(getTeam1String)
        team1Tuple = self.cur.fetchall()
        team1Name = team1Tuple[0][0]

        getTeam2String = f"select name from teams where id = {match.team2_id};"
        self.cur.execute(getTeam2String)
        team2Tuple = self.cur.fetchall()
        team2Name = team2Tuple[0][0]

        addMatchString = f"""insert into matches(team1_id, team2_id, team1_name, team2_name, date) values({match.team1_id}, {match.team2_id}, "{team1Name}", "{team2Name}", "{match.date}");"""
        self.cur.execute(addMatchString)
        self.con.commit()

    def deleteMatch(self, match):

        deleteMatchString = f"delete from matches where match_id = {match.match_id};"
        self.cur.execute(deleteMatchString)
        self.con.commit()

    def topTeams(self): #home

        topTeamsString = "select * from topTeams;"
        self.cur.execute(topTeamsString)
        teams = self.cur.fetchall()

        return teams

    def homeMatches(self):  #home

        homeMatchesString = "select * from homeMatches;"
        self.cur.execute(homeMatchesString)
        matches = self.cur.fetchall()

        return matches

    def fullMatches(self):  #./schedule

        fullMatchesString = "select * from fullMatches;"
        self.cur.execute(fullMatchesString)
        matches = self.cur.fetchall()

        return matches

    def points(self):   #./points

        pointsString = "select * from points;"
        self.cur.execute(pointsString)
        point = self.cur.fetchall()

        return point

    def allTeams(self): #./points
        
        teamString = "select name, captain from teams;"
        self.cur.execute(teamString)
        teams = self.cur.fetchall()

        return teams

    def indieTeam(self, teamName):

        teamDetailString = f'select name, captain, matches, points from teams where name="{teamName}";'
        self.cur.execute(teamDetailString)
        teamDetail = self.cur.fetchall()

        team = {
            'name': teamDetail[0][0],
            'captain': teamDetail[0][1],
            'matches': teamDetail[0][2],
            'points': teamDetail[0][3]
        }

        playersString = f'select name, sc_runs, pl_balls, st_rate, th_balls, gv_runs, wickets from players where team_name="{teamName}";'
        self.cur.execute(playersString)
        players = self.cur.fetchall()

        l = [team, players]

        return l

    def ad_matches(self):   #-Dashboard schedule
        
        ad_matchesString = "select * from ad_matches;"
        self.cur.execute(ad_matchesString)
        match = self.cur.fetchall()

        return match

    def ad_teams(self): #dashboard/allTeams

        ad_teamsString = "select * from ad_teams;"
        self.cur.execute(ad_teamsString)
        teams = self.cur.fetchall()

        return teams

    def ad_players(self):   #dashboard/allPlayers

        ad_playersString = "select * from ad_players;"
        self.cur.execute(ad_playersString)
        players = self.cur.fetchall()

        return players

    
if __name__ == "__main__":
   
   db = Database()

   for i in range (1, 11):
       t1 = random.randint(1, 8)
       t2 = random.randint(1, 8)

       match = Match(team1_id=t1, team2_id=t2, date="26/10/2019")

       db.addMatch(match)