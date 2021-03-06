from flask import request, render_template, flash, url_for, redirect
from . import main
from .. import db
from ..models import Feedback
from flask_mail import Message
from app import mail
import re
from .forms import IncidentForm



@main.route('/', methods=['GET', 'POST'])
def index():
    form = IncidentForm()
    return render_template('index.html', form=form)

@main.route('/submit', methods=['GET','POST'])
def submit():
    form = IncidentForm()
    if form.validate_on_submit():
        customer = form.customer.data
        dealer = form.dealer.data
        rating = form.rating.data
        comments = form.comments.data
        suggestions = form.suggestions.data
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
        return render_template('index.html', form=form, message='You have already submmitted your feedback')
    return render_template('index.html', form=form, message='Please input valid Incident number HPXXXXXX')