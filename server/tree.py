# -*- coding: utf-8 -*-
import os


class FileTree(object):
    """
    Holds active filesystem representation
    """

    def __init__(self, path):
        """
        Path to FS to watch
        """
        super(FileTree, self).__init__()
        self.path = path

    def filter(self, file_path):
        """
        Filter files to watch
        """
        return True

    def scan(self):
        pass

