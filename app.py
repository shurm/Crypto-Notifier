import os

from flask import Flask, render_template, request, jsonify

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/email', methods=['POST'])
def email():
    msg = EmailMessage()
    msg.set_content("Hello World")

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Test Email'
    msg['From'] = 'michaelshur28@gmail.com'
    msg['To'] = 'michaelshur28@gmail.com'

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()