from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField, BooleanField, SubmitField
from wtforms.validators import Required
import re
import gevent.monkey
from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from give_answer import answer_question
import unicodedata
import wolframalpha
import wikipedia
import json 
with open('data.json') as data:
    d = json.load(data)
    print(d)

class ExampleForm(Form):
    question = TextField('', description='', validators=[Required()])
    submit_button = SubmitField('Go')


#def create_app(configfile=None):
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/qas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']= "AA2X2E-GKPAKE8365"
#AppConfig(app, configfile)
Bootstrap(app)
db = SQLAlchemy(app)

class users(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))

#app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    all_user = users.query.all()
    print(all_user)
    if request.method == 'POST':
        try:
            question = request.form['question']
        except KeyError(e):
            print("key eror")
            print('I got a KeyError - reason '+str(e))
        except:
            print('I got another exception, but I should re-raise')
            raise


        print(question)
        answer = answer_question(question)
        print('answer: '+answer)
        answer=re.sub('([(].*?[)])',"",answer)

        return render_template('answer.html', answer=answer, question=question)

    form = ExampleForm()
    return render_template('index.html', form=form)
    #return app

# create main callable
if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 9191), app)
    print("starting server on port 9191")
    http_server.serve_forever()
    