from flask import Flask, request, render_template, redirect

app=Flask(__name__)

app.config['DEBUG']=True


@app.route('/home')
def make_home():
    return render_template('home.html', title="User signup")

app.run()