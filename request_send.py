class RequestSend:

    def __init__(self, **kwargs):
        self.invitation_button = kwargs["button"]

    def send_invitation(self):
        self.invitation_button.click()