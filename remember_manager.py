class RememberManager:

    def __init__(self, **kwargs):
        self.remember_me_button = kwargs["remember"]
        self.not_remember_button = kwargs["noremember"]

    def remember(self):
        self.remember_me_button.click()

    def dont_rememeber(self):
        self.not_remember_button.click()