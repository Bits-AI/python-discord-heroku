"""Module for getting the parameters and credentials from the config json file."""

import os
import json

def get_token():
    """Function to get Discord token from the 
    configuration json file.
    """

    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config"))
    with open(f'{directory}/config.json') as jsonfile:
        file_reader = json.load(jsonfile)
        return file_reader['token']

def get_prefix():
    """Function to get the Louise bot prefix 
    in Discord.
    """

    return ';'