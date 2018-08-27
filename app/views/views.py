from flask import render_template, flash, redirect
from arbor.app import app
#from arbor.app.forms import LoginForm
@app.route('/')
#@app.route('/arbor')
def index():
   # print(app.config['SECRET_KEY'])
   return render_template('bbb.html')
