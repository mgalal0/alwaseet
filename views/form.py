# Forms And Validations 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , FloatField ,FileField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email , InputRequired , ValidationError , EqualTo 
from views.models import User



class login(FlaskForm):
    email = StringField(label="email", validators=[DataRequired()])
    password = PasswordField()




# JOB REQUIRMENTS 
class JobRequirementForm(FlaskForm):
    job_name = StringField('Job Name', validators=[DataRequired(), Length(max=100)])
    salary = StringField('Salary', validators=[Length(max=50)])
    experience = StringField('Experience', validators=[Length(max=100)])
    education_level = StringField('Education Level', validators=[Length(max=100)])
    working_hours = StringField('Working Hours', validators=[Length(max=100)])
    job_title = StringField('Job Title', validators=[Length(max=100000)])
    gender = StringField('Gender', validators=[Length(max=8)])
    saudi_arabia_region = StringField('Saudi Arabia Region', validators=[Length(max=20)])
    job_skills = TextAreaField('Job Skills')

    photo = FileField('Photo')  # Add a FileField for photo upload

    def validate_job_skills(self, field):
        skills = field.data.split(',')
        if len(skills) > 10:
            raise ValidationError('You can only add up to 10 skills.')


class UserCreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email Address', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Create User')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
        


class UserEditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email Address', validators=[DataRequired(), Email(), Length(max=120)])
    new_password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm New Password', validators=[
        EqualTo('new_password', message='Passwords must match')
    ])
    submit = SubmitField('Update')        