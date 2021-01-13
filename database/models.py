import os
from sqlalchemy import Column, String, Integer, Boolean
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all(app):
    db.drop_all()
    db.create_all()
    fill_db(app)

def get_word_data():
    word_data = []
    with open('adjectives.json') as f:  
        word_data= json.load(f)
    return word_data

def fill_db(app):
    word_data = get_word_data()
    with app.app_context():
        #load adjectives
        adj_objects = [Adjectives(adjective=adjective)for adjective in word_data['positive_adjectives']]
        db.session.add_all(adj_objects)
        #load nouns
        noun_objects = [Nouns(noun = noun) for noun in word_data['positive_nouns']]
        db.session.add_all(noun_objects)
        db.session.commit()
        

class Adjectives(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    adjective = Column(String(80), unique=True)

    def __repr__(self):
        return f'{self.adjective}'

class Nouns(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    noun = Column(String(80), unique=True)

    def __repr__(self):
        return f'{self.noun}'