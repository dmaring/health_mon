#!/usr/bin/python3
# Main script

import storage
import render
import sys
import download
import time
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

project_id = "drews-project-279817"
subscription_id = "image_topic-sub"
# Set location for downloaded file to raspberry pi
destination_file_name = "/home/pi/app/health_mon/raspberry_pi/images/new"
# Number of seconds the subscriber should listen for messages
timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Received {message}.")
    message.ack()

    # parse message for bucket_name, source_blob_name
    bucket_name = message.attributes.get("bucketId")
    source_blob_name = message.attributes.get("objectId")

    download.download_blob(bucket_name, source_blob_name, destination_file_name)

    render.render_file(destination_file_name)


while True:
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")
    time.sleep(5)

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.