from flask import Flask, request, url_for, session, redirect, render_template
from forms import RegistrationForm, LoginForm, UserForm
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = '424b2b01b3b28ab8fbc7707c854570f7'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "c05cbe655b464e36aa3fa5b0ce5416f0",
        client_secret = "2e2d9afa7d0f480093b147b78d289aa4",
        redirect_uri= url_for('Guest', _external=True)
    )

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Register', methods=['GET', 'POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.validate_date() == True:
            sp_oauth = create_spotify_oauth()
            auth_url = sp_oauth.get_authorize_url()
            return redirect(auth_url)
    return render_template('Registration.html', title = 'Register' , form = form)


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    return render_template('Login.html', title = 'Login' , form = form)

@app.route('/Guest', methods=['GET', 'POST'])
def Guest():
    form = UserForm()
    return render_template('Guest.html', title = 'User', form = form)

if __name__ == '__main__':
    app.run(debug=True)
