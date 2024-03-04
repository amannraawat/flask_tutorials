from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json', 'r') as file:
    params = json.load(file)['params']
    
local_server=True
app = Flask(__name__)
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
    
    
@app.route("/")
def home():
    return render_template('index.html', params=params)

@app.route("/about")
def about():
    return render_template('about.html')

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
    return render_template('contact.html', params=params)

@app.route("/post")
def post():
    return render_template('post.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)
