import json


with open('private_config.conf', 'r') as configFile:
    config = json.load(configFile)

secret_key, email = config['SECRET_KEY'], config['Email']