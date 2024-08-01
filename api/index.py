
from flask import Flask, request
import paho.mqtt.publish as publish

app = Flask(__name__)

@app.route('/')
def index():
    mqtt_topic = request.args.get('mqtt_topic', '')
    mqtt_payload = request.args.get('mqtt_payload', '')
    publish.single(mqtt_topic, mqtt_payload, hostname="broker.mqttgo.io")
    return f'MQTT Topic: {mqtt_topic}, MQTT Payload: {mqtt_payload}. Message sent.'

if __name__ == '__main__':
    app.run(debug=True)
