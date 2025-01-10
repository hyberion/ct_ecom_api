from flask import Flask
from models import db, User, Order, Product, OrderProduct
from schemas import ma
from utils.db_setup import setup_db
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sqluser:letmein1969@localhost:3306/flask_api_project_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

#Removed this because we added flask_migrate but kept here because of emtional attachment.
#with app.app_context():
#    db.create_all()


# Import routes
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.order_routes import order_bp

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(order_bp, url_prefix='/orders')

#Register Flask CLI Commands
from flask.cli import with_appcontext
import click

@click.command(name="db_create_all")
@with_appcontext
def db_create_all():
    db.create_all()
    print("Tables created!")

# Register the command for development environments
app.cli.add_command(db_create_all)

if __name__ == '__main__':
    app.run(debug=True)



