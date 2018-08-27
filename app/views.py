from flask import render_template, flash, redirect
from arbor.app import app
#from arbor.app.forms import LoginForm
@app.route('/index')
def index():
   return 'hello'

@app.route('/arbor')
def arbor():
   # print(app.config['SECRET_KEY'])
   return render_template('arbor.html')
