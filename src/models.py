# models.py
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()


class County(db.Model):
    __tablename__ = "county"

    Index = db.Column(db.Integer)
    County = db.Column(db.String, primary_key=True)
    Count = db.Column(db.Integer)

    def __repr__(self):
        return "<County %r>" % (self.Index)


class Offender(db.Model):
    __tablename__ = "offender"

    Index = db.Column(db.Integer)
    Execution = db.Column(db.Integer, primary_key=True)
    Link = db.Column(db.String)
    Last_Name = db.Column(db.String)
    First_Name = db.Column(db.String)
    TDCJ = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Date = db.Column(db.Date)
    Race = db.Column(db.String)
    County = db.Column(db.String)

    def __repr__(self):
        return "<Offender %r>" % (self.Index)


class Words(db.Model):
    __tablename__ = "words"

    Index = db.Column(db.Integer, primary_key=True)
    Most_Spoken_Words = db.Column(db.String)
    Count_of_Words = db.Column(db.Integer)

    def __repr__(self):
        return "<Words %r>" % (self.Index)
