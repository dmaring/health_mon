#!/usr/bin/python3
# Download file and return path of file

import storage
import render
import sys

def download(bucket_name, source_blob_name, destination_file_name):

    
    # Download message fom Cloud Storage
    storage.download_blob(bucket_name, source_blob_name, destination_file_name)

    # Render image
    return(destination_file_name)


if __name__ == "__main__":
    download(sys.argv[1], sys.argv[2], sys.argv[3])
