# coding: UTF-8
import flask

app = flask.Flask(__name__)


@app.route('/')
def toppage():
    return flask.render_template('toppage.html')

@app.route('/showname')
def showname():
    name = flask.request.args['name']
    return flask.render_template('showname.html', name=name)
