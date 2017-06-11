from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = 'Go0Gl3524'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'authorisationrequest@gmail.com'
app.config["MAIL_PASSWORD"] = 'digital.247operations'

mail.init_app(app)

@app.route('/')
def home():
  return render_template('home.html')

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
      msg = Message(subject='CPS Access Request', sender='authorisationrequest@gmail.com', recipients=['bfyffe1993@gmail.com'])
      msg.body = """
      Hi 24/7, please action the following request for CPS access.
      ------------------------------------------------------------
      The Users name: %s
      The Username: %s
      Sent From: %s 
      Email: %s
      %s
      """ % (form.usersname.data, form.username.data, form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
  
if __name__ == '__main__':
  app.run(debug=True)