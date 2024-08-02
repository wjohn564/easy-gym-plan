from flask import Blueprint, render_template, redirect, url_for

from auth_forms import AuthenticationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = AuthenticationForm()
    if form.validate_on_submit():
        # Handle signup logic here
        return redirect(url_for('main.home'))
    return render_template('signup.html', form=form)
