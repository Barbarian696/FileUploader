from file_reader import ReadFiles

FILE_EXTENSIONS = 'FILE_EXTENSIONS'


class FileSorter(object):

    @staticmethod
    def sort_media_images_and_documents(file_list):
        fr = ReadFiles()
        ext_types = (fr.read_config_properties('config.properties', FILE_EXTENSIONS))

        media_tuple = ext_types.get('media')  # ('mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm')
        doc_tuple = ext_types.get('doc')  # ('doc', 'docx', 'pdf', 'csv')
        image_tuple = ext_types.get('image')  # ('jpg', 'png', 'svg', 'webp')
        image_files = []
        doc_files = []
        media_files = []
        for file in file_list:
            if file.endswith(media_tuple):
                media_files.append(file)
            elif file.endswith(doc_tuple):
                doc_files.append(file)
            elif file.endswith(image_tuple):
                image_files.append(file)
        return media_files, image_files, doc_files
