#In some cases instead of pulling data, it will be pushed to us
#Digital architecture is to have some kind of a message que, and clients listening to it
#remember to use spammer.py

"""NATS client accepint JSON messages on 'rides" topic"""
import json

from pynats import NATSClient


def handler(message):
    payload = json.loads(message.payload)
    print(payload)  # TODO: store/calculate/train ...


client = NATSClient('nats://localhost:4222')
client.connect()
client.subscribe('rides', callback=handler)
client.wait(count=10)  # Read 10 messages