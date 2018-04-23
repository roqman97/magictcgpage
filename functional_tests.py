from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_decks_list_on_homepage(self):

        # Bob has a new Magic App
        # He goes to the home page
        self.browser.get('http://localhost:8000')

        # The home page shows his list of decks
        self.assertIn('Your Decks', self.browser.title)
        self.fail('Finish writing tests')

        # He has the option to create a new deck, or edit an existing deck
        existing_deck = self.browser.find_element_by_id('deck1')
        new_deck_button = self.browser.find_element_by_id('newDeck')

        # He creates a new deck and titles it "Test Deck 1"

        # When he hits enter, the page changes and shows the card collection screen

        # If Bob clicks on a card, it's added to his deck list

        # If Bob clicks on a card in his deck list, it is removed.

        # When bob leaves the page and comes back, the deck is still saved

        # He can then choose to delete the deck

        # The page updates, and on his home page, that deck is not displayed

if __name__ == '__main__':
    unittest.main(warnings='ignore')