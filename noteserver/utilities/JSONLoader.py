import Log
import json

__config_file_address = "../config/"


def get_json(filename):
    """Retrieves and returns JSON data from specified file.
    Parameters
        ----------
    filename : str
        Can either be the path to the file, or just the file name if file is in ../config.
    """
    config = None
    # If user passes an address, read from that address instead of config folder.
    if "/" not in filename:
        try:
            with open(__config_file_address + filename + ".json") as jsonfile:
                config = json.load(jsonfile)
        except FileNotFoundError:
            Log.ERROR("File " + __config_file_address + filename + ".json not found.")
    else:
        try:
            with open(filename) as jsonfile:
                config = json.load(jsonfile)
        except FileNotFoundError:
            Log.ERROR("File " + filename + " not found.")
    return config


# Create a JSON file given any field, and any file name
def create_json(filename, primary_field):
    """Creates a JSON file in a specified directory
    Keyword Arguments
    filename -- file name for the json data
    primary_field --
    """
    if "/" not in filename:
        f = open(__config_file_address + filename + ".json", "w+")
    else:
        f = open(filename, "w+")

    data = {}
    data[primary_field] = []
    save_json(data, filename)


def save_json(data, filename):
    """Save data into an existing JSON file and returns an error if the JSON file is not found
    Parameters
        ----------
    data : dict
        Data to be saved as a JSON object.
    filename : str
        Can either be the path to the file, or just the file name if file is in ../config.
    """

    try:
        # If user passes an address, save to that address instead of config folder.
        if "/" not in filename:
            with open(__config_file_address + filename + '.json', 'w') as outfile:
                json.dump(data, outfile)
        else:
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
    except FileNotFoundError:
        Log.ERROR("File " + __config_file_address + filename + ".json not found.")