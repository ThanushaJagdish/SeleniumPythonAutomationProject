import configparser
import os

class ConfigReader:

    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configurations", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_username(self):
        return self.config.get("login", "username")

    def get_password(self):
        return self.config.get("login", "password")

    def get_base_url(self):
        return self.config.get("env", "base_url")

    def get_cvv(self):
        return self.config.get("card", "cvv")

    def get_name_on_card(self):
        return self.config.get("card", "name")