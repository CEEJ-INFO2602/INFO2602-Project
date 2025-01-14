from App.database import db
from datetime import datetime

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adminId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    compName = db.Column(db.String(120), nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    teams = db.relationship("Team", backref="competition", lazy=True, cascade = "all, delete-orphan")

    def __init__(self, adminId, compName, startDate, endDate):
        self.adminId = adminId
        self.compName = compName
        self.startDate = startDate
        self.endDate = endDate
        #self.teams = teams
        
    def to_json(self):
        return{
            "id": self.id,
            "adminId": self.adminId,
            "compName": self.compName,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "teams": [team.to_json() for team in self.teams],
        }