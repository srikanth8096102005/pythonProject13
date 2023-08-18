from flask import render_template
from project_files.User_data import data
from project_files.config import app
@app.route('/', methods=['POST', 'GET'])
def home_page():
    return data.home()

@app.route('/forgotpassword', methods=['POST','GET'])
def forgot_password():
    return data.forgot_data()

@app.route('/signup', methods=['POST', 'GET'])
def signup_form_data():
    return data.signup()
    # return render_template('password_mnmt.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin_form_data():
    return data.signin()

@app.route('/setpassword', methods=['POST', 'GET'])
def set_password_user():
    return data.set_password()

if __name__ == '__main__':
    app.run(debug=False, port=7000)
kmklmgkvfmdklbmfvfnfkjvnfkjvnklflmvlkfcmvklgfcmgklvfdmgklvlfdmglkvrmf