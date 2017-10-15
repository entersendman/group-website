from flask import Flask, render_template, request, flash, json

import sendModule
#mail = Mail()

application = Flask(__name__)

application.secret_key = 'development key'

#mail.init_app(app)

@application.route('/')
def home():
  return render_template('index.html')


@application.route('/subscribeUser', methods=['POST'])
def contact():
  UserEmail =  request.form['to']
  UserName = request.form['name']

  sendModule.subscribeUser_UserSide(UserEmail,UserName)
  sendModule.subscribeUser_StudioSide(UserEmail,UserName)

  return json.dumps({'status':'subscribed','UserEmail':UserEmail,'UserName':UserName});

@application.route('/orderProject', methods=['POST'])
def order():
  CustomerName = request.form['CustomerName']
  CustomerEmail = request.form['CustomerEmail']
  CustomerPhone = request.form['CustomerPhone']
  CustomerLocation = request.form['CustomerLocation']
  CustomerCompany = request.form['CustomerCompany']
  CustomerTypeProject = request.form['CustomerTypeProject']
  CustomerProjectDetails = request.form['CustomerProjectDetails']

  sendModule.orderProject_UserSide(CustomerName, CustomerEmail, CustomerPhone, CustomerLocation, CustomerCompany, CustomerTypeProject,  CustomerProjectDetails)
  sendModule.orderProject_StudioSide(CustomerName, CustomerEmail, CustomerPhone, CustomerLocation, CustomerCompany, CustomerTypeProject,  CustomerProjectDetails)

  return json.dumps({'status':'ordered','CustomerEmail':CustomerEmail,'CustomerName':CustomerName});
  
if __name__ == '__main__':
  application.run()


