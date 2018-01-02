from flask import Flask, request, render_template, redirect

app=Flask(__name__)

app.config['DEBUG']=True

#function to check if field was empty 

''' def is_empty_field(form_value):
    #takes value of form and checks to see if it is an empty string
    if form_value == "":
        
    #if it is empty string then display error message
    #error message
        error= "Missing information. Please enter username, password and verify password"
        
    #else pass if all fields are present 
    else:
        return False '''

#routes to home screen showing form 
@app.route('/home')
def make_home():
    return render_template('home.html', title="User signup")

#processes form to check for correct input length an to ensure there are no spaces
@app.route('/home', methods=['post'])
def process_form():
    # need to make conditional to process form if method is get or post 
    if request.method =='POST':
        user_name= request.form['user_name'] #variables to contain form inputs
        password= request.form['password']
        verify_password= request.form['verify_password']
        email=request.form['email']
    ''' if not user_name and password and verify_password:
        #throw error message requesting all fields be entered
        error= "Please enter info in all fields" '''
    return redirect(url_for('welcome'))
    #condition to check if input value is correct length 
    ''' if is_empty_field(user_name)=False: 
        if len(user_name)< 3 or > 19:
            error:"Input too long. Please enter a value that is between (3-20) characters."
        else:
            for char in user_name():
                if char == "":
                    error="Please re-enter info without spaces"
                else:
                    return redirect('/welcome', user_name='user_name') '''

@app.route('/welcome')
def welcome_user():
    return render_template('welcome.html', username="username")

app.run()