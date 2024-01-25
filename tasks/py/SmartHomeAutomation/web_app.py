# web_app.py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

def set_lights_state(state):
    app.lights_state = state  # Store lights_state as an attribute of the Flask app

@app.route("/")
def index():
    # Redirect to the lights route
    return redirect(url_for('lights'))

@app.route("/lights")
def lights():
    lights_state = getattr(app, 'lights_state', 'unknown')  # Get lights_state from the app attribute
    return render_template('template.html', lights_state=lights_state)


@app.route("/thermo")
def thermostat():
    return f"<h1>Thermostat's value is</h1>"
