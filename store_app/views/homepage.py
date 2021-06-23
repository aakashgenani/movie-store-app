from app import app


@app.route('/')
@app.route('/home')
def home():
    return "Welcome to the Movie Store app."
