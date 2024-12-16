from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        print(f"Password set for user {self.id}: {self.password}")


class JobRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50))
    experience = db.Column(db.String(100))
    education_level = db.Column(db.String(100))
    working_hours = db.Column(db.String(100))
    job_title = db.Column(db.String(10000))
    gender = db.Column(db.String(8))
    saudi_arabia_region = db.Column(db.String(20))
    job_skills = db.relationship('JobSkill', backref='job_requirement', lazy=True)
    photo = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class JobSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_text = db.Column(db.String(255), nullable=False)
    job_requirement_id = db.Column(db.Integer, db.ForeignKey('job_requirement.id'), nullable=False)
    





    



