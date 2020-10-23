import yaml
import os

config_path = os.path.dirname(__file__)
file_path = os.path.join(config_path, 'config.yaml')
def read_config():
    f = open(file_path)
    y = yaml.load(f)
    return y


