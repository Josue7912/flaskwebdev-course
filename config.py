import profile

class Config:
    SECRET_KEY = "Keep it a secret, at all costs"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = 'prod'

    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:codingnomads@localhost/hp'
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://isudggiveggtsx:68a56b4286f6801af9d4f95de4efc754d539d56cc3834636f7efde485a4e0314@ec2-3-225-30-189.compute-1.amazonaws.com:5432/d5uiua5c39ldeh'

    MAIL_SERVER='smtp.mailtrap.io'
    MAIL_PORT = 2525

    MAIL_USERNAME = profile.username
    MAIL_PASSWORD = profile.password
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    HP_MAIL_SUBJECT_PREFIX = 'HP Feedback - '
    HP_MAIL_SENDER = 'email1@example.com'
    HP_MAIL_RECEIVER = 'email2@example.com'

    def init_app(app):
        pass

config = {'default': Config}