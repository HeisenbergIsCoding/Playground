import configparser


def read_api_key_from_config():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config['API']['chatgpt_api_key']


