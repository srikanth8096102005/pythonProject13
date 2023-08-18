from flask_mail import Mail,Message
from flask import request
import random
from project_files.config import app

mail= Mail(app)

def send_otp(email):
    # try:
        otp= str(random.randint(100000,999999))
        msg= Message('your otp is'+' '+otp, sender=app.config['MAIL_USERNAME'], recipients=[mail])
        mail.send(msg)
        otp_validation= otp_valid(otp)
        if otp_validation == True:
            return True
        else:
            return False
    # except Exception as e:
    #     return {e}
def otp_valid(otp):
    userSide_otp = request.form['OTP']
    if userSide_otp == otp:
        return True