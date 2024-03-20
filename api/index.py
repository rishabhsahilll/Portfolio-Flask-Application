'''
Name:- Portfolio
Developer:- RISHABH KUMAR
Version:- 3.24.8
'''

from flask import Flask, render_template, request
from flask_mail import Mail, Message
# from dotenv import load_dotenv
import json
import os
import requests

app = Flask(__name__)

# Json Files Path
about_file_path = os.path.join(os.path.dirname(__file__), 'about.json')
resume_file_path = os.path.join(os.path.dirname(__file__), 'resume.json')
portfolio_file_path = os.path.join(os.path.dirname(__file__), 'portfolio.json')
blog_file_path = os.path.join(os.path.dirname(__file__), 'blog.json')

# Load About Json File
with open(file=about_file_path) as f:
    data = json.load(f)

def get_gender_from_name(name):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url)
    data = response.json()

    if "gender" in data:
        return data["gender"]
    else:
        return "Unknown"

@app.route('/')
def about():
    style = {
        "content_active_btn":  "active"
    }
    return render_template('about.html',data=data,style=style)

@app.route('/resume')
def resume():
    # Load Resume Json File
    with open(file=resume_file_path) as f:
        resume_data = json.load(f)

    style = {
        "content_active_btn":  "active"
    }
    return render_template('resume.html',data=data,style=style,resume_data=resume_data)

@app.route('/portfolio')
def portfolio():
    # Load Portfolio Json File
    with open(file=portfolio_file_path) as f:
        portfolio_data = json.load(f)

    style = {
        "content_active_btn":  "active"
    }
    return render_template('portfolio.html',data=data,style=style,portfolio_data=portfolio_data)

@app.route('/blog')
def blog():
    # Load Blog Json File
    with open(file=blog_file_path) as f:
        blog_data = json.load(f)
        
    style = {
        "content_active_btn":  "active"
    }
    return render_template('blog.html',data=data,style=style,blog_data=blog_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    style = {
        "content_active_btn":  "active"
    }
    if request.method == 'POST':
        fullname = request.form['fullname']
        user_email = request.form['email']
        message = request.form['message']
        
        firts_and_last_name = str(fullname).split()

        firts_name = firts_and_last_name[0]

        if get_gender_from_name(fullname)=='male':
            firts_name = f"Hello, Mr. {firts_name.capitalize()}"
        elif get_gender_from_name(firts_name)=='female':
           firts_name = f"Hello, Mrs. {firts_name.capitalize()}"
        else:
            firts_name = f"Hello, {fullname.capitalize()}"

        # Configuration for Flask-Mail
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
        app.config['MAIL_PORT'] = 587  # Replace with your SMTP port (e.g., 587 for TLS)
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Replace with your email address
        app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Replace with your email password
        app.config['MAIL_DEBUG'] = True
        
        mail = Mail(app)
        
        # Sende Mesage On Email
        msg = Message(subject='New Contact Form Submission: Inquiry from Portfolio - Rishabh Kumar ',
                    sender=os.getenv('MAIL_USERNAME'),  # Replace with your email address
                    recipients=[user_email])  # Replace with recipient's email address

        # Set the body of the email
        msg.html = f'''
            <H2><b>{firts_name}</b></H2>,

            <H3>You have received a new contact form submission from Portfolio. Here is the summary:</H3>

            <H4>
            Name: {fullname}<br>
            Email: {user_email}<br>
            Message: {message}
            </H4>

            Please take necessary action or respond accordingly.<br>

            Thank you for reaching out!<br><br>

            Best Regards,<br>
            <a href="https://bento.me/sahill-ray">RISHABH</a> <a href="https://bento.me/sahill-ray"> SAHIL</a><br>
            <a href="https://github.com/rishabhsahilll">RSE</a><br>
            Instagram ID: <a href="https://instagram.com/ll._rsy_.ll/">@ll._rsy_.ll</a><br>
        '''

        # Send the email
        mail.send(msg)
        # print("Email sent successfully!")
        return render_template('contact.html',data=data,style=style)
    
    # If it's a GET request, simply render the contact form template
    return render_template('contact.html',data=data,style=style)
