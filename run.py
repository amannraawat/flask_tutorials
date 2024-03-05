from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail

with open('config.json', 'r') as file:
    params = json.load(file)['params']
    
local_server=True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/thedailyblog"
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(13), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=True)
    
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    tagline = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(150), nullable=False)
    posted_by = db.Column(db.String(20), nullable=False)
    posted_on = db.Column(db.String(10), nullable=True)
    slug = db.Column(db.String(20), nullable=False)
    image_name = db.Column(db.String(10), nullable=True)
    
    
@app.route("/")
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html', params=params, posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)
    

@app.route("/contact", methods =['GET', 'POST'])
def contact():
    if (request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        entry = Contacts(name=name, email=email, phone_num = phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail_user']],
                          body=message+"\n"+phone
                           )        
    return render_template('contact.html', params=params)

# @app.route("/post")
# def post():
#     return render_template('post.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)
