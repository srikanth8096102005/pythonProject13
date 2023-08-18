from flask import request, render_template, redirect
import datetime
from project_files.config import db,signup_data
from project_files.db_insertion import insert_values,email_validataion
import json
from project_files.OTP_verification import send_otp


user_dict={}
class User_form_data:
    def signup(self):
        if request.method == 'POST':
            if request.form.get('Next') == 'Next':
                user_dict['fname'] = request.form['fname']
                user_dict['lname'] = request.form['lname']
                user_dict['date'] = request.form['dob']
                user_dict['email'] = request.form['email']
                db_data = signup_data.query.all()
                for item in db_data:
                    if item.email == user_dict['email']:
                        return 'This email already registered'
                return redirect('/setpassword')
            elif request.form.get('Cancel')=='Cancel':
                return redirect('/')
            else:
                return 'error accured'
        elif request.method == 'GET':
            today_date = datetime.datetime.now().replace(microsecond=0)
            past_year = datetime.timedelta(days=365)
            dob_form = today_date - past_year
            print('@@@@@@@@@@@@@@@@@@',dob_form)
            # all_users_data = signup_data.query.all()
            # str_date = datetime.datetime.strptime(today_date)
            return render_template('signup.html',dob_form= dob_form)

    def signin(self):
        if request.method == 'POST':

            email = request.form['email']
            password= request.form['password']
            resp= email_validataion(email,password)
            if resp:
                return 'Name:'+ resp[0][0]+' password:'+str('* '*len(resp[0][1]))
            return redirect('/signup')

        return render_template('signin.html')

    def set_password(self):
        if request.method=='POST':
            user_dict['password'] = request.form['password']
            user_dict['confirm_password']= request.form['confirm_password']
            if (user_dict['password']!=user_dict['confirm_password']) or user_dict['password']=='':
                return 'Error accured please check if the password and confirm password is the same and aslo check password will not allow the empty box'
            insert_values(user_dict)
            return redirect('/signin')
        else:
            return render_template('set_password.html')
    def home(self):
        if request.method=='POST':
            if request.form.get('action') == 'Register':
                return redirect('/signup')
            elif request.form.get('action') == 'Signin':
                return redirect('/signin')
            else:
                return 'error accured'
        else:
            return render_template('/home_page.html')
    def forgot_data(self):
        if request.method=='POST':
            if request.form.get('send') == 'OTP':
                email = request.form['email']
                # userside_otp= request.form['OTP']
                list = signup_data.query.all()
                for item in list:
                    if item.email == email:
                        otp_validate = send_otp(email)
                        if otp_validate==True:
                            return redirect('/setpassword')

                else:
                    return "can't find your account please register using http://127.0.0.1:8000/signup"
            elif request.form.get('OK') == 'Submit':
                return redirect('/setpassword')
        else:
            return render_template('forgot_password.html')

    # This is not related registration loginform just for testing purpose
    def get_data(self):
        d ={}
        l = []
        user_data = signup_data.query.all()
        for item in user_data:
            d['fname']= item.fname
            d['lname']=item.lname
            d['date']=item.date
            d['email']=item.email
            d['password']=item.password
            l.append(d)
        return l

data=User_form_data()



