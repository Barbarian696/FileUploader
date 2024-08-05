import os
import configparser
from glob import glob


class ReadFiles(object):
    @staticmethod
    def list_files_scandir(path):
        file_list = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.*'))]
        return file_list

    @staticmethod
    def read_config_properties(config_path, section):
        config = configparser.RawConfigParser()
        config.read(config_path)
        details_dict = dict(config.items(section))
        return details_dict
