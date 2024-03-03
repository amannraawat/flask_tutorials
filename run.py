from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/about")
def about():
    nam = "About"
    return render_template('about.html', name=nam)

if __name__ == '__main__':
    app.run(debug=True)
