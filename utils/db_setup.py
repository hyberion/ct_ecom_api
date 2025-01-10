from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def setup_db(app):
    """
    Configures and initializes the database and Marshmallow with the Flask app.
    """
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind SQLAlchemy and Marshmallow to the Flask app
    db.init_app(app)
    ma.init_app(app)

    # Create all tables in the database
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
