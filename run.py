from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/thedailyblog"
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
    return render_template('index.html')

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
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
