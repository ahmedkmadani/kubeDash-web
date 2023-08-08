from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'ahmedk.madani@outlook.com'  
app.config['MAIL_PASSWORD'] = 'ahmed@12345'  
app.config['MAIL_DEFAULT_SENDER'] = 'ahmedk.madani@outlook.com' 


mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        email = request.form['email']
        occupation = request.form['occupation']
        phone_os = request.form['phone_os']

        msg = Message('New Beta User Signup',
                      recipients=['ahmedkamal543@gmail.com'])
        

        msg.body = f"First Name: {first_name}\nEmail: {email}\nOccupation: {occupation}\nPhone OS: {phone_os}"


        msg_confirmaton = Message('Beta User Signup Confirmation',
                      recipients=[email])  

        msg_confirmaton.body = f"Dear {first_name},\n\n🎉 Thank you for signing up as a beta user for KubeDash! 🚀 We have received your information and will contact you soon with further details.\n\nBest regards,\nKubeDash Team"

        mail.send(msg)

        mail.send(msg_confirmaton)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
