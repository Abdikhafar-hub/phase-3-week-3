from flask import Flask
from flask_migrate import Migrate
from models import db, Band, Venue, Concert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concerts.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Welcome to the Concerts API!'

if __name__ == '__main__':
    app.run(debug=True)
