from flask import render_template, flash, redirect
from arbor.app import app
from arbor.app.models.AuthForm import LoginForm
#@app.route('/')
@app.route('/arbor')
def arbor():
   # print(app.config['SECRET_KEY'])
   return render_template('arbor.html')
@app.route('/')
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
