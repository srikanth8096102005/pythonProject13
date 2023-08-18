from project_files.config import signup_data,db
def insert_values(user_dict):
    fname= user_dict['fname']
    lname=user_dict['lname']
    date= user_dict['date']
    email=user_dict['email']
    password=user_dict['password']
    values = signup_data(fname=fname,lname=lname, date=date, email=email, password=password)
    try:
        db.session.add(values)
        db.session.commit()
    except:
        return 'there is an error while posting data'

def email_validataion(email,password):
    try:
        list = db.session.query(signup_data.email,signup_data.password).filter_by(email=email,password=password).all()
        return list
    except:
        return 'ther is an error accurred whil fetching data from the data base'