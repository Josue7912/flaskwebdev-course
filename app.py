from hp import create_app

def app_creation():
    app = create_app('Feedback-app')
    assert app