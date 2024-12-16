from flask import Flask, redirect , flash
from flask_login import LoginManager
from views.models import db, User
from views.config import SECRET_KEY, uri_db
from flask_migrate import Migrate
from flask_mail import Mail
import re 
# Create Flask application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')

# Initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = uri_db
db.init_app(app)

# Migrate 
migrate = Migrate(app, db)

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'dashboard.login_'  # Specify the login view endpoint

# Define the user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    # Retrieve the user object from the database based on the user_id
    return User.query.get(int(user_id))

# CSRF All Secrets Key for forms
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY

# Import Blueprints and Register them
from home import home 
from trans import trans
from galary import galary
from album import album
from dashboard import dashboard
from mailer import mailer

app.register_blueprint(home)
app.register_blueprint(trans)
app.register_blueprint(galary)
app.register_blueprint(album)
app.register_blueprint(dashboard)
app.register_blueprint(mailer)

# Import and configure models
from views.models import *

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mahmoudgalal55555@gmail.com'
app.config['MAIL_PASSWORD'] = 'dvynwttyjxcuuhfy'
app.config['MAIL_DEFAULT_SENDER'] = ('Mahmoud Galal', 'mahmoudgalal55555@gmail.com')

# Initialize Flask-Mail
mail = Mail(app)

# Ensure all models are imported and created
with app.app_context():
    db.create_all()

# Define a route to redirect to the home page
@app.route("/")
def get_home():
    return redirect("/home")


@app.template_filter('remove_br')
def remove_br(text):
    if text:
        return re.sub(r'<br\s*/?>', '', text)
    return text

# Register the filter with Jinja2
app.jinja_env.filters['remove_br'] = remove_br


# Run the application
if __name__ == '__main__':
    app.run(debug=True)