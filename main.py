from parser import SoupParser
from driver import FormFiller
import requests
import pprint
import time

FORM_URL = "https://forms.gle/2aWwVWcBM2f2XFFn7"
LISTINGS_URL = "https://appbrewery.github.io/Zillow-Clone/"

pp = pprint.PrettyPrinter(indent=4)

response = requests.get(LISTINGS_URL)
listing_website = response.text

parser = SoupParser(listing_website)
address_list = parser.get_addresses()
price_list = parser.get_prices()
link_list = parser.get_links()

form_filler = FormFiller(FORM_URL)
time.sleep(2)
form_filler.fill_form(address_list, price_list, link_list)
