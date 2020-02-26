from flask import Flask, redirect, url_for, request
from fatsecret import Fatsecret

consumer_key = '41c60054515a403298bb7e62c4708b3a'
consumer_secret = '91a5240e4771461dba932468a6c48654'

app = Flask(__name__)
fs = Fatsecret(consumer_key, consumer_secret)

@app.route("/")
def index():
    if request.args.get('oauth_verifier'):

        verifier_pin = request.args.get('oauth_verifier')

        # Store token as desired. The session is now authenticated
        session_token = fs.authenticate(verifier_pin)

        return redirect(url_for('profile'))

    else:
        return "<a href={0}>Authenticate Access Here</a>".format(url_for('authenticate'))


@app.route("/auth")
def authenticate():

    auth_url = fs.get_authorize_url(callback_url="http://127.0.0.1:5000")

    return redirect(auth_url)


@app.route("/profile")
def profile():
    food = fs.foods_get_most_eaten()

    return "<h1>Profile</h1><div><strong>Most Eaten Foods</strong><br>{}</div>"\
        .format(food)


if __name__ == "__main__":
    app.run()
