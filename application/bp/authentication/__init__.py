from flask import Blueprint, render_template, redirect, url_for, flash, request
from application.database import User, db
from application.bp.authentication.forms import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='templates')

@authentication.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@authentication.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user_check = User.find_user_by_email(form.email.data)
            if user_check is None:
                user = User.create(form.email.data, form.password.data)
                user.save()
                return redirect(url_for("authentication.dashboard"))
            else:
                flash("Already Registered")
                return redirect(url_for("authentication.registration"))

    return render_template('registration.html', form=form)
