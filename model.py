from flask import Flask, request, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    reponame = db.Column(db.String(100))


@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/')
def show_all():
   return render_template('show_all.html', posts = User.query.all() )


@app.route('/new', methods=['GET', 'POST'])
def new():

    if request.method == 'POST':

        u = User(request.form['name'], request.form['repo'])

        db.session.add(u)
        db.session.commit()

        flash('Record was successfully added')
        return redirect(url_for('show_all'))

    return render_template('new.html')


if __name__ == '__main__':

    # db.create_all()
    # user1 = User(username='abc', reponame='repo1')
    # db.session.add(user1)
    # db.session.commit()
    # print("SSS", User.query.all())
    app.run(debug=True)