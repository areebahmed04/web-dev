from flask import Flask, request, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class info(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    reponame = db.Column(db.String(100))

    def __init__(self, name, repo):
        self.username = name
        self.reponame = repo
#comment
#newcomment
def get_db():

    if 'db' not in g:
        db.create_all()

    return g.db


@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/')
def show_all():
   return render_template('index.html', posts = info.query.all() )


@app.route('/new', methods=['GET', 'POST'])
def new():

    if request.method == 'POST':

        u = info(request.form['name'], request.form['repo'])

        db.session.add(u)
        db.session.commit()

        flash('Record was successfully added')
        return redirect(url_for('index.html'))

    return render_template('new.html')


if __name__ == '__main__':

    db.create_all()
    app.run(debug=True)