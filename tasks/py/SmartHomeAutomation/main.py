# main.py
import threading
import paho.mqtt.client as mqtt
from databasesetup import create_database, load_thermostat_values
from flask import Flask
from web_app import app, set_lights_state, set_thermostat_temperature

# MQTT topics for devices
LIGHTS_TOPIC = "smart_home/lights"
THERMOSTAT_TOPIC = "smart_home/thermostat"

# Initial device states
lights_state = "off"
thermostat_temperature = 20.0

# Database setup
create_database()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(LIGHTS_TOPIC)
    client.subscribe(THERMOSTAT_TOPIC)

def on_message(client, userdata, msg):
    global lights_state, thermostat_temperature

    if msg.topic == LIGHTS_TOPIC:
        # Interpret "1" as lights on, "0" as lights off
        lights_state_bool = bool(int(msg.payload))
        lights_state = "on" if lights_state_bool else "off"
        set_lights_state(lights_state)  # Pass lights_state to the Flask app

    elif msg.topic == THERMOSTAT_TOPIC:
        # Update thermostat temperature
        new_temperature = float(msg.payload)
        thermostat_temperature = new_temperature
        set_thermostat_temperature(new_temperature)  # Update Flask app attribute

        # Check if thermostat temperature is in the database    
        thermostat_values = load_thermostat_values()
        description = thermostat_values.get(thermostat_temperature, "No description available")
        print(f"{description}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect("cloud.tbz.ch", 1883, 60)

def mqtt_thread():
    # MQTT client loop forever
    client.loop_forever()

# Start MQTT client in a separate thread
mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.start()

if __name__ == '__main__':
    app.config['lights_state'] = lights_state
    app.config['thermostat_temperature'] = thermostat_temperature
    app.run(host="0.0.0.0", port=4000)