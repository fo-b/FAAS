import time
from threading import Thread
from flask import Flask
import schedule
import paho.mqtt.client as mqtt
from enum import Enum

def split_into_axis(raw_sensor_value: str):
    # TODO: Implement
    values_str = raw_sensor_value.split(',')
    values_float = [float(value) for value in values_str]
    values_tuple = tuple(values_float)
    return values_tuple

split_into_axis("-0.03,0.99,0.05")

class GarageDoorState(Enum):
    CLOSED = 1,
    OPEN = 2,
    NEITHER = 3
    
def eval_garage_door_state(raw_sensor_value: str) -> GarageDoorState:
    x, y, z = split_into_axis(raw_sensor_value)
    # TODO: Implement
    if z < -0.8:
        return GarageDoorState.OPEN
    elif z > -0.1:
        return GarageDoorState.CLOSED
    else:
        return GarageDoorState.NEITHER

assert eval_garage_door_state("-0.03,0.99,0.05") == GarageDoorState.CLOSED
assert eval_garage_door_state("-0.03,0.85,0.05") == GarageDoorState.CLOSED
assert eval_garage_door_state("-0.03,0.0,-0.85") == GarageDoorState.OPEN
assert eval_garage_door_state("-0.03,0.0,-0.9") == GarageDoorState.OPEN
assert eval_garage_door_state("-0.03,0.0,-0.4")  == GarageDoorState.NEITHER
print("All tests successful")


# Topic on which we receive the sensor data
GARAGE_DOOR_TOPIC = "koop/poop"

# Flask application instance
app = Flask(__name__)

# global variable to keep the last state of the garage door 
last_state: GarageDoorState = GarageDoorState.NEITHER
if last_state == GarageDoorState.NEITHER:
    last_state = "Unknown"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect, then subscriptions will be renewed.
    client.subscribe(GARAGE_DOOR_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # Import the global variable into the function
    global last_state
    # Check if the topic is equal to ours
    if msg.topic == GARAGE_DOOR_TOPIC:
        msg_str = msg.payload.decode("utf-8")
        new_state = eval_garage_door_state(msg_str)
        # TODO: Implement
        last_state = new_state.name  

        print(f"Updated last_state: {last_state}")

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("cloud.tbz.ch", 1883, 60)

# Flask route definition
@app.route("/")
def index():
    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>Die Garage ist {last_state}</h1>
    </body>
    </html>
    """

# MQTT client loop start
client.loop_start()


def schedule_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    thread_schedule = Thread(target=schedule_thread, args=())
    thread_schedule.start()
    app.run()