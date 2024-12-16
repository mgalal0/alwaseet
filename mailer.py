from flask import Blueprint, render_template, request , flash
from flask_mail import Message
from flask_mail import Mail

mail = Mail()

mailer = Blueprint("mailer", __name__, template_folder="templates")



# Route for the contact form
@mailer.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Send email
        msg = Message(subject='AlWaseet : New message from contact us ',
                      recipients=['sales@alwaseet-cs.com'],
                      html=f'''
                          <html>
                          <head>
                              <style>
                                  body {{
                                      font-family: Arial, sans-serif;
                                      background-color: blue;
                                      padding: 20px;
                                  }}
                                  .container {{
                                      max-width: 600px;
                                      margin: 0 auto;
                                      background-color: white ;
                                      padding: 30px;
                                      border-radius: 10px;
                                      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                  }}
                                  h2 {{
                                      color: #333333;
                                  }}
                                  p {{
                                      color: #666666;
                                      line-height: 1.6;
                                  }}
                                  strong {{
                                      color: #000000;
                                  }}
                              </style>
                          </head>
                          <body>
                              <div class="container">
                                  <h2>New message from contact form</h2>
                                  <p><strong>Name:</strong> {name}</p>
                                  <p><strong>Email:</strong> {email}</p>
                                  <p><strong>Phone:</strong> {phone}</p>
                                  <p><strong>Message:</strong></p>
                                  <p>{message}</p>
                              </div>
                          </body>
                          </html>
                      ''')
        mail.send(msg)
        
        # Optionally, you can redirect the user to a thank you page
        return flash("Thank You")

    return render_template('contact-us.html')


