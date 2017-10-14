from flask import Flask, render_template, request, flash, json

import sendModule
#mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

#mail.init_app(app)

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/subscribeUser', methods=['POST'])

def contact():
  to =  request.form['to']
  name = request.form['name']

  sendModule.sendMail(to,name)

  return json.dumps({'status':'subscribed','to':to,'name':name});
  
if __name__ == '__main__':
  app.run(debug=True)
