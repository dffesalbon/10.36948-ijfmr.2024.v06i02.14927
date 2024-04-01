import csv
import os
from logging import Logger


class Data():
    def __init__(self, logger: Logger = None) -> None:
        self.__logger = logger
        self.__append = 'a'
        self.__write = 'w'
        self.__fields = ['date time',
                         'match',
                         'region',
                         'game time',
                         'slot',
                         'player slot',
                         'message']

    def write(self, file, row_data):

        ops = self.__append if os.path.exists(file) else self.__write

        f = open(file, ops, encoding="utf-8")  # open the file: write or append
        writer = csv.writer(f, lineterminator='\n')  # create the csv writer

        if ops is self.__write:
            writer.writerow([f for f in self.__fields])  # include header

        writer.writerow(row_data)  # write a row to the csv file
        f.close()  # close the file
