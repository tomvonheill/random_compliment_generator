import random
from flask import Flask, jsonify, abort
from database.models import db_drop_and_create_all,setup_db, Nouns, Adjectives, db


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    db_drop_and_create_all(app)

    def create_compliment(adjectives,noun):
        adjective_string = ', '.join(adjectives)
        return f"You are a {adjective_string} {noun}"
    
    @app.errorhandler(400)
    def questions_not_found(error):
        error_data = {
            'success' : False,
            'error' : 400,}
        error_data['message'] =error.description
        return jsonify(error_data),404

    @app.route('/compliment/<int:length>', methods = ['GET'])
    def compliment(length):
        adj_length = db.session.query(Adjectives.adjective).count()
        if length<1 or length>adj_length:
            abort(400, description = f'length should be between 1 and {adj_length}. A length of {length} was given')
        noun_length = db.session.query(Nouns.noun).count()


        compliment_adjectives = []
        for index in random.sample(range(1,adj_length+1),length):
            compliment_adjectives.append(db.session.query(Adjectives).get(index).adjective)
        random_noun = db.session.query(Nouns).get(random.randint(1,noun_length)).noun
        
        return jsonify({'success':True,'compliment':create_compliment(compliment_adjectives,random_noun)})
    return app

if __name__ == 'main':
    app = create_app()
    app.run()
