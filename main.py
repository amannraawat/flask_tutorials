from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
import os, math
from werkzeug.utils import secure_filename

with open('config.json', 'r') as file:
    params = json.load(file)['params']
    
local_server=True
app = Flask(__name__, instance_path='C:/Users/hp/Desktop/flask_tut/instance/')
app.secret_key = 'super secret key'
# app.config['UPLOAD_FOLDER'] = params['uploader_location']

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
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1) * int(params['no_of_posts']) : (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    
    #pagination
    if (page==1):
        prev = '#'
        next = "/?page=" + str(page+1)
    elif (page==last):
        prev = "/?page=" + str(page-1)
        next = '#'
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)
        
    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/dashboard", methods=['GET', 'POST'])
def admin_login():
    if ('user' in session and session['user']==params['admin_username']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    
    
    if request.method == 'POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if (username ==params['admin_username'] and userpass == params['admin_password']):
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        
    else:
        return render_template('login.html', params=params)
    
@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user']==params['admin_username']):
        if request.method=='POST':
            title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            posted_by = request.form.get('posted_by')
            posted_on = datetime.now()
            img_file = request.form.get('img_file')
           
            if sno=='0':
                post = Posts(title=title, tagline=tline, slug=slug, content=content, posted_by=posted_by, posted_on = posted_on, image_name=img_file)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tline
                post.slug = slug
                post.content = content
                post.posted_by = posted_by
                post.posted_on = posted_on
                post.image_name = img_file
                
                db.session.commit()
                return redirect('/edit/' + sno)
        
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)
        
    

@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method=='POST':
            fil = request.files['file1']
            os.makedirs(os.path.join(app.instance_path, 'file1'), exist_ok=True)
            fil.save(os.path.join(app.instance_path,'file1', secure_filename(fil.filename) ))
            return "Upload Successfully"    
        
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route('/delete/<string:sno>')
def delete(sno):
    if ('user' in session and session['user'] == params['admin_username']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        
    return redirect('/dashboard')

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

if __name__ == '__main__':
    app.run(debug=True)