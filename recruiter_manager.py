
class RecruiterManager:

    def __init__(self, **kwargs):
        self.recruiter_location = kwargs["location"]
        self.connect_button = kwargs["connect"]
        self.enabled_buttons = [button for button in self.connect_button if button.is_enabled() is True]

