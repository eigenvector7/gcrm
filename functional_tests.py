from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewSessionTest(unittest.TestCase):
    def setUp(self):
        print("Bye World")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Jayne is Introduced to the new CRM which exists at an address
        self.browser.get("http://localhost:8000")
        # She notices the page title and header mention to-do lists
        self.assertIn('G-CRM', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('TO-DO',header_text)


        # She is invited to enter a new client information right away
        inputbox = self.browser.find_element_by_id('id_new_client')

        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a new client information'
        )





        # She fills in the form presented with the information
        inputbox.send_keys('John Doe')
        # When she hits enter, the page updates, and now the page lists
        inputbox.send_keys(keys.Enter)
        time.sleep(1)
        # <Client 1 Persona> <Status> <Notes> <Last Commmunication> <Next Step>
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: John Doe' for row in rows)
        )
        # There is still a form inviting her to add another item. She enters
        # <Client 2 Persona> <Status> <Notes> <Last Commmunication> <Next Step>


        # The page updates again, and now shows both items on her list

        # Jayne wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her CRM is still there.
        self.fail('Finish the test!')

if __name__ == '__main__':
    print("Hello World")
    unittest.main(warnings='ignore')