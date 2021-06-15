from selenium.webdriver.common.keys import Keys

class SearchManager:

    def __init__(self, **kwargs):
        self.search_field=kwargs['input']
        self.people_category=kwargs['category']

    def search_input(self):
        self.search_field.send_keys("it recruiter")
        self.search_field.send_keys(Keys.ENTER)

    def select_category(self):
        self.people_category.click()