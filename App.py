from flask import Flask
from flask_restful import Api, Resource
from flask_mail import Mail, Message

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'sresthaafeedback@gmail.com'
app.config['MAIL_PASSWORD'] = '@5Sresthaa1'
app.config['MAIL_DEFAULT_SENDER'] = 'sresthaafeedback@gmail.com'
app.config['MAIL_MAX_EMAILS'] = 'None'
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


class home(Resource):
    def get(self):
        return{"status_code": "200", "response": "/home"}


class wake(Resource):
    def get(self):
        return{"status_code": "200", "Api_status": "Active"}


class mailData(Resource):
    def get(self, receipientAddr, subject, body):
        msg = Message(subject, recipients=[receipientAddr])
        msg.html = '<b>Hello,<br>' + body
        mail.send(msg)
        return{"status_code": "200", "response": "message sent"}


api.add_resource(home, "/")
api.add_resource(wake, "/wake")
api.add_resource(
    mailData, "/mailData/<string:receipientAddr>/<string:subject>/<string:body>")

if __name__ == "__main__":
    app.run()
