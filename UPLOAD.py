import sys
from google.cloud import storage

# (bucket_name, source_file_name, destination_blob_name)
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

if __name__ == "__main__":
    # input
    #bucket = input("bucket name: ")
    #source = input("source file name: ")
    #dest = input("destination blob name: ")
    #upload_blob(bucket,source,dest)

    # sys argv
    print(" >> sys.argv",sys.argv)
    bucket = sys.argv[1]
    source = sys.argv[2]
    dest = sys.argv[3]
    upload_blob(bucket,source,dest)
        # result
        # python3 up.py couserde test.txt sys_text.txt
        # >> sys.argv ['up.py', 'couserde', 'test.txt', 'sys_text.txt']
        # File test.txt uploaded to sys_text.txt.
