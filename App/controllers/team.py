from App.database import db
from App.models.team import Team
from datetime import datetime, timedelta

def create_team(competitionId, adminId, teamName, score):
    team = Team(competitionId = competitionId, adminId = adminId, teamName = teamName, score = score)
    db.session.add(team)
    db.session.commit()
    return team

def get_team_by_id(id):
    return Team.query.get(id)

def update_team(id, teamName, score): 
    team = get_team_by_id(id)
    if team:
        if teamName:
            team.teamName = teamName
        if score:
            team.score = score
        db.session.add(team)
        db.session.commit()
        return team
    return None

def delete_team(id): 
    team = get_team_by_id(id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return True
    return False

def get_team_by_id_json(id):
    return get_team_by_id(id).to_json()

