from flask import Flask, render_template, request, flash
from forms import ContactForm

import sendModule
#mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

#mail.init_app(app)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      sendModule.sendMail("volodya.ternopil1997@gmail.com","zatrimka")

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)
