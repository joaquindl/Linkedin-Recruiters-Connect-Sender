import os
from dotenv import load_dotenv

load_dotenv(".env")

class LoginManager:

    def __init__(self, **kwargs):
        self.login_email = kwargs["email"]
        self.login_password = kwargs["password"]
        self.login_button = kwargs["button"]

    def login(self):
        self.login_email.send_keys(os.getenv("LOGIN_EMAIL"))
        self.login_password.send_keys(os.getenv("LOGIN_PASSWORD"))
        self.login_button.click()



