from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from login_manager import LoginManager
from remember_manager import RememberManager
from search_manager import SearchManager
from recruiter_manager import RecruiterManager
from request_send import RequestSend


def time_delay(sec):
    delay = True
    while delay:
        time.sleep(sec)
        delay = False


load_dotenv(".env")

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/")

# Login
time_delay(5)
login_manager = LoginManager(
    email=driver.find_element_by_id("session_key"),
    password=driver.find_element_by_id("session_password"),
    button=driver.find_element_by_css_selector(".sign-in-form .sign-in-form__submit-button")
)
login_manager.login()

# # When trying to login with selenium, Linkedin ask if you want to be remembered on your browser.
# # If you choose to remember you will probably need to disable it th second time you run the code
# remember_manager = RememberManager(
#     remember=driver.find_element_by_css_selector("#remember-me-prompt__form-primary button"),
#     noremember=driver.find_element_by_css_selector("#remember-me-prompt__form-secondary button")
# )
# # To be remembered use this function below
# remember_manager.remember()
# # If you don't want to be remembered
# remember_manager.dont_rememeber()


# Recruiter input search and category select
search_manager = SearchManager(
    input=driver.find_element_by_class_name("search-global-typeahead__input"),
    category=driver.find_element_by_css_selector(".search-results-container .artdeco-card "
                                                      ".search-results__cluster-bottom-banner a")
)
search_manager.search_input()
time_delay(2)
search_manager.select_category()

time_delay(2)


# Check if recruiter resides in Buenos Aires or in Argentina
recruiter_manager = RecruiterManager(
    location=driver.find_elements_by_css_selector(".linked-area div .entity-result__secondary-subtitle"),
    connect=driver.find_elements_by_css_selector(".entity-result__actions div button"),
)

for n in range(len(recruiter_manager.enabled_buttons)):
    if recruiter_manager.recruiter_location[n].text == "Argentina" or \
            recruiter_manager.recruiter_location[n].text == "Buenos Aires":
        recruiter_manager.enabled_buttons[n].click()
        time_delay(4)
        request_send = RequestSend(
            button=driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
        )
        request_send.send_invitation()

driver.quit()
