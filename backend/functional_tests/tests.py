from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
from selenium.webdriver.common.by import By
from decouple import config

MAX_WAIT = 8


class NewVisitorTest(StaticLiveServerTestCase):

    #* special method that gets called before and after each test
    def setUp(self):  
        self.browser = webdriver.Firefox()
        staging_server = config('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):  
        self.browser.quit()

    # user goes to the API, sees if they are greeted by the different endpoints
    def test_user_visits_api(self):
        self.browser.get(self.live_server_url + 'cards/api/')
        header_text = self.browser.find_elements(By.TAG_NAME, 'h1')[0].text
        self.assertIn('Monster Card List Api', header_text)
    # they then go to the cards/api/ endpoint, because they want to create a new card
    # they enter their object (might be later refactored to writing out a form)
    # after clicking on POST, they are greeted by their new object
    # the user clicks on refresh
    # they then enter a new card in the api
    # their newest addition is then again added
    # another refresh will be used, to see if all cards have been added
    # they realize that the first card they created had a typo in it, so they go to cards/api/:id to edit it
    # after entering their edited card, they do a PUT request.
    # check if the card has indeed been updated and isn't the same as before
    # the second card that have added was a bit boring, so they decide to delete it
    # they go to cards/api/:id, and are greeted by the card they wanted to delete
    # they request a DELETE for the card
    # and make sure the specified card has actually been deleted 

#! checks if it's been executed from command line, rather than imported from another script
if __name__ == '__main__':  
    #* calling unittest main, launches unittest test runner which automatically finds test classes and methods in the file and runs them
    unittest.main()