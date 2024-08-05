import boto3
from google.cloud import storage
from file_reader import ReadFiles

fr = ReadFiles()
BUCKET_NAME = 'BUCKET_NAME'
S3_FOLDER = 'S3_FOLDER'
G_BUCKET_NAME = 'G_BUCKET_NAME'


class Uploader(object):

    @staticmethod
    def upload_to_s3_buckets(*file_list):
        final_file_list = []
        s3 = boto3.resource('s3')
        bucket = (fr.read_config_properties('config.properties', BUCKET_NAME)).get('b_name')
        s3_file_path = (fr.read_config_properties('config.properties', S3_FOLDER)).get('s3_path')
        for lst in file_list:
            final_file_list.extend(lst)
        for file in final_file_list:
            s3.Bucket(bucket).upload_file(file, s3_file_path)

    @staticmethod
    def upload_to_google_cloud(*file_list):
        final_file_list = []
        for lst in file_list:
            final_file_list.extend(lst)

        storage_client = storage.Client()
        bucket_name = (fr.read_config_properties('config.properties', G_BUCKET_NAME)).get('g_name')
        bucket = storage_client.get_bucket(bucket_name)  # your bucket name
        blob_name = (fr.read_config_properties('config.properties', G_BUCKET_NAME)).get('g_blob')

        blob = bucket.blob(blob_name)
        for file in final_file_list:
            blob.upload_from_filename(file)