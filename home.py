# home.py
from flask import Blueprint, render_template, redirect, request, make_response , flash
from trans import *
home = Blueprint("home", __name__, template_folder="templates")
from galary import *
from album import *
from views.form import JobRequirementForm
from views.models import User, JobRequirement, JobSkill
from flask_mail import Message, Mail
import re



@home.route("/")
def root():
    return redirect("/home")

@home.route("/None")
def get_none():
    return redirect ("/home")
#   page_title = page_titles.get('/home')
# home page -------------------------------------------------------------------------
@home.route("/home")
def home_page():
    lang = request.cookies.get("lang")
    if not lang or lang not in translations:  # Default to English if language is not set or invalid
        lang = "en"
        response = make_response(redirect(request.referrer))
        response.set_cookie("lang", lang)
        return response

 
    return render_template("index.html",  translations_galary=translations_galary , meta_tag= meta_tags ,
                        page_title = page_titles.get('/home') ,
    translations=translations[lang], image_filenames=image_filenames, album1=album1_images, album2=album2_images , our_logos= logos)
# 1-security-service-page -----------------
@home.route("/security")
def get_sec():
        
        lang = request.cookies.get("lang")
        if not lang or lang not in translations: 
             # Default to English if language is not set or invalid
             lang = "en"
             response = make_response(redirect(request.referrer))
             response.set_cookie("lang", lang)
             return response
        return render_template("secuirty.html" ,translations_galary=translations_galary2, image_filenames=image_filenames2 ,
         translations=translations[lang],album1=sec_album_1, album2=sec_album_2 , banner_info=banner_info.get('/security')  ,
          sliders_info = sliders_info.get('/security') , 
           page_title = page_titles.get('/security') )
         



# 2-crowd-services-page  ----------------------
@home.route("/crowd")
def get_crowd():
        lang = request.cookies.get("lang")
        if not lang or lang not in translations: 
             # Default to English if language is not set or invalid
             lang = "en"
             response = make_response(redirect(request.referrer))
             response.set_cookie("lang", lang)
             return response
        return render_template("crowd.html" ,translations_galary=translations_galary3   , image_filenames=image_filenames3 ,
         translations=translations[lang],album1=crowd_album_1, album2=crowd_album_2 , banner_info=banner_info.get('/crowd')  ,
          sliders_info = sliders_info.get('/crowd') ,
           page_title = page_titles.get('/crowd')  )

#  ,translations_galary=translations_galary2, translations=translations[lang],album1=crowd_album_1, album2=crowd_album_2 ,
#           banner_info=banner_info.get('/crowd')  ,  sliders_info = sliders_info.get('/crowd')

# 3-valet-&-car-parking-services-page  ----------------------
@home.route("/valet")
def get_valet():
        
        lang = request.cookies.get("lang")
        if not lang or lang not in translations: 
             # Default to English if language is not set or invalid
             lang = "en"
             response = make_response(redirect(request.referrer))
             response.set_cookie("lang", lang)
             return response
        return render_template("valet.html" ,translations_galary=translations_galary4, translations=translations[lang],album1=valet_album_1, album2=valet_album_2,
       banner_info=banner_info.get('/valet') , sliders_info = sliders_info.get('/valet') , image_filenames=image_filenames4 ,
        page_title = page_titles.get('/valet')  )   

# 4-car-wash-services----------------------------------------------------------
@home.route("/car-wash")
def get_car_wash():
        
        lang = request.cookies.get("lang")
        if not lang or lang not in translations: 
             # Default to English if language is not set or invalid
             lang = "en"
             response = make_response(redirect(request.referrer))
             response.set_cookie("lang", lang)
             return response
        return render_template("car-wash.html" ,translations_galary=translations_galary5, translations=translations[lang],album1=car_wash_album_1, album2=car_wash_album_2,
        banner_info=banner_info.get('/car-wash') , sliders_info = sliders_info.get('/car-wash') , image_filenames=image_filenames5 ,
         page_title = page_titles.get('/car-wash') )





@home.route("/change_language", methods=["POST"])
def change_language():
    lang = request.form.get("lang")
    if lang not in translations:  # Default to English if language is not valid
        lang = "en"
    response = make_response(redirect(request.referrer))
    response.set_cookie('lang', lang)
    return response



# jobs page ------------------------
@home.route("/jobs")
def get_jobs():
      
     
     lang = request.cookies.get("lang")
     if not lang or lang not in translations:  # Default to English if language is not set or invalid
        lang = "en"
        response = make_response(redirect(request.referrer))
        response.set_cookie("lang", lang)
        return response
     jobs = JobRequirement.query.all()



     return render_template ("jobs.html",translations=translations[lang] , jobs=jobs , page_title = page_titles.get('/jobs') )  


# job-details route
@home.route("/job_details/<int:job_id>", methods=['GET', 'POST'])
def get_job_details(job_id):
    lang = request.cookies.get("lang")
    if not lang or lang not in translations:
        lang = "en"
        response = make_response(redirect(request.referrer))
        response.set_cookie("lang", lang)
        return response

    job = JobRequirement.query.get_or_404(job_id)
    mail = Mail()

    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            gender = request.form.get('gender')
            date_of_birth = request.form.get('date_of_birth')
            nationality = request.form.get('nationality')
            country = request.form.get('country')
            years_of_experience = request.form.get('years_of_experience')
            education_level = request.form.get('education_level')
            email = request.form.get('email')
            contact_number = request.form.get('contact_number')
            
            # Handle file upload
            cv = request.files['cv']
            
            # Send email
            msg = Message(subject='AlWaseet : Job Submisson',
                          recipients=['your_email@example.com'],
                          body=f'''
                              First Name: {first_name}
                              Last Name: {last_name}
                              Gender: {gender}
                              Date of Birth: {date_of_birth}
                              Nationality: {nationality}
                              Country: {country}
                              Years of Experience: {years_of_experience}
                              Education Level: {education_level}
                              Email: {email}
                              Contact Number: {contact_number}
                          ''')
            msg.attach(filename=cv.filename, content_type=cv.content_type, data=cv.read())
            mail.send(msg)
            
            flash("Your information has been submitted successfully. We will contact you soon.", 'success')
            return redirect(url_for('home.get_job_details', job_id=job.id))
        except Exception as e:
            flash(f"An error occurred: {e}", 'danger')

    return render_template("job-details.html", translations=translations[lang], job=job  )




@home.route("/contact-us")
def get_contact_us():
     lang = request.cookies.get("lang")
     if not lang or lang not in translations:  # Default to English if language is not set or invalid
        lang = "en"
        response = make_response(redirect(request.referrer))
        response.set_cookie("lang", lang)
        return response
     return render_template ("contact-us.html",translations=translations[lang] , page_title = page_titles.get('/contact-us'))  


