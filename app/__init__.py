from flask import Flask, render_template
from app.db import db

# intializing app
app = Flask(__name__)

# configuring app for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

# initializing database
db.init_app(app)

with app.app_context():
	db.create_all()

# home route
@app.route('/')
def index():
	return "render_template('home.html')"

# blog routes

# user routes

# deploying developement server
if __name__=='__main__':
	app.run(debug=True)