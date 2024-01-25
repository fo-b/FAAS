# main.py
import time
from threading import Thread
from flask import Flask, render_template
import schedule
from mqtt_module import client, last_state, GARAGE_DOOR_TOPIC
from garage_door import eval_garage_door_state, GarageDoorState

# Flask application instance
app = Flask(__name__)

# Flask route definition
@app.route("/")
def index():
    return render_template("index.html", last_state=last_state)

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
