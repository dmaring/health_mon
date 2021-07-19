#!/usr/bin/python3
# Main application

import storage
import render
import sys

def main(bucket_name, source_blob_name, destination_file_name):

    # Check Pub/Sub for new message
    # Parse message for file name

    # Download message fom Cloud Storage
    storage.download_blob(bucket_name, source_blob_name, destination_file_name)

    # Render image
    render.render(destination_file_name)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
