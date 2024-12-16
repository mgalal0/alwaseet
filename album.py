from flask import Blueprint, render_template, url_for
album = Blueprint("album", __name__, template_folder="templates")
from galary import *

#  home album ---------------------------------------
@album.route("/album")
def get_sec_album():
    # Pass the list of image filenames to the template
    return render_template("album.html", album1=sec_album_1 , album2 = sec_album_2 )

@album.route('/prim')
def get_prim():
    return render_template("primary.html")

# This function generates the URL for serving static files like images
@album.app_template_filter('static')
def static_filter(filename):
    return url_for('static', filename=filename)
