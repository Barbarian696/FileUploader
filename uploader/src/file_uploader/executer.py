from file_reader import ReadFiles
from file_sorter import FileSorter
from file_uploader import Uploader

DIRECTORY_PATH = 'DIRECTORY_PATH'


class Executor(object):

    @staticmethod
    def execute_uploader():
        read_files = ReadFiles()
        sort_files = FileSorter()
        upload_files = Uploader()

        directory_path = read_files.read_config_properties('config.properties', DIRECTORY_PATH)
        file_list = read_files.list_files_scandir(directory_path.get('path'))
        media_list, image_list, doc_list = sort_files.sort_media_images_and_documents(file_list)

        upload_files.upload_to_s3_buckets(media_list, image_list)
        upload_files.upload_to_google_cloud(doc_list)


def main():
    ex = Executor()
    ex.execute_uploader()


main()

