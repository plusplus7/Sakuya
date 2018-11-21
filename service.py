import uuid
import flask
import config

FlaskApp = flask.Flask(__name__, template_folder='statics/templates')
FlaskApp.debug = True
FlaskApp.secret_key = 'development'

OAUTH = OAuth(FlaskApp)

@FlaskApp.route('/')
def Homepage():

    """Render the home page."""

    return flask.render_template('homepage.html', sample='Flask-OAuthlib')

@FlaskApp.route('/dashboard')
def ExpenseDashboard():

    """Handler user's request to dashboard"""

    if str(flask.session['state']) != str(flask.request.args['state']):
        raise Exception('state returned to redirect URL does not match!')
    response = g_msgraph.authorized_response()
    flask.session['access_token'] = response['access_token']
    return flask.redirect('/graphcall')

if __name__ == '__main__':
    FlaskApp.run()
