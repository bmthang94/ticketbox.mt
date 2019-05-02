from flask import Blueprint, render_template, request, redirect, url_for, flash
from src import db, app
from src.models.user import User
from src.models.userForm import signIn, signUp, EmailForm, PasswordForm
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user, login_url
import requests
from itsdangerous import URLSafeTimedSerializer

events_blueprint = Blueprint('/',
                             __name__,
                             template_folder='../../templates/home')

LoginManager = LoginManager(app)
LoginManager.login_view = 'signin'
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


@LoginManager.user_loader
def load_user(id):
    return User.query.get(int(id))


@events_blueprint.route('/')
def homepage():
    return render_template('home.html')


@events_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    signInForm = signIn()
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        user = User.query.filter_by(email=user_email).first()
        if(user is not None and user.check_password(user_password)):
            # flash('Hi! ' + user.username, 'alert-success')
            print(user.username)
            login_user(user)
            return redirect(url_for('/.homepage'))
        else:
            flash('Wrong Email/Password', 'alert-danger')
    return render_template('signin.html', form=signInForm)


@events_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    signUpForm = signUp()
    if request.method == 'POST':
        username = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        user = User(username=username, email=user_email)
        user.set_password(user_password)
        db.session.add(user)
        db.session.commit()
        if user is not None:
            return redirect(url_for('/.homepage'))
    return render_template('signup.html', form=signUpForm)


@events_blueprint.route('/signout')
@login_required
def signout():
    logout_user()
    flash('Logout success', 'alert-success')
    return redirect(url_for('/.homepage'))


@events_blueprint.route('/reset', methods=['GET', 'POST'])
def reset():
    emailform = EmailForm()
    if request.method == 'POST' and emailform.validate_on_submit():
        user_email = request.form['email']
        user = User.query.filter_by(email=user_email).first_or_404()
        if user is not None:
            token = ts.dumps(user.email, salt='recover-password-secret-10794')
            user.send_password_reset_email(token)
    return render_template('reset.html', form=emailform)


@events_blueprint.route('/new_password/<token>', methods=['GET', 'POST'])
def new_password(token):
    form = PasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            email = ts.loads(token, salt='recover-password-secret-10794', max_age=3600)
        except:
            flash('The password reset link is invalid or has expired.', 'error')
            return redirect(url_for('/.signin'))
        user_password = request.form['password']
        user = User.query.filter_by(email=email).first_or_404()
        if user is not None:
            user.set_password(user_password)
            db.session.commit()
            return redirect(url_for('/.homepage'))
    return render_template('new_password.html', form=form)
