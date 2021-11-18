from flask import request, render_template
from . import main
from .. import db
from ..models import Feedback
from flask_mail import Message
from app import mail

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        suggestions = request.form['suggestions']
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments, suggestions)
            db.session.add(data)
            db.session.commit()
            msg = Message('HP Feedback', sender = 'email1@example.com', recipients = ['email2@example.com'], html=None)
            msg.html = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li><li>Suggestions: {suggestions}</li></ul>"
            msg.body = f"New Feedback Submission:\
            * Customer: {customer}\
                * Dealer: {dealer}\
                    * Rating: {rating}\
                        * Comments: {comments}\
                            * Suggestions: {suggestions}"
            mail.send(msg)
            return render_template('thankyou.html')
        return render_template('index.html', message='You have already submmitted your feedback')