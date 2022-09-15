"""Module for handling the retrieval of status defined in the status file which will be used in Discord presence."""

import os
from shutil import copy
from itertools import cycle
import csv

class StatusUtil:

    def __init__(self, target_file):
        self.target_file = target_file
        self.load()

    def load(self):
        """Retrieve the list of status available
        in the status.csv file, create a file by 
        copying the status.csv.sample if cannot 
        find a status.csv file in the directory.
        """
        
        self.status_arr = []
        if not os.path.isfile(self.target_file):
            copy(f"{self.target_file}.sample", self.target_file)

        with open(self.target_file, "r") as f:
            reader = csv.reader(f, delimiter = "|")
            for row in reader:
                status = row[0]
                self.status_arr.append(status)

        self.loop = cycle(self.status_arr)

    def get(self):
        return next(self.loop)