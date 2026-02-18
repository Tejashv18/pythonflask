from flask import Flask, render_template
app = Flask(__name__)

posts=[
    {
        'author':'Tejas H V',
        'Title':'Blog not yet stated',
        'content':'first started to exceute',
        'date_started':'feb 18 2026'
    },
    {
        'author':'mahesh',
        'Title':'Blog  started',
        'content':'first started to exceute',
        'date_started':'feb 17 2026'
    }
]
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html',title='about')


if __name__ == "__main__":
    app.run(debug=True)