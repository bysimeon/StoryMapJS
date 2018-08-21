from flask_alchemy import SQLAlchemy
from ____ import db

class users(db.model):
    contents = db.Column(JSON)
