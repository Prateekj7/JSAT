from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Path: app\models.py
# from app import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}')"

# # Path: app\main.py
# from app import app
# from app.models import User

# @app.route('/')
# def index():
#     user = User.query.filter_by(name='John').first()
#     return user.email

# if __name__ == '__main__':
#     app.run(debug=True)

# # Path: app\run.py
# from app import app

# if __name__ == '__main__':
#     app.run(debug=True)
    
