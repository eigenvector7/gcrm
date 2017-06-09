from selenium import webdriver
import unittest


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
        self.fail('Finish the test!')

        # She is invited to enter a new client information right away

        # She fills in the form presented with the information

        # When she hits enter, the page updates, and now the page lists
        # <Client 1 Persona> <Status> <Notes> <Last Commmunication> <Next Step>

        # There is still a form inviting her to add another item. She enters
        # <Client 2 Persona> <Status> <Notes> <Last Commmunication> <Next Step>


        # The page updates again, and now shows both items on her list

        # Jayne wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her CRM is still there.

if __name__ == '__main__':
    print("Hello World")
    unittest.main(warnings='ignore')