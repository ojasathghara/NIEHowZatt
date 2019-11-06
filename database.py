class Teams(db.Model):
    
    __tablename__ = 'teams'

    team_id = db.Column('team_id', db.Integer, primary_key=True)
    team_name = db.Column('team_name', db.String(20))
    team_captain = db.Column('team_captain', db.String(20))
    team_players = db.Column('team_players', db.Integer)

    def __repr__(self):
        return '<Member %r>' % self.team_name

class Schedule(db.Model):
    __tablename__ = 'schedule'

    match_id = db.Column('match_id', db.Integer, primary_key=True)
    team1_id = db.Column('team1_id', db.Integer)
    team2_id = db.Column('team2_id', db.Integer)
    team1_name = db.Column('team1_name', db.String(20))
    team2_name = db.Column('team2_name', db.String(20))

    def __repr__(self):
        return '<Member %r>' % self.match_id