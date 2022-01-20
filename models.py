from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Pet model"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False, unique = True)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, default = 'https://www.oseyo.co.uk/wp-content/uploads/2020/05/empty-profile-picture-png-2-2.png')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default = True)

