from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = '***********'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = '**************'
app.config['MAIL_PASSWORD'] = '**************'
app.config['MAIL_DEFAULT_SENDER'] = '******************'
app.config['MAIL_MAX_EMAILS'] = 'None'
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Feedback/Collab Contact Request', recipients=[
        '********************'])
    msg.html = '<b>Hello ********,<br>This is a test request from your contact form</b>'
    mail.send(msg)

    return 'Message sent'


if __name__ == "__main__":
    app.run()
