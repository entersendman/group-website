from flask import Flask, render_template, request, flash
from forms import ContactForm

import sendModule
#mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

#mail.init_app(app)

@app.route('/dfsd')
def home():
  return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:

      sendModule.sendMail(form.email.data,form.name.data)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)
