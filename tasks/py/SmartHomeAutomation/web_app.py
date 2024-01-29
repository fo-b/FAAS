# web_app.py
from flask import Flask, render_template, redirect, url_for, jsonify, Response
from databasesetup import load_thermostat_values
import json

app = Flask(__name__)

def set_lights_state(state):
    app.lights_state = state  # Store lights_state as an attribute of the Flask app

def set_thermostat_temperature(temperature):
    app.thermostat_temperature = temperature  # Store thermostat_temperature as an attribute


#Forward URL to Lights // only used because there is no "main" page
@app.route("/")
def index():
    # Redirect to the lights route
    return redirect(url_for('lights'))

#Adds new url page called "lights" and loads the template for visualations
#Data comes from mqtt and loads out to a template
@app.route("/lights")
def lights():
    lights_state = getattr(app, 'lights_state', 'unknown')  # Get lights_state from the app attribute
    return render_template('template.html', lights_state=lights_state)


#Adds new url page called "thermo" and 
@app.route("/thermo")
def thermostat():
    # Get the thermostat temperature from the app attribute
    thermostat_temperature_value = getattr(app, 'thermostat_temperature', 'unknown')

    # Use the temperature to fetch the description from the database
    thermostat_values = load_thermostat_values()
    description = thermostat_values.get(thermostat_temperature_value, "unknown")

    #return f"<h1>Today it's: {description}</h1>"
    return render_template('thermo.html', description=description)

@app.route("/json")
def thermostat_json():
    # Fetch all thermostat values from the database
    thermostat_values = load_thermostat_values()

    # Convert the dictionary to a JSON string with indentation
    json_string = json.dumps(thermostat_values, indent=2)

    # Create a Flask response with JSON content type
    response = Response(response=json_string, status=200, content_type="application/json")

    # Return the response
    return response
