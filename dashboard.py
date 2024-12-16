from flask import Blueprint, render_template, redirect, request, jsonify, flash, url_for, session, send_from_directory
from flask_login import LoginManager, login_user, current_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import os
import re

from views.form import login, UserCreateForm, UserEditForm, JobRequirementForm
from views.models import User, JobRequirement, JobSkill
from app import db, app
dashboard = Blueprint("dashboard", __name__, template_folder="templates")
# Define upload folder
UPLOAD_FOLDER = 'static/Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize login manager
login_manager = LoginManager()
# User loader for login manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Set login view for login manager
login_manager.login_view = 'dashboard.login_'

# Route for user login
@dashboard.route('/login', methods=['GET', 'POST'])
def login_():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.admin'))

    form = login()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user:
            print(f"User found: {user.email}")
            if user.check_password(password):
                print("Password check passed")
                login_user(user)
                response_data = {
                    'status': 'success',
                    'message': 'Login Successful!'
                }
                return jsonify(response_data), 200
            else:
                print("Password check failed")
        else:
            print("User not found")

        response_data = {
            'status': 'error',
            'message': 'Invalid email or password. Please try again.'
        }
        return jsonify(response_data), 400

    print("Form validation failed")
    return render_template("dashboard/login.html", form=form)


    
# Route to show all jobs
@dashboard.route('/admin-jobs')
@login_required
def show_jobs():
    jobs = JobRequirement.query.all()
    return render_template('dashboard/jobs.html',  jobs=jobs)





@dashboard.route('/admin')
@login_required
def admin():
    if current_user.is_authenticated:
        # Fetch all jobs
        jobs = JobRequirement.query.all()
        # Render the admin dashboard template with jobs
        return render_template('dashboard/admin.html', jobs=jobs )
    else:
        response_data = {
            'status': 'error',
            'message': 'You need to log in as an admin first.'
        }
        return jsonify(response_data), 401


# Route to create a new admin
@dashboard.route('/create_user', methods=['POST'])
@login_required 
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            return jsonify({'message': 'Missing required parameters.'}), 400

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists with that email.'}), 409

        # Create a new user
        new_user = User(name=name, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully.'}), 201

    return jsonify({'message': 'Invalid request method.'}), 405


# Route to show all users ( Admins )
@dashboard.route("/admins")
@login_required
def show_users():
    all_users = User.query.all()
    response = session.pop('response', None)  # Get response message from session
    return render_template("dashboard/admins.html", users=all_users, response=response)

# Route to edit user information
@dashboard.route("/admins/<int:user_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserEditForm(obj=user)
    
    print(f"Request method: {request.method}")
    if form.validate_on_submit():
        print("Form validated")
        user.name = form.name.data
        user.email = form.email.data

        if form.new_password.data:  # Check if new password is provided
            user.set_password(form.new_password.data)  # Use a method to set hashed password
            print(f"New password set for user {user.id}: {user.password}")

        db.session.commit()
        print(f"User {user.id} updated successfully")
        session['response'] = "User updated successfully."
        return redirect(url_for('dashboard.show_users'))
    
    return render_template("dashboard/edit_user.html", form=form, user=user)



# Route to delete a user
@dashboard.route("/users/<int:user_id>/delete", methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    session['response'] = "User deleted successfully."
    return redirect(url_for('dashboard.show_users'))  # Corrected redirect URL



# Route to log out
@dashboard.route("/logout")
def logout():
    # Clear the user's session data
    session.clear()
    # Redirect the user to the home page or any other desired page
    return redirect(url_for('dashboard.login_'))

# Route to create a new job
@dashboard.route('/create_job', methods=['GET', 'POST'])
@login_required
def create_job():
    form = JobRequirementForm()

    if form.validate_on_submit():
        job_name = form.job_name.data
        salary = form.salary.data
        experience = form.experience.data
        education_level = form.education_level.data
        working_hours = form.working_hours.data
        job_description = form.job_title.data.replace("\n", "<br>")  # Preserve line breaks for HTML
        gender = form.gender.data
        saudi_arabia_region = form.saudi_arabia_region.data
        job_skills = form.job_skills.data
        photo = form.photo.data

        # Handle file upload
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            photo_path = None

        # Create job requirement instance
        new_job = JobRequirement(
            job_name=job_name,
            salary=salary,
            experience=experience,
            education_level=education_level,
            working_hours=working_hours,
            job_title=job_description,
            gender=gender,
            saudi_arabia_region=saudi_arabia_region,
            photo=photo_path
        )

        # Add job skills (if any)
        if job_skills:
            skills = job_skills.split('\n')  # Split the input by newline to get individual skills
            for skill in skills:
                new_job_skill = JobSkill(skill_text=skill.strip())
                new_job.job_skills.append(new_job_skill)

        # Commit to the database
        db.session.add(new_job)
        db.session.commit()

        flash("Job created successfully.", 'success')
        return redirect(url_for('dashboard.admin'))  # Redirect to the same page after successful job creation

    return render_template("dashboard/create_job.html", form=form)




# Route to delete a job
@dashboard.route('/admin-jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def delete_job(job_id):
    job = JobRequirement.query.get_or_404(job_id)

    # Delete related JobSkill records
    JobSkill.query.filter_by(job_requirement_id=job.id).delete()

    # Delete the job
    db.session.delete(job)
    db.session.commit()

    flash("Job deleted successfully.", 'success')
    return redirect(url_for('dashboard.admin'))


# Route to show job details
@dashboard.route('/job_details/<int:job_id>')
@login_required
def show_job_details(job_id):
    job = JobRequirement.query.get_or_404(job_id)
    return render_template("dashboard/more-info.html", job=job)



# Route to serve uploaded files
@dashboard.route('/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)




