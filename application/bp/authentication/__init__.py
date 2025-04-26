from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegisterForm
from application.database import User
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')
@authentication.route('/dashboard')
def dashboard():
    # user_records = User.all()

    return render_template('dashboard.html')

@authentication.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.find_user_by_email(form.email.data)
        if existing_user:
            flash('Email is already registered.', 'danger')
        else:
            new_user = User.create(form.email.data, form.password.data)
            new_user.save()
            flash('Registration successful!', 'success')
            return redirect(url_for('authentication.dashboard'))
    return render_template('registration.html', form=form)


