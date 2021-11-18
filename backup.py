from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:codingnomads@localhost/hp'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    suggestions = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments, suggestions):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments
        self.suggestions = suggestions



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
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
            send_mail(customer, dealer, rating, comments, suggestions)
            return render_template('thankyou.html')
        return render_template('index.html', message='You have already submmitted your feedback')



if __name__ == '__main__':
    app.run()