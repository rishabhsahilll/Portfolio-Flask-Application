from flask import Flask, render_template, request
import json


app = Flask(__name__)

# Load About Json File
with open('about.json') as f:
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
    with open('resume.json') as f:
        resume_data = json.load(f)

    style = {
        "content_active_btn":  "active"
    }
    return render_template('resume.html',data=data,style=style,resume_data=resume_data)

@app.route('/portfolio')
def portfolio():
    # Load Portfolio Json File
    with open('portfolio.json') as f:
        portfolio_data = json.load(f)

    style = {
        "content_active_btn":  "active"
    }
    return render_template('portfolio.html',data=data,style=style,portfolio_data=portfolio_data)

@app.route('/blog')
def blog():
    # Load Blog Json File
    with open('blog.json') as f:
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
