from flask import request, render_template, flash, session
from . import main
from .. import db
from ..models import Feedback
from flask_mail import Message
from app import mail
import re
from .forms import IncidentForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit', methods=['GET', 'POST'])
def submit():
    form = IncidentForm()
    if form.validate_on_submit():
        customer = form.customer.data
        dealer = form.dealer.data
        rating = form.rating.data
        comments = form.rating.data
        suggestions = form.rating.data
        if db.session.query(Feedback).filter(Feedback.customer == session['customer']).count() == 0:
            data = Feedback(session['customer'], dealer, rating, comments, suggestions)
            db.session.add(data)
            db.session.commit()
            msg = Message('HP Feedback', sender = 'email1@example.com', recipients = ['email2@example.com'], html=None)
            msg.html = f"<h3>New Feedback Submission</h3><ul><li>Customer: {session['customer']}</li><li>Dealer: {session['dealer']}</li><li>Rating: {rating}</li><li>Comments: {comments}</li><li>Suggestions: {suggestions}</li></ul>"
            msg.body = f"New Feedback Submission:\
            * Customer: {customer}\
                * Dealer: {dealer}\
                    * Rating: {rating}\
                        * Comments: {comments}\
                            * Suggestions: {suggestions}"
            mail.send(msg)
            return render_template('thankyou.html')
        flash('You have already submmitted your feedback')
    session['customer'] = form.customer.data
    session['dealer'] = form.dealer.data
    return render_template('index.html', form=form, customer=session.get('customer'), dealer=session.get('dealer'))