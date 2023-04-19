from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
db = SQLAlchemy()

class Competition(db.Model):
    compCode = db.Column(db.Integer, primary_key=True)
    #create a new realationship with the Team table
    #teamId = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    adminId = db.Column(db.Integer, db.ForeignKey('admin_user.id'), nullable=False)
    compName = db.Column(db.String(120), nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    teams = db.relationship("Team", backref="competition", lazy=True)

    def __init__(self, adminId, compName, startDate, endDate):
        self.adminId = adminId
        self.compName = compName
        self.startDate = startDate
        self.endDate = endDate
# add in others
    def get_json(self):
        return{
            "compCode": self.compCode,
            "compName": self.compName,
            "startDate": self.startDate,
            "endDate": self.endDate,
        }