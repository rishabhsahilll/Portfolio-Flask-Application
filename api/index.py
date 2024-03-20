'''
Name:- Portfolio
Developer:- RISHABH KUMAR
Version:- 3.24.5
'''

from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Json Files Path
about_file_path = os.path.join(os.path.dirname(__file__), 'about.json')
resume_file_path = os.path.join(os.path.dirname(__file__), 'resume.json')
portfolio_file_path = os.path.join(os.path.dirname(__file__), 'portfolio.json')
blog_file_path = os.path.join(os.path.dirname(__file__), 'blog.json')

# Load About Json File
with open(file=about_file_path) as f:
    data = json.load(f)

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
        email = request.form['email']
        message = request.form['message']
        
        # Here, you can process the data as needed, such as sending an email, saving to a database, etc.
        # For example, you could print the data to the console:
        print(f"Full Name: {fullname}, Email: {email}, Message: {message}")
        
        # Redirect to a thank you page or display a confirmation message
        return "Thank you for your message!"
    
    # If it's a GET request, simply render the contact form template
    return render_template('contact.html',data=data,style=style)

# if __name__ == '__main__':
#     app.run(debug=True)
