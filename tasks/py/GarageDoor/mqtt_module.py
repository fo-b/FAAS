# mqtt_module.py
import paho.mqtt.client as mqtt
from garage_door import eval_garage_door_state, GarageDoorState

# Topic on which we receive the sensor data
GARAGE_DOOR_TOPIC = "koop/poop"

# global variable to keep the last state of the garage door
last_state: GarageDoorState = GarageDoorState.NEITHER

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
        last_state = new_state.name
        print(f"Updated last_state: {last_state}")

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("cloud.tbz.ch", 1883, 60)
