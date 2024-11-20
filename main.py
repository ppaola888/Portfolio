from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/project_detail_1')
def project_detail_1():
    return render_template('project_detail_1.html')

@app.route('/project_detail_2')
def project_detail_2():
    return render_template('project_detail_2.html')

@app.route('/project_detail_3')
def project_detail_3():
    return render_template('project_detail_3.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        oggetto= request.form['subject']
        messaggio = request.form['message']
        
        # Email
        email_body = f"Nome: {nome}\nEmail: {email}\nOggetto: {oggetto}\nMessaggio: {messaggio}"
        
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS,
                f"Subject: Nuovo messaggio dal Portfolio\n\n{email_body}")
            return redirect(url_for('thank_you', name=nome))
        except Exception as e:
            return f"Errore nell'invio dell'email: {e}"
    return render_template('index.html')


@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Guest')  
    return render_template('thank_you.html', name=name)


@app.route('/credits')
def credits():
    return render_template('credits.html')


if __name__ == '__main__':
    app.run(debug=False)